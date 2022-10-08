import logging
from typing import Union
from aiogram import types

from keyboard.user_buttons import first_level_menu, menu_callback_data, second_level_menu, our_way

from create_bot import dp
logging.basicConfig(level=logging.INFO)


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await show_menu(message)


async def show_menu(message: Union[types.Message, types.CallbackQuery], **kwargs):
    markup = await first_level_menu()
    text = 'Добро пожаловать к боту Proffi Trade\nВыберите необходимое меню...'

    if isinstance(message, types.Message):
        await message.answer(text=text, reply_markup=markup)

    elif isinstance(message, types.CallbackQuery):
        call = message
        if call.data == 'show_menu:level_menu':
            await call.message.edit_text(text=text)
        await call.message.edit_reply_markup(markup)


async def menu_catalogs(callback: types.CallbackQuery, **kwargs):
    markup = await second_level_menu()
    await callback.message.edit_text(f'Привет, {callback.from_user.id} {callback.from_user.full_name}!\n'
                                     f'Жми "Скачать каталог"', reply_markup=markup)


async def about_us(callback: types.CallbackQuery, **kwargs):
    markup = await our_way()
    await callback.message.edit_text(f'Что хочешь узнать?', reply_markup=markup)


@dp.callback_query_handler(text='our_place')
async def working_place(callback: types.CallbackQuery, **kwargs):
    markup = await our_way()
    text = 'Мы находимся:\n' \
           ' г. Владивосток, ул. Командорская 11\n' \
           'Вход с торца здания.\n' \
           'Режим работы пн-пт 09:00-20:00\n' \
           'Рады видеть в гости!'

    markup.inline_keyboard.pop(1)

    await callback.message.edit_text(text=text, reply_markup=markup)


@dp.callback_query_handler(menu_callback_data.filter())
async def navigate(callback: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')

    levels = {
        'level_menu': show_menu,
        'level_catalogs': menu_catalogs,
        'our_way': about_us
    }

    current_level_function = levels[current_level]
    await current_level_function(
        callback,
        current_level=current_level
    )
