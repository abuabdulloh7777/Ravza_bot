# handlers/hotel.py
from aiogram import types, Dispatcher
from handlers.start import t_user_lang

async def hotel_handler(message: types.Message):
    user_id = message.from_user.id
    lang = t_user_lang.get(user_id, "🇺🇿 O'zbekcha")

    if lang == "🇺🇿 O'zbekcha":
        text = (
            "🏨 <b>Меҳмонхона хизмати — Мадина ва Маккада!</b>\n\n"
            "🏢 Биз зиёратчилар учун <b>Мадина</b> ва <b>Макка</b> шаҳарларида қулай, тоза ва яқин масофадаги меҳмонхоналарни таклиф қиламиз.\n\n"
            "📌 Бюджетингизга мос турли вариантлар мавжуд.\n"
            "📌 Олдиндан банд қилиш имконияти бор.\n"
            "📌 Гуруҳлар учун ҳам алоҳида жойлашув хизматлари мавжуд.\n\n"
            "📩 <b>Мурожаат учун:</b> @Abumadani77\n"
            "🧑‍💼 <b>Бот асосчиси:</b> @abu94oshiy"
        )
        await message.answer(text, parse_mode="HTML")


def register_handlers_hotel(dp: Dispatcher):
    dp.register_message_handler(hotel_handler, lambda message: message.text == "🏨 Меҳмонхона")
