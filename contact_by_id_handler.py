# contact_by_id_handler.py

import json
from config import ADMIN_ID

async def get_contact_by_id(update, context):
    if update.message.from_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Bu buyruq faqat admin uchun.")
        return

    args = context.args
    if not args or not args[0].isdigit():
        await update.message.reply_text("❗ Iltimos, to‘g‘ri formatda yozing: /kontakt [ID]\nMasalan: /kontakt 3")
        return

    profile_id = int(args[0])

    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        data = []

    profile = next((p for p in data if p.get("ID") == profile_id), None)

    if not profile:
        await update.message.reply_text("❌ Bunday ID raqamli anketa topilmadi.")
        return

    username = profile.get("Username", "no_username")
    await update.message.reply_text(f"📞 {profile['Ism']} profili uchun kontakt: @{username}")
