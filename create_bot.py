from aiogram import Bot
from aiogram.dispatcher import Dispatcher


from data import config

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher(bot)