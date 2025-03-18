from aiogram import Bot, Dispatcher, executor, types
import logging
import asyncio

API_TOKEN = "8074896764:AAHUpA3FQnX5178l1WmaWQu6Wbgx30U3htg"  # <-- E'tibor bering: tokenni shu yerga yozing

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# USER ID — shu foydalanuvchiga har 10 daqiqada xabar yuboriladi
TARGET_CHAT_ID = 5928661068  # <-- BUNI o'zingizning Telegram ID bilan almashtiring (pastda aytaman qanday olishni)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Bu bot 24/7 ishlaydi ✅")

# 🔄 Har 10 daqiqada xabar yuboruvchi background task
async def periodic_sender():
    while True:
        try:
            await bot.send_message(TARGET_CHAT_ID, "⏰ Bot hali ham ishlayapti — 24/7 faol!")
        except Exception as e:
            logging.warning(f"Xabar yuborishda xatolik: {e}")
        await asyncio.sleep(600)  # 600 sekund = 10 daqiqa

# ✅ Startup funksiyada background taskni boshlaymiz
async def on_startup(dispatcher):
    asyncio.create_task(periodic_sender())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
