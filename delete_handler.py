# delete_handler.py

import json
from telegram import ReplyKeyboardMarkup
from telegram.ext import ConversationHandler

CONFIRM_DELETE = "confirm_delete"

async def confirm_delete_prompt(update, context):
    buttons = [["Ha, o‘chirish", "Yo‘q, bekor qilish"]]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)

    await update.message.reply_text(
        "❗ Siz haqiqatdan profilingizni o‘chirmoqchimisiz?",
        reply_markup=reply_markup
    )
    return CONFIRM_DELETE

async def delete_profile(update, context):
    answer = update.message.text.lower()
    user_id = update.message.from_user.id

    if "ha" in answer:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except:
            data = []

        new_data = [p for p in data if p.get("user_id") != user_id]

        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)

        await update.message.reply_text("✅ Sizning profilingiz o‘chirildi.")
    else:
        await update.message.reply_text("❌ Profilni o‘chirish bekor qilindi.")

    return ConversationHandler.END
