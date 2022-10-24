from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from utils.db_api.database import session
from utils.db_api.models import Catalogs
session_connector = session()

menu_callback_data = CallbackData('show_menu', 'level')


def _make_callback_data(level):
    return menu_callback_data.new(level=level )


async def first_level_menu():
    CURRENT_LEVEL = 'level_menu'
    markup = InlineKeyboardMarkup(row_width=1)
    callback_data_button_1 = _make_callback_data(level='level_our_way')
    callback_data_button_2 = _make_callback_data(level='level_catalogs')

    markup.add(InlineKeyboardButton(text='Как нас найти', callback_data=callback_data_button_1))
    markup.add(InlineKeyboardButton(text='Каталоги', callback_data=callback_data_button_2))

    return markup


async def second_level_menu():
    CURRENT_LEVEL = 'level_catalogs'
    markup = InlineKeyboardMarkup(row_width=1)
    for catalog in session_connector.query(Catalogs.path, Catalogs.title).all():
        markup.add(InlineKeyboardButton(text=f'Скачать {catalog.title}', callback_data=catalog.title))
    markup.add(
        InlineKeyboardButton(
            text='Назад',
            callback_data=_make_callback_data(level='level_menu')
        )
    )
    return markup


async def our_way():
    CURRENT_LEVEL = 'level_our_way'
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

