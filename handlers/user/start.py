from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InputFile

from keyboard.user_buttons import inline_kb1

from create_bot import dp


async def _download_catalogs(path_or_bytesio=None, chat_id=None):
    document_path = InputFile(path_or_bytesio=path_or_bytesio)
    await dp.bot.send_document(chat_id=chat_id, document=document_path)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.id} {message.from_user.full_name}!\n'
                         f'Жми "Скачать каталог"', reply_markup=inline_kb1)


@dp.message_handler(text='Catalog')
async def bot_start(message: types.Message):
    document_path = InputFile(path_or_bytesio='files/Новогодний каталог ч.2.pdf')
    await dp.bot.send_document(chat_id=message.from_user.id, document=document_path)


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    await dp.bot.answer_callback_query(callback_query.id)

    match callback_query.data:
        case 'Catalog_new_year2':
            await _download_catalogs('files/Новогодний каталог ч.2.pdf', callback_query.from_user.id)
            text = 'пожалуйста ваш новогодний каталог'
        case 'Catalog_opors':
            await _download_catalogs('files/Каталог Опор.pdf', callback_query.from_user.id)
            text = 'пожалуйста ваш каталог опор'
        case _:
            await dp.bot.answer_callback_query(callback_query.id, show_alert=True)

    print(callback_query.id)
    await dp.bot.answer_callback_query(callback_query.id,
                                       show_alert=True,
                                       text=text)
