# admin_handler.py – REKLAMA + STATISTIKA + CONTACT REQUEST

import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

from config import ADMIN_ID

SEND_BROADCAST = "send_broadcast"

# =============== ADMIN PANEL MENU ===============
async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("⛔ Bu bo‘lim faqat admin uchun.")
        return

    buttons = [
        [InlineKeyboardButton("📢 Reklama yuborish", callback_data="admin_broadcast")],
        [InlineKeyboardButton("📊 Statistika", callback_data="admin_stats")],
    ]
    markup = InlineKeyboardMarkup(buttons)
    await update.message.reply_text("👨‍💼 Admin paneliga xush kelibsiz!", reply_markup=markup)

# =============== CALLBACKS ===============
async def handle_admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data

    if data == "admin_broadcast":
        await query.message.reply_text("📢 Yubormoqchi bo‘lgan reklama matnini yozing:")
        return SEND_BROADCAST

    elif data == "admin_stats":
        count_profiles = 0
        count_users = set()
        count_vips = 0

        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                count_profiles = len(data)
                for item in data:
                    count_users.add(item.get("user_id"))
                    if item.get("is_vip") == True:
                        count_vips += 1
        except:
            pass

        await query.message.reply_text(
            f"📊 *Bot statistikasi:*\n\n"
            f"👥 Umumiy foydalanuvchilar: {len(count_users)}\n"
            f"📄 Umumiy anketalar: {count_profiles}\n"
            f"💎 VIP profillar: {count_vips}",
            parse_mode="Markdown"
        )

    await query.answer()

# =============== REKLAMA YUBORISH DAVOMI ===============
async def send_broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    success = 0
    fail = 0

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            user_ids = set([d.get("user_id") for d in data])
    except:
        user_ids = []

    for user_id in user_ids:
        try:
            await context.bot.send_message(chat_id=user_id, text=f"📢 REKLAMA:\n\n{text}")
            success += 1
        except:
            fail += 1

    await update.message.reply_text(f"✅ Yuborildi: {success} ta foydalanuvchiga\n❌ Xatolik: {fail} ta")

    return ConversationHandler.END

# =============== PROFIL O‘CHIRISH – ADMIN ===============
async def delete_user_by_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id_text = update.message.text.strip()
    try:
        user_id = int(user_id_text)
        with open("data.json", "r") as file:
            data = json.load(file)
        data = [d for d in data if d.get("user_id") != user_id]
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)

        await update.message.reply_text(f"✅ {user_id} foydalanuvchi o‘chirildi.")
    except:
        await update.message.reply_text("❌ Xatolik! Foydalanuvchini o‘chirishda muammo.")

# =============== CONTACT REQUEST (MAIN.PY ICHIDA KERAK BO‘LGAN) ===============
async def handle_contact_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Kontakt so‘rash funksiyasi ishlamoqda!\nAdminga yozing: @abu94oshiy"
    )
