from aiogram import types
from aiogram.types import InputFile

from utils.db_api.database import session
from create_bot import dp
from utils.db_api.database import session
from utils.db_api.models import Catalogs
from utils.db_api.db_commands import WorkWithDb

session_connect = session()
db = WorkWithDb()


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    path = db.get_path_catalogs(Catalogs.title, callback_query.data)

    await dp.bot.send_document(chat_id=callback_query.from_user.id, document=path)
    text = f'пожалуйста ваш catalog'

    await callback_query.answer(text=text, show_alert=True,)
