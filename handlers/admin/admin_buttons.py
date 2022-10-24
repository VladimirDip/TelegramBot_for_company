from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_button_cancel = InlineKeyboardButton('Отмена операции', callback_data='cancel')

inline_button_1 = InlineKeyboardMarkup().add(inline_button_cancel)


