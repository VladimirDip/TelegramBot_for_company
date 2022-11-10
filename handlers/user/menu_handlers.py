from typing import Union
from aiogram import types

from keyboard.user_buttons import first_level_menu, menu_callback_data, \
    second_level_menu, our_way, admin_registration

from utils.db_api.db_commands import WorkWithDb

from create_bot import dp
from data.config import ADMIN_PASSWORD

db = WorkWithDb()


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


async def check_admin(callback: types.CallbackQuery, **kwargs):
    markup = await admin_registration()
    await callback.message.edit_text(f'Что хочешь сделать?', reply_markup=markup)


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

"""It will be late"""
# @dp.callback_query_handler(text='check_admin_for_you')
# async def check_admin_for_you(callback: types.CallbackQuery, **kwargs):
#     admin_exists = db.check_admin(callback.from_user.id)
#     await callback.answer()
#     if admin_exists is False:
#         await callback.message.answer('Ты не являешься Админом!')
#     else:
#         await callback.message.answer('Ты Администратор!')
#
#
# @dp.callback_query_handler(text='authorization')
# async def authorization(callback: types.CallbackQuery, **kwargs):
#     await callback.message.answer('Введите код администратора(только цифры)')
#     db.add_new_admin(callback.from_user.id,
#                      callback.from_user.first_name,
#                      callback.from_user.last_name,
#                      callback.from_user.username)
#     await callback.message.answer('Reg new admin')
#     print(*kwargs)


# @dp.message_handler()
# async def input_admin_password(message: types.Message):
#     if message.text == ADMIN_PASSWORD:
#         return True
#     else:
#         return False


@dp.callback_query_handler(menu_callback_data.filter())
async def navigate(callback: types.CallbackQuery, callback_data: dict):
    current_level = callback_data.get('level')

    levels = {
        'level_menu': show_menu,
        'level_catalogs': menu_catalogs,
        'level_our_way': about_us,
        'level_registration_admin': check_admin,

    }

    current_level_function = levels[current_level]
    await current_level_function(
        callback,
        current_level=current_level
    )
