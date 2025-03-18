
from aiogram import Bot, Dispatcher, executor, types
from aiohttp import web
import logging
import asyncio
import os

API_TOKEN = os.getenv("BOT_TOKEN", "your_token_here")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! Bu Ravza bot 24/7 ishlamoqda.")

# Ping endpoint
async def handle_ping(request):
    return web.Response(text='Bot alive!')

async def on_startup(_):
    app.router.add_get('/ping', handle_ping)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = web.Application()
    app.router.add_get('/ping', handle_ping)
    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    loop.run_until_complete(site.start())
    executor.start_polling(dp, skip_updates=True)
