# handlers/food.py
from aiogram import types, Dispatcher
from handlers.start import t_user_lang

async def food_handler(message: types.Message):
    user_id = message.from_user.id
    lang = t_user_lang.get(user_id, "🇺🇿 O'zbekcha")

    if lang == "🇺🇿 O'zbekcha":
        text = (
            "🍽 <b>Ўзбек таомлари</b>\n\n"
            "Мадинада сиз учун хуштаъм ва сифатли таомлар тайёрланади.\n\n"
            "📌 2 маҳал овқат (доставка): <b>28 SR</b>\n"
            "📌 Буфия хизмати: <b>30 SR</b>\n\n"
            "📩 <b>Мурожаат учун:</b> @Abumadani77\n"
            "🧑‍💼 <b>Бот асосчиси:</b> @abu94oshiy"
        )
        await message.answer(text, parse_mode="HTML")


def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(food_handler, lambda message: message.text == "🍽 Ўзбек таомлари")
