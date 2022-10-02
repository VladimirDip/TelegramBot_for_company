from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile

from create_bot import dp

from keyboard.user_buttons import greet_kb


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.id} {message.from_user.full_name}!'
                         f'Жми /menu', reply_markup=greet_kb)


@dp.message_handler(text='Catalog')
async def bot_start(message: types.Message):
    document_path = InputFile(path_or_bytesio='files/Новогодний каталог ч.2.pdf')
    await dp.bot.send_document(chat_id=message.from_user.id, document=document_path)
