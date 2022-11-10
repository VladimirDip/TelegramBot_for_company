from aiogram.dispatcher.filters import BoundFilter
from aiogram.types.message import Message

from data.config import admins


class IsAdmin(BoundFilter):

    async def check(self, message: Message) -> bool:
        member = message.from_user.id in admins
        if not member:
            await message.answer('Это только для администраторов!')
        return member


def setup(dp):
    dp.filters_factory.bind(IsAdmin)