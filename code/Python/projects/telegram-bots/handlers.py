from aiogram.types import Message
from main import dp, bot

HELP = """
/start - Запуск бота
/help - список комманд
/sasha - спам саше
"""

 
async def on_startup(dp):
    await bot.send_message(1677373526, "Я родился!")

@dp.message_handler(commands = ['help'])
async def help_command(message: Message):
    await message.reply(HELP)

@dp.message_handler(commands = ['start'])
async def start_command(message: Message):
    await bot.send_message(message.from_user.id, f"Привет, я бот")
    await message.delete()

@dp.message_handler(commands = ["sasha"])
async def sasha(message: Message):
    for i in range(1,101):
        await bot.send_message(819315911, f"{i})Соси хуй")
