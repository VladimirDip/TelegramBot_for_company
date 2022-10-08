from aiogram import types
from aiogram.types import InputFile


from create_bot import dp


async def _download_catalogs(path_or_bytesio=None, chat_id=None):
    document_path = InputFile(path_or_bytesio=path_or_bytesio)
    await dp.bot.send_document(chat_id=chat_id, document=document_path)


@dp.callback_query_handler(lambda c: c.data)
async def process_callback_button1(callback_query: types.CallbackQuery):
    match callback_query.data:
        case 'Catalog_new_year2':
            await _download_catalogs(path_or_bytesio='files/Новогодний каталог ч.2.pdf',
                                     chat_id=callback_query.from_user.id)
            text = 'пожалуйста ваш новогодний каталог'

        case 'Catalog_opors':
            await _download_catalogs(path_or_bytesio='files/Каталог Опор.pdf',
                                     chat_id=callback_query.from_user.id)
            text = 'пожалуйста ваш каталог опор'

        case _:
            await callback_query.answer()

    print(callback_query.id)
    await callback_query.answer(text=text, show_alert=True,)
