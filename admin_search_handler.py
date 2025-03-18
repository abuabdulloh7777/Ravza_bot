# admin_search_handler.py

import json
from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID

DATA_FILE = "data.json"

async def search_profile_by_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id

    # Faqat admin foydalanishi mumkin
    if user_id != ADMIN_ID:
        await update.message.reply_text("🚫 Sizda bu funksiyadan foydalanish huquqi yo‘q.")
        return

    text = update.message.text.strip()
    if not text.startswith("#"):
        await update.message.reply_text("❗ Iltimos, anketani raqam bilan yuboring. Masalan: #12")
        return

    try:
        number = int(text[1:])
    except:
        await update.message.reply_text("❗ Noto‘g‘ri format. Masalan: #12 deb yuboring.")
        return

    try:
        with open(DATA_FILE, "r") as file:
            profiles = json.load(file)
    except:
        await update.message.reply_text("❗ Ma’lumotlar topilmadi.")
        return

    for profile in profiles:
        if profile.get("profile_number") == number:
            username = profile.get("username", "Noma’lum")
            text = f"""
📋 Anketa raqami: #{number}
👤 Ism: {profile.get('name')}
🕒 Yosh: {profile.get('age')}
📍 Shahar: {profile.get('city')}
📏 Bo‘y: {profile.get('height')} sm
⚖ Vazn: {profile.get('weight')} kg
🕌 Musulmon: {profile.get('islam')}
🧕 Namoz o‘qiydi: {profile.get('prayer')}
📖 Qur’on bilimi: {profile.get('quran')}
📚 Fiqh: {profile.get('fiqh')}
👶 Farzand: {profile.get('children')}
❤️ Juft talablari: {profile.get('partner_criteria')}
🎨 Xarakter va hobbi: {profile.get('hobby')}
📝 O‘zi haqida: {profile.get('about')}
🔗 Telegram username: @{username}
"""
            await update.message.reply_text(text)
            return

    await update.message.reply_text(f"❗ #{number}-raqamli anketa topilmadi.")
