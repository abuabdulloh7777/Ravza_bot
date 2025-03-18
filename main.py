from aiogram import Bot, Dispatcher, executor, types
from data.config import BOT_TOKEN, ADMIN_ID  # ADMIN_ID ni config.py ga qo‘shing
from data.handlers import start, menu, ravza, food, hotel, faq, bozor
import asyncio

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# Har bir bo‘limni ro‘yxatdan o‘tkazamiz
start.register_handlers_start(dp)
menu.register_handlers_menu(dp)
ravza.register_handlers_ravza(dp)
hotel.register_handlers_hotel(dp)
food.register_handlers_food(dp)
faq.register_handlers_faq(dp)
bozor.register_handlers_bozor(dp)

# 🔒 Foydalanuvchiga ko‘rinmas "keep-alive" signal
async def keep_alive():
    while True:
        try:
            await bot.send_chat_action(chat_id=ADMIN_ID, action=types.ChatActions.TYPING)
        except:
            pass
        await asyncio.sleep(600)  # 10 daqiqa

async def on_startup(dispatcher):
    asyncio.create_task(keep_alive())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
