from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

direction_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

direction_back = KeyboardButton("BackEnd")
direction_front = KeyboardButton("FrontEnd")
direction_uxui = KeyboardButton("UX UI")
direction_android = KeyboardButton("Android")
direction_ios = KeyboardButton("IOS")

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)
submit_markup1 = KeyboardButton("ДА")
submit_markup2 = KeyboardButton("НЕТ")

cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(KeyboardButton('CANCEL'))
direction_markup.add(direction_back, direction_front, direction_android).add(direction_uxui, direction_ios).add(
    cancel_markup)
submit_markup.add(submit_markup1, submit_markup2)
