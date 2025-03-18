# handlers/menu.py
from aiogram import types, Dispatcher
from keyboards.reply import menu_uz, menu_ru, menu_ar, tillar
from handlers.start import t_user_lang

# Ortga qaytish hisoblagichi
user_back_counter = {}

# Ortga tugmasi ishlovchi funksiya
async def back_handler(message: types.Message):
    user_id = message.from_user.id
    lang = t_user_lang.get(user_id, "🇺🇿 O'zbekcha")
    user_back_counter[user_id] = user_back_counter.get(user_id, 0) + 1

    if user_back_counter[user_id] == 1:
        # Asosiy menyuga qaytish
        if lang == "🇺🇿 O'zbekcha":
            await message.answer("👇 Қуйидаги меню орқали бўлимни танланг:", reply_markup=menu_uz)
        elif lang == "🇷🇺 Русский":
            await message.answer("👇 Выберите раздел:", reply_markup=menu_ru)
        elif lang == "🇸🇦 العربية":
            await message.answer("👇 اختر القسم:", reply_markup=menu_ar)

    elif user_back_counter[user_id] >= 2:
        # Til tanlashga qaytish
        await message.answer("👇 Iltimos, tilni tanланг:", reply_markup=tillar)
        user_back_counter[user_id] = 0  # Reset counter

# Handlerlarni ro'yxatdan o'tkazamiz
def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(back_handler, lambda message: message.text in ["⬅️ Орқага", "⬅️ Назад", "⬅️ رجوع"])
