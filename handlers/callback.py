from config import bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def quiz2(call: types.callback_query):
    markup = InlineKeyboardMarkup()
    button_call2 = InlineKeyboardButton("Дальше", callback_data='button_call2')
    markup.add(button_call2)
    question = "В каком году родился Манас?"
    answers = [
        "1900",
        "1890",
        "1906",
        "2020"]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=10,
        reply_markup=markup)


async def quiz3(call: types.callback_query):
    question = "В каком году распался СССР?"
    answers = [
        "1900",
        "1991",
        "1897",
        "2000"]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        open_period=10
    )


def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2, lambda call: call.data == 'button_call1')
    dp.register_callback_query_handler(quiz3, lambda call: call.data == 'button_call2')
