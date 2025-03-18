# handlers/bozor.py
from aiogram import types, Dispatcher
from handlers.start import t_user_lang
from data.config import ADMIN_ID

# Foydalanuvchilar ro'yxati (uzbek tilidagilar)
uzbek_users = set()

async def bozor_handler(message: types.Message):
    user_id = message.from_user.id
    lang = t_user_lang.get(user_id, "🇺🇿 O'zbekcha")

    # Foydalanuvchi uzbek tilida bo‘lsa ro‘yxatga qo‘shamiz
    if lang == "🇺🇿 O'zbekcha":
        uzbek_users.add(user_id)

    # Faqat admin yozishi mumkin
    if str(user_id) == str(ADMIN_ID):
        await message.answer("🛍 Илтимос, эълон матнини юборинг. У барча ўзбек фойдаланувчиларга юборилади.")
        # Keyingi bosqichda matnni olish uchun keyingi handler kutadi
        # Bu uchun oddiy FSM ham ishlatish mumkin, lekin oddiy usulda yozamiz quyida
        bozor_handler.waiting_for_text = True
    else:
        await message.answer("🛍 Бу бўлим фақат админ учун фаол. Эълонлар бу ерда чиқади.")

# Admin e'lon yuborganda — barcha uzbek tilidagilarga yuboriladi
async def bozor_send_announcement(message: types.Message):
    user_id = message.from_user.id
    if str(user_id) != str(ADMIN_ID):
        return

    if getattr(bozor_handler, "waiting_for_text", False):
        text = message.text
        for uid in uzbek_users:
            try:
                await message.bot.send_message(chat_id=uid, text=f"📢 <b>Янги эълон:</b>\n{text}", parse_mode="HTML")
            except:
                continue
        bozor_handler.waiting_for_text = False
        await message.answer("✅ Эълон юборилди.")


def register_handlers_bozor(dp: Dispatcher):
    dp.register_message_handler(bozor_handler, lambda message: message.text == "🛍 Бозор")
    dp.register_message_handler(bozor_send_announcement)
