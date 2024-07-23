from aiogram.filters import BaseFilter
from aiogram.filters.command import Command
from aiogram import Bot, Dispatcher, types
import asyncio
import logging
import dotenv
import os

dotenv.load_dotenv()

TOKEN = os.getenv('TOKEN')
USERS = os.getenv('USERS')

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher()


class IsAdminFilter(BaseFilter):

    async def __call__(self, message: types.Message):
        if str(message.from_user.id) in USERS:
            return True
        else:
            message.answer('Вы кто вообще ? ')
            return False


@dp.message(IsAdminFilter(), Command("start"))
async def cmd_start(message: types.Message):
    print(message.from_user.full_name, message.from_user.username)
    await message.answer(text=f'Здравствуйте {message.from_user.full_name}. Ваш username {message.from_user.username}')


async def main():
    await dp.start_polling(bot)

asyncio.run(main())