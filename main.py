# main.py (asosiy fayl)
from aiogram import Bot, Dispatcher, executor, types
from data.config import BOT_TOKEN
from handlers import start, menu, ravza, food, hotel, faq, bozor
import asyncio

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Har bir bo'limni ro'yxatdan o'tkazamiz
start.register_handlers_start(dp)
menu.register_handlers_menu(dp)
ravza.register_handlers_ravza(dp)
hotel.register_handlers_hotel(dp)
food.register_handlers_food(dp)
faq.register_handlers_faq(dp)
bozor.register_handlers_bozor(dp)

# 🔒 Maxsus yashirin xabar yuboruvchi task (foydalanuvchilar ko‘rmaydi)
async def silent_keepalive():
    while True:
        try:
            await bot.send_chat_action(chat_id=BOT_TOKEN, action=types.ChatActions.TYPING)
        except Exception:
            pass
        await asyncio.sleep(600)  # 10 daqiqa (600 sekund)

async def on_startup(dispatcher):
    asyncio.create_task(silent_keepalive())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
