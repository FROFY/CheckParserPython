from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button_get = KeyboardButton('Получить из базы')

keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(button_get)

