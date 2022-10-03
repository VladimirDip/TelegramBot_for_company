from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

catalog_button = 'Download Catalog'

inline_btn_1 = InlineKeyboardButton('Скачать новогодний каталог ч2', callback_data='Catalog_new_year2')
inline_btn_2 = InlineKeyboardButton('Скачать каталог опор', callback_data='Catalog_opors')

inline_kb1 = InlineKeyboardMarkup(row_width=1)

inline_kb1.add(inline_btn_1).insert(inline_btn_2)

