from aiogram.utils import executor
from create_bot import dp

from handlers import help
from utils.notify_admins import on_startup_notify

help.register_handlers_client(dp)


async def on_startup(dp):
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
