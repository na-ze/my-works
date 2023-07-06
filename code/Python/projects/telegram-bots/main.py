import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from config import TOKEN


bot = Bot(TOKEN, parse_mode = "HTML")
dp = Dispatcher(bot)


if __name__ == "__main__":
    from handlers import dp, bot, HELP, on_startup
    executor.start_polling(dp, on_startup=on_startup)
