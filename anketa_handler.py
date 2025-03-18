# 📂 anketalarni boshqaruvchi fayl
# ✅ To‘liq importlar PRO versiya uslubida
import json
import os

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)
from telegram.ext import (
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    CommandHandler,
    CallbackQueryHandler,
    filters
)

# ========== Anketa bosqichlari ==========
GENDER, NAME, AGE, CITY, HEIGHT, WEIGHT, ISLAM, PRAYER, QURAN, FIQH, CHILDREN, CRITERIA, HOBBY, ABOUT, PHOTO = range(15)


# ====== Boshlash ======
async def start_anketa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[KeyboardButton("🧔 Erkak"), KeyboardButton("👩 Ayol")]]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text("Jinsingizni tanlang:", reply_markup=markup)
    return GENDER

async def get_gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["gender"] = update.message.text
    await update.message.reply_text("Ismingizni yozing:")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("Yoshingizni yozing:")
    return AGE

async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["age"] = update.message.text
    await update.message.reply_text("Shahar nomini yozing:")
    return CITY

async def get_city(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["city"] = update.message.text
    await update.message.reply_text("Bo‘yingizni yozing (sm):")
    return HEIGHT

async def get_height(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["height"] = update.message.text
    await update.message.reply_text("Vazningizni yozing (kg):")
    return WEIGHT

async def get_weight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["weight"] = update.message.text
    await update.message.reply_text("Musulmonmisiz? (ha/yo‘q):")
    return ISLAM

async def get_islam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["islam"] = update.message.text
    await update.message.reply_text("Namoz o‘qiysizmi? (ha/yo‘q):")
    return PRAYER

async def get_prayer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["prayer"] = update.message.text
    await update.message.reply_text("Qur’on o‘qiy olasizmi? (ha/yo‘q):")
    return QURAN

async def get_quran(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["quran"] = update.message.text
    await update.message.reply_text("Fiqh bo‘yicha bilim darajangiz (yoki + / -):")
    return FIQH

async def get_fiqh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["fiqh"] = update.message.text
    await update.message.reply_text("Farzandingiz bormi? (ha/yo‘q):")
    return CHILDREN

async def get_children(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["children"] = update.message.text
    await update.message.reply_text("Juftingizga qo‘yiladigan talablar:")
    return CRITERIA

async def get_criteria(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["criteria"] = update.message.text
    await update.message.reply_text("Xarakteringiz, hobbilaringiz:")
    return HOBBY

async def get_hobby(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["hobby"] = update.message.text
    await update.message.reply_text("O‘zingiz haqida qisqacha yozing:")
    return ABOUT

async def get_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["about"] = update.message.text
    await update.message.reply_text("📸 Rasmingizni yuboring (ixtiyoriy):")
    return PHOTO

async def get_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    username = update.message.from_user.username or "Noma'lum"

    if update.message.photo:
        file = await update.message.photo[-1].get_file()
        photo_path = f"photos/{user_id}.jpg"
        await file.download_to_drive(photo_path)

    # Saqlash
    try:
        with open("data.json", "r") as f:
            users = json.load(f)
    except FileNotFoundError:
        users = []

    profile = {
        "user_id": user_id,
        "username": username,
        "gender": context.user_data.get("gender"),
        "name": context.user_data.get("name"),
        "age": context.user_data.get("age"),
        "city": context.user_data.get("city"),
        "height": context.user_data.get("height"),
        "weight": context.user_data.get("weight"),
        "islam": context.user_data.get("islam"),
        "prayer": context.user_data.get("prayer"),
        "quran": context.user_data.get("quran"),
        "fiqh": context.user_data.get("fiqh"),
        "children": context.user_data.get("children"),
        "criteria": context.user_data.get("criteria"),
        "hobby": context.user_data.get("hobby"),
        "about": context.user_data.get("about"),
        "photo": f"{user_id}.jpg",
        "profile_number": len(users) + 1
    }
    users = [u for u in users if u["user_id"] != user_id]
    users.append(profile)

    with open("data.json", "w") as f:
        json.dump(users, f, indent=2)

    text = f"""
✅ Anketangiz saqlandi!

━━━━━━━━━━━━━━━
👤 Ism: 📝 {profile['name']}
🕒 Yosh: 📝 {profile['age']}
📍 Shahar: 📝 {profile['city']}
📏 Bo‘y: 📝 {profile['height']} sm
⚖ Vazn: 📝 {profile['weight']} kg
🕌 Musulmonmisiz: 📝 {profile['islam']}
🧕 Namoz o‘qiysizmi: 📝 {profile['prayer']}
📖 Qur’on bilimi: 📝 {profile['quran']}
📚 Fiqh: 📝 {profile['fiqh']}
👶 Farzand: 📝 {profile['children']}
❤️ Juft talablari: 📝 {profile['criteria']}
🎨 Xarakter va hobbi: 📝 {profile['hobby']}
📝 O‘zi haqida: 📝 {profile['about']}
📩 Aloqa: Admin orqali — @abu94oshiy
━━━━━━━━━━━━━━━

✅ Bu sizning anketangiz.
"""

    photo_path = f"photos/{user_id}.jpg"
    if os.path.exists(photo_path):
        with open(photo_path, "rb") as photo_file:
            await update.message.reply_photo(photo=photo_file, caption=text, parse_mode="Markdown")
    else:
        await update.message.reply_text(text, parse_mode="Markdown")
    return ConversationHandler.END

# Profilni ko‘rish
async def show_my_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    profile = next((item for item in data if item["user_id"] == user_id), None)
    if profile:
        text = f"""
👤 Ism: {profile['name']}
🕒 Yosh: {profile['age']}
📍 Shahar: {profile['city']}
📏 Bo‘y: {profile['height']} sm
⚖ Vazn: {profile['weight']} kg
🕌 Musulmon: {profile['islam']}
🧕 Namoz: {profile['prayer']}
📖 Qur’on: {profile['quran']}
📚 Fiqh: {profile['fiqh']}
👶 Farzand: {profile['children']}
❤️ Talablar: {profile['criteria']}
🎨 Xarakter va hobbi: {profile['hobby']}
📝 O‘zi haqida: {profile['about']}
📩 Aloqa: Admin — @abu94oshiy
"""
        photo_path = f"photos/{user_id}.jpg"
        if os.path.exists(photo_path):
            with open(photo_path, "rb") as photo:
                await update.message.reply_photo(photo=photo, caption=text, parse_mode="Markdown")
        else:
            await update.message.reply_text(text, parse_mode="Markdown")
    else:
        await update.message.reply_text("❗ Sizda hali anketa yo‘q.")

# ✅ Formatlangan profilni chiqaruvchi funksiya
def format_profile(profile):
    return f"""━━━━━━━━━━━━━━━
👤 Ism: 📝 {profile.get("name", "-")}
🕒 Yosh: 📝 {profile.get("age", "-")}
📍 Shahar: 📝 {profile.get("city", "-")}
📏 Bo‘y: 📝 {profile.get("height", "-")} sm
⚖ Vazn: 📝 {profile.get("weight", "-")} kg
🕌 Musulmonmisiz: 📝 {profile.get("islam", "-")}
🧕 Namoz o‘qiysizmi: 📝 {profile.get("prayer", "-")}
📖 Qur’on bilimi: 📝 {profile.get("quran", "-")}
📚 Fiqh: 📝 {profile.get("fiqh", "-")}
👶 Farzand: 📝 {profile.get("children", "-")}
❤️ Juft talablari: 📝 {profile.get("criteria", "-")}
🎨 Xarakter va hobbi: 📝 {profile.get("hobby", "-")}
📝 O‘zi haqida: 📝 {profile.get("about", "-")}
📩 Aloqa: Admin orqali — @abu94oshiy
━━━━━━━━━━━━━━━"""
    

# ✅ Foydalanuvchining profilini user_id orqali topish
def load_profile_by_user_id(user_id):
    try:
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except:
        data = []

    for profile in data:
        if profile.get("user_id") == user_id:
            return profile
    return None
