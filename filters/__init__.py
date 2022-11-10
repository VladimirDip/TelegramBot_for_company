from aiogram import Dispatcher

from .filters import IsAdmin


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)