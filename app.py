import logging
from aiogram.utils import executor

from handlers import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.db_api.models import create_db


logging.basicConfig(level=logging.INFO)

async def on_startup(dp):
    create_db()
    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
