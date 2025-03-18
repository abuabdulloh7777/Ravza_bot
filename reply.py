# keyboards/reply.py (Javob tugmalari)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# 🔸 Til tanlash tugmalari
tillar = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
tillar.add(
    KeyboardButton("🇺🇿 O'zbekcha"),
    KeyboardButton("🇷🇺 Русский"),
    KeyboardButton("🇸🇦 العربية")
)

# 🔸 Asosiy menu — O'zbek tili uchun
menu_uz = ReplyKeyboardMarkup(resize_keyboard=True)
menu_uz.add(
    KeyboardButton("🕌 Равза"),
    KeyboardButton("🏨 Меҳмонхона"),
    KeyboardButton("🍽 Ўзбек таомлари"),
    KeyboardButton("❓ Савол-жавоб"),
    KeyboardButton("🛍 Бозор")
)
menu_uz.add(KeyboardButton("⬅️ Орқага"))

# 🔸 Asosiy menu — Rus tili uchun (faqat Равза bo‘limi)
menu_ru = ReplyKeyboardMarkup(resize_keyboard=True)
menu_ru.add(KeyboardButton("🕌 Равза"))
menu_ru.add(KeyboardButton("⬅️ Назад"))

# 🔸 Asosiy menu — Arab tili uchun (faqat رَوضَة bo‘limi)
menu_ar = ReplyKeyboardMarkup(resize_keyboard=True)
menu_ar.add(KeyboardButton("🕌 رَوضَة"))
menu_ar.add(KeyboardButton("⬅️ رجوع"))

# 🔸 Ortga qaytish tugmalari
back_uz = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("⬅️ Орқага"))
back_ru = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("⬅️ Назад"))
back_ar = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("⬅️ رجوع"))
