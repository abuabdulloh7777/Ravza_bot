# handlers/users.py

from aiogram import types, Dispatcher
from data.config import ADMIN_ID

user_list = set()

async def save_user_info(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    user_info = f"{user_id} | {full_name} | @{username if username else 'username yo‘q'}"
    user_list.add(user_info)

async def show_users(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Бу бўлим фақат админ учун.")
    if not user_list:
        return await message.answer("📋 Фойдаланувчилар рўйхати бўш.")
    text = "📋 <b>Фойдаланувчилар рўйхати:</b>\n\n" + "\n".join(user_list)
    await message.answer(text, parse_mode='HTML')

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(show_users, commands=['users'])
    dp.register_message_handler(save_user_info, content_types=types.ContentType.TEXT)
