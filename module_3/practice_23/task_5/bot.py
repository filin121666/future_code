import os
from dotenv import load_dotenv
import asyncio
from aiohttp import ClientSession

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.filters.command import Command
from aiogram3_form import Form, FormField
from aiogram.fsm.context import FSMContext

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router=router)


class Create_user_form(Form, router=router):
    username: str = FormField(enter_message_text='Enter username:')
    password: str = FormField(enter_message_text='Enter password:')
    
    
class Update_user_form(Form, router=router):
    old_username: str = FormField(enter_message_text='Enter old username')
    old_password: str = FormField(enter_message_text='Enter old password')
    new_username: str = FormField(enter_message_text='Enter new username')
    new_password: str = FormField(enter_message_text='Enter new password')
    

class Delete_user_form(Form, router=router):
    username: str = FormField(enter_message_text='Enter username')
    password: str = FormField(enter_message_text='Enter password')


@Create_user_form.submit()
async def create_user_form_submit_handler(form: Create_user_form):
    async with ClientSession() as session:
        async with session.post(url='http://127.0.0.1:5001/create_user_api', json={'username': form.username, 'password': form.password}) as resp:
            data: dict = await resp.json()
            if data.get('status_code') == 201:
                created_username = data.get('created_username')
                await form.answer(f'Hello {created_username}')
            elif data.get('status_code') == 400:
                await form.answer('Error 400: Bad Request')


@Update_user_form.submit()
async def update_user_form_submit_handler(form: Update_user_form):
    async with ClientSession() as session:
        async with session.post(url='http://127.0.0.1:5001/update_user_api', json={'old_username': form.old_username, 'old_password': form.old_password, 'new_username': form.new_username, 'new_password': form.new_password}) as resp:
            data: dict = await resp.json()
            if data.get('status_code') == 200:
                updated_username = data.get('updated_username')
                await form.answer(f'Updated username is {updated_username}')
            elif data.get('status_code') == 404:
                await form.answer('Error 404: Not Found')
                

@Delete_user_form.submit()
async def delete_user_form_submit_handler(form: Delete_user_form):
    async with ClientSession() as session:
        async with session.post(url='http://127.0.0.1:5001/delete_user_api', json={'username': form.username, 'password': form.password}) as resp:
            data: dict = await resp.json()
            if data.get('status_code') == 200:
                await form.answer('The user has been successfully deleted')
            elif data.get('status_code') == 404:
                await form.answer('Error 404: Not Found')


@router.message(Command('create_user'))
async def create_form_handler(_, state: FSMContext):
    await Create_user_form.start(bot, state)


@router.message(Command('read_all_users'))
async def read_all_users_handler(message: types.Message):
    async with ClientSession() as session:
        async with session.get(url='http://127.0.0.1:5001/read_all_users_api') as resp:
            data = await resp.json()
            for i in data:
                await message.answer(f'{i}\n')
                

@router.message(Command('update_user'))
async def update_user_handler(_, state: FSMContext):
    await Update_user_form.start(bot, state)


@router.message(Command('delete_user'))
async def delete_user_handler(_, state: FSMContext):
    await Delete_user_form.start(bot, state)


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='/create_user'),
            types.KeyboardButton(text='/read_all_users')
        ],
        [
            types.KeyboardButton(text='/update_user'),
            types.KeyboardButton(text='/delete_user')
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb, resize_keyboard=True, one_time_keyboard=True)
    await message.answer('Select the command', reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
