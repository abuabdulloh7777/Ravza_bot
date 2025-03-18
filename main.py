from aiogram import Bot, Dispatcher, executor, types
from aiohttp import web
import logging
import asyncio

# BOT TOKEN — siz bergan token to'g'ridan-to'g'ri yozildi
API_TOKEN = "8074896764:AAEvBNUgvcLTu_pf9mdb_GdH7FEc0frZl0M"

# Logging
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start komandasi
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Bu Ravza bot 24/7 ishlamoqda.")

# Ping endpoint (Render uchun)
async def handle_ping(request):
    return web.Response(text='Bot alive!')

# Startup
async def on_startup(_):
    app.router.add_get('/ping', handle_ping)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # Web app (ping uchun)
    app = web.Application()
    app.router.add_get('/ping', handle_ping)
    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    loop.run_until_complete(site.start())

    # Botni ishga tushurish
    executor.start_polling(dp, skip_updates=True)
