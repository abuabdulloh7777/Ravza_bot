# handlers/ravza.py
from aiogram import types, Dispatcher
from handlers.start import t_user_lang

async def ravza_handler(message: types.Message):
    user_id = message.from_user.id
    lang = t_user_lang.get(user_id, "🇺🇿 O'zbekcha")

    if lang == "🇺🇿 O'zbekcha":
        text = (
            "🕌 <b>Равза хизмати ҳақида</b>\n\n"
            "📜 Ҳадис:\nما بين بيتي ومنبري روضة من رياض الجنة\n"
            "“Менинг уйим ва минбарим орасидаги жой — жаннат боғларидан бир боғдир.”\n"
            "📚 Ровий: Имом Бухорий ва Муслим\n\n"
            "📌 Равза хизмати нархи: 5 SR\n\n"
            "📣 Муҳим эслатма:\n"
            "Гуруҳ раҳбарлари ва умра ширкати масъулларига:\n"
            "Мадинаи Мунавварага гуруҳингиз келишига 3–5 кун қолганда визаларни бизга юборинг.\n"
            "Сиз келгунингизгача шу сана учун навбат олиб қўйилади, иншаАллоҳ.\n\n"
            "📩 Мурожаат учун: @Abumadani77\n"
            "🧑‍💼 Бот асосчиси: @abu94oshiy"
        )
    elif lang == "🇷🇺 Русский":
        text = (
            "🇷🇺 О сервисе Равза\n\n"
            "📜 Хадис:\nما بين بيتي ومنبري روضة من رياض الجنة\n"
            "«Место между моим домом и минбаром — один из садов рая».\n"
            "📚 Передал: Имам Бухари и Муслим\n\n"
            "📌 Стоимость сервиса Равза: 5 SR\n\n"
            "📣 Важное напоминание:\n"
            "Руководителям групп и умра-компаниям:\n"
            "Отправьте визы за 3–5 дней до прибытия группы в Медину.\n"
            "Очередь будет заранее забронирована, ин шаа Аллах.\n\n"
            "📩 Для связи: @Abumadani77\n"
            "🧑‍💼 Админ бота: @abu94oshiy"
        )
    elif lang == "🇸🇦 العربية":
        text = (
            "🇸🇦 خدمة الروضة الشريفة\n\n"
            "📜 الحديث:\nما بين بيتي ومنبري روضة من رياض الجنة\n"
            "ما بين بيتي ومنبري روضة من رياض الجنة\n"
            "📚 الراوي: الإمام البخاري ومسلم\n\n"
            "📌 رسوم الخدمة: 5 ريال سعودي\n\n"
            "📣 ملاحظة مهمة:\n"
            "على رؤساء المجموعات وشركات العمرة إرسال التأشيرات قبل 3 إلى 5 أيام من الوصول إلى المدينة المنورة.\n"
            "سيتم حجز الدور مسبقًا إن شاء الله.\n\n"
            "📩 للتواصل: @Abumadani77\n"
            "🧑‍💼 مشرف البوت: @abu94oshiy"
        )

    await message.answer(text)


def register_handlers_ravza(dp: Dispatcher):
    dp.register_message_handler(ravza_handler, lambda message: message.text in ["🕌 Равза", "🕌 Равза", "🕌 رَوضَة"])
