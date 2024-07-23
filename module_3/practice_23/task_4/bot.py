from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Hello world!')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
