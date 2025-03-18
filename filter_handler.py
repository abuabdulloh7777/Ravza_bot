# filter_handler.py

import json
import os
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from anketa_handler import format_profile

FILTER_STEP = "filter_step"
FILTER_CITY = "filter_city"
FILTER_MIN_AGE = "filter_min_age"
FILTER_MAX_AGE = "filter_max_age"

async def filter_start(update, context):
    await update.message.reply_text("📍 Qaysi shahar bo‘yicha izlayapsiz?")
    return FILTER_CITY

async def filter_city(update, context):
    context.user_data["filter_city"] = update.message.text
    await update.message.reply_text("🕒 Eng kichik yosh (masalan: 20):")
    return FILTER_MIN_AGE

async def filter_min_age(update, context):
    try:
        context.user_data["min_age"] = int(update.message.text)
    except:
        await update.message.reply_text("❗ Faqat raqam yozing. Qayta kiriting:")
        return FILTER_MIN_AGE

    await update.message.reply_text("🕒 Eng katta yosh (masalan: 30):")
    return FILTER_MAX_AGE

async def filter_max_age(update, context):
    try:
        context.user_data["max_age"] = int(update.message.text)
    except:
        await update.message.reply_text("❗ Faqat raqam yozing. Qayta kiriting:")
        return FILTER_MAX_AGE

    city = context.user_data["filter_city"]
    min_age = context.user_data["min_age"]
    max_age = context.user_data["max_age"]

    try:
        with open("data.json", "r") as file:
            all_data = json.load(file)
    except:
        all_data = []

    matched = []
    for profile in all_data:
        try:
            age = int(profile.get("age", 0))
        except:
            continue

        if (
            profile.get("city", "").lower() == city.lower()
            and min_age <= age <= max_age
        ):
            matched.append(profile)

    if not matched:
        await update.message.reply_text("❗ Siz so‘ragan mezonlarga mos profil topilmadi.")
        return -1

    await update.message.reply_text(f"✅ Topildi: {len(matched)} ta profil")

    for profile in matched:
        profile_text = format_profile(profile)
        user_id = profile.get("user_id")
        photo_path = f"media/{user_id}.jpg"

        button = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("📞 Bog‘lanish", callback_data=f"connect_{user_id}"),
                InlineKeyboardButton("❤️ Yoqdi", callback_data=f"like_{user_id}")
            ]
        ])

        if os.path.exists(photo_path):
            await update.message.reply_photo(photo=open(photo_path, "rb"), caption=profile_text, reply_markup=button, parse_mode="Markdown")
        else:
            await update.message.reply_text(profile_text, reply_markup=button, parse_mode="Markdown")

    return -1
