# anket_list_handler.py

import json
from telegram import Update
from telegram.ext import ContextTypes

async def show_all_profiles(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open("data.json", "r") as file:
            profiles = json.load(file)
    except:
        profiles = []

    if not profiles:
        await update.message.reply_text("⛔ Hozircha hech qanday anketa topilmadi.")
        return

    count = 0
    for profile in profiles:
        # Har bir profilni chiroyli formatda chiqaramiz
        profile_text = format_profile(profile)
        await update.message.reply_text(profile_text)
        count += 1

        # Cheklash: 10 ta profil ko‘rsatamiz maksimal (xohlasangiz o‘zgartirasiz)
        if count >= 10:
            break

def format_profile(data):
    return f"""
━━━━━━━━━━━━━━━
👤 **Ism:** {data.get('name', '❗Ko‘rsatilmagan')}
🕒 **Yosh:** {data.get('age', '❗Ko‘rsatilmagan')}
📍 **Shahar:** {data.get('city', '❗Ko‘rsatilmagan')}
🕌 **Musulmonmi?:** {data.get('islam', '❗Ko‘rsatilmagan')}
🧕 **Namoz o‘qiysizmi?:** {data.get('prayer', '❗Ko‘rsatilmagan')}
📖 **Qur’on o‘qishni bilasizmi?:** {data.get('quran', '❗Ko‘rsatilmagan')}
📚 **Fiqh yo‘nalishi:** {data.get('fiqh', '❗Ko‘rsatilmagan')}
❤️ **Juft izlaydi:** {data.get('partner_age', '❗Ko‘rsatilmagan')}
📝 **O‘zi haqida:** {data.get('about', '❗Ko‘rsatilmagan')}
📩 **Bog‘lanish uchun admin bilan aloqaga chiqing.**
━━━━━━━━━━━━━━━
"""
