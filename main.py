from aiogram import Bot, Dispatcher, executor, types
from data.config import BOT_TOKEN
import start, menu, ravza, food, hotel, faq, bozor  # <-- faqat oddiy import

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

# 🔒 Bot uxlamasligi uchun yashirin signal
async def keep_alive():
    while True:
        try:
            await bot.send_chat_action(chat_id=BOT_TOKEN, action=types.ChatActions.TYPING)
        except:
            pass
        await asyncio.sleep(600)

async def on_startup(dispatcher):
    asyncio.create_task(keep_alive())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
