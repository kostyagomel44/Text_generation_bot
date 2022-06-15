from aiogram.types import InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton



button_h1 = KeyboardButton('Добро')
button_h2 = KeyboardButton('Зло')
greet_kb = ReplyKeyboardMarkup()


# greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_h2, button_h3, button_h4)
greet_kb11 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_h1, button_h2)

