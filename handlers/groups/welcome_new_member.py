from aiogram import types

from create_bot import dp, bot


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def welcome_message(message: types.Message):
    members = ', '.join([mess.get_mention(as_html=True) for mess in message.new_chat_members])
    bot_obj = await bot.get_me()
    await message.reply(f'Привет {members}!\n'
                        f'Напиши боту для скачивания каталогов {bot_obj.id}')