from aiogram import types, Dispatcher
from config import bot


async def echo(message: types.Message):
    username = f"@{message.from_user.username}" \
        if message.from_user.username is not None else message.from_user.full_name
    bad_words = ['javascript', 'html', 'чорт', 'бля']
    for word in bad_words:
        if word in message.text.lower():
            await bot.delete_message(message.chat.id, message.message_id)
            await message.answer(f"Не матерись @{username}")
            break

    # if message.text.isnumeric():
    #     await bot.send_message(message.from_user.id, int(message.text) ** 2)

    # else:
    #     await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
