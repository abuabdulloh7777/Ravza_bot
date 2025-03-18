# handlers/faq.py
from aiogram import types, Dispatcher
from handlers.start import t_user_lang

async def faq_handler(message: types.Message):
    user_id = message.from_user.id
    lang = t_user_lang.get(user_id, "🇺🇿 O'zbekcha")

    if lang == "🇺🇿 O'zbekcha":
        text = (
            "❓ <b>Савол-жавоб</b>\n\n"
            "Агар саволингиз бўлса, бизга мурожаат қилинг.\n\n"
            "📩 <b>Мурожаат учун:</b> @Abumadani77\n"
            "🧑‍💼 <b>Бот асосчиси:</b> @abu94oshiy"
        )
        await message.answer(text, parse_mode="HTML")


def register_handlers_faq(dp: Dispatcher):
    dp.register_message_handler(faq_handler, lambda message: message.text == "❓ Савол-жавоб")
