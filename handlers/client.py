from config import dp, bot, ADMINS
from aiogram import types, Dispatcher
import random
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from parser.parser_wheel import parser
from database.bot_db import sql_command_random, sql_command_all
from keyboards.clien_kb import direction_markup


async def pin_message(message: types.Message):
    if message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('сообщение должно быть ответом')


async def dice_game(message: types.Message):
    bot_dice = await bot.send_dice(message.chat.id)
    user_dice = await bot.send_dice(message.chat.id)
    await message.answer("первый игральный кость бота а второй игрока")
    if bot_dice.dice.value > user_dice.dice.value:
        await message.answer(f"Бот выиграл {message.from_user.full_name}!")
    elif bot_dice.dice.value == user_dice.dice.value:
        await message.answer("Ничья")
    else:
        await message.answer(f"{message.from_user.full_name} выиграл бота!")


async def game(message: types.Message):
    if message.from_user.id in ADMINS:
        data = ['⚽', '🏀', '🎯', '🎰', '🎳', '🎲']
        r = random.choice(data)
        await bot.send_dice(message.chat.id, emoji=r)
    else:
        await bot.send_message(message.chat.id, 'Ты не админ')


async def start_command(message: types.Message):
    await message.answer(f"Добро пожаловать {message.from_user.username}\n"
                         f"Хочешь мемы нажми /mem\n"
                         f"Хочешь викторину нажми /quiz\n"
                         f"Хочешь послушать музыку нажми /music\n"
                         f"Хочешь возвести какое-то число в квадрат, просто напиши это число\n"
                         f"Мини-игра только для админов/game\n"
                         f"Хочешь покидать кости с ботом нажми /dice")


async def music(message: types.Message):
    audios = (
        'media/AUD-20220103-WA0018.mp3',
        'media/Bakr - Эталон Красоты.mp3',
        'media/mende kanday kyne bar_ speed up.mp3',
        'media/Sharara sharara rmx_️.mp3',
        'media/Xcho_Eskizy.mp3',
        'media/Xcho_Malaya.mp3',
        'media/Дама босиком на берегу .mp3',
        'media/Мурашки - V X V PRiNCE.mp3',
    )
    audio = open(random.choice(audios), 'rb')
    await bot.send_audio(message.from_user.id, audio=audio)


async def mem(message: types.Message):
    photos = (
        'media/mem1.jpg',
        'media/mem2.jpg',
        'media/mem3.jpg',
        'media/mem4.jpg',
        'media/mem5.jpg',
        'media/mem6.jpg',
    )
    photo = open(random.choice(photos), 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


async def quiz1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call1 = InlineKeyboardButton("Дальше", callback_data='button_call1')
    markup.add(button_call1)
    question = "Как зовут супермена?"
    answers = [
        "Владимир",
        "Брюс Вейн",
        "Калэл",
        "Чак Норис"]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        open_period=10,
        reply_markup=markup)


async def get_random_user(message: types.Message):
    # await message.answer("Какое направление?", reply_markup=direction_markup)
    await sql_command_random(message)


async def parsser_wheels(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,

            f"{item['link']}"
            f"{item['logo']}\n"
            f"# {item['size']}\n"
            f"цена - {item['price']}\n"
            )



async def get_all_mentor(message: types.Message):
    await sql_command_all()


def register_client_handler(dp: Dispatcher):
    dp.register_message_handler(quiz1, commands=["quiz"])
    dp.register_message_handler(mem, commands=["mem"])
    dp.register_message_handler(music, commands=["music"])
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(pin_message, commands=["pin"], commands_prefix='!')
    dp.register_message_handler(game, commands=["game"])
    dp.register_message_handler(dice_game, commands=["dice"])
    dp.register_message_handler(get_random_user, commands=["getmentor"])
    dp.register_message_handler(get_all_mentor, commands=["allmentor"])
    dp.register_message_handler(parsser_wheels, commands=["wheel"])
