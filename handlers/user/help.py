from aiogram import types
from create_bot import dp as Dispatcher
from create_bot import bot


async def start_command(message: types.Message):
    print(message)
    await bot.send_message(message.chat.id, 'answer of bot')


async def echo_send(message: types.Message):
    # await message.reply(message.text)
    print(message)
    await bot.send_message(chat_id=message.chat.id, text=message.text, )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(callback=start_command, commands=['start'],)
    dp.register_message_handler(echo_send)

