from aiogram import types, Dispatcher
from data.config import admins


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands(
        [
            types.BotCommand('/start', 'Запустить бота'),
            types.BotCommand('/upload', 'Загрузить каталоги')
        ]
    )
