from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types

from utils.db_api import models
from utils.db_api.database import session
from create_bot import dp

from handlers.admin.admin_buttons import inline_button_1

session_connect = session()


class FSMAdmin(StatesGroup):
    document = State()
    title = State()


@dp.message_handler(commands='upload', state=None)
async def cm_start(message: types.Message):
    await FSMAdmin.document.set()
    await message.reply('Загрузи каталог', reply_markup=inline_button_1)


@dp.message_handler(content_types=types.ContentType.DOCUMENT, state=FSMAdmin.document)
async def load_catalog(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['document'] = message.document.file_id
    await FSMAdmin.next()
    await message.reply('Теперь введи название', reply_markup=inline_button_1)


@dp.message_handler(state=FSMAdmin.title)
async def load_title(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text
    async with state.proxy() as data:
        await message.reply(str(data))

    add_new_catalog = models.Catalogs(path=data['document'], title=data['title'])
    session_connect.add(add_new_catalog)
    session_connect.commit()

    await message.answer(text='каталог добален в базу данных')
    await state.finish()


@dp.callback_query_handler(lambda c: c.data == 'cancel', state='*')
async def cancel_handler(callback_query: types.CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await callback_query.answer('вы вышли из режима загрузки', show_alert=True)
    await callback_query.bot.delete_message(
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id
    )