import logging

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

menu_callback_data = CallbackData('show_menu', 'level')


def _make_callback_data(level):
    return menu_callback_data.new(level=level )


async def first_level_menu():
    CURRENT_LEVEL = 'level_menu'
    markup = InlineKeyboardMarkup(row_width=1)
    callback_data_button_1 = _make_callback_data(level='our_way')
    callback_data_button_2 = _make_callback_data(level='level_catalogs')

    markup.add(InlineKeyboardButton(text='Как нас найти', callback_data=callback_data_button_1))
    markup.add(InlineKeyboardButton(text='Каталоги', callback_data=callback_data_button_2))

    return markup


async def second_level_menu():
    CURRENT_LEVEL = 'level_catalogs'
    markup = InlineKeyboardMarkup(row_width=1)
    callback_data_button_1 = 'Catalog_new_year2'
    callback_data_button_2 = 'Catalog_opors'

    markup.add(InlineKeyboardButton(text='Скачать новогодний каталог ч2', callback_data=callback_data_button_1))
    markup.add(InlineKeyboardButton(text='Скачать каталог опор', callback_data=callback_data_button_2))
    markup.add(
        InlineKeyboardButton(
            text='Назад',
            callback_data=_make_callback_data(level='level_menu')
        )
    )
    return markup


async def our_way():
    CURRENT_LEVEL = 'our_way'
    markup = InlineKeyboardMarkup(row_width=1)
    callback_data_button_2 = 'our_place'

    markup.add(InlineKeyboardButton(text='Наш сайт', url='https://mg-l.ru/'))
    markup.add(InlineKeyboardButton(text='Где мы находимся?', callback_data=callback_data_button_2))
    markup.add(
        InlineKeyboardButton(
            text='Назад',
            callback_data=_make_callback_data(level='level_menu')
        )
    )
    return markup

