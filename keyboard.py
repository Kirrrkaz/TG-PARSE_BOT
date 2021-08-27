from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

button_NEWS = KeyboardButton('news')

NEWS_kb = ReplyKeyboardMarkup(resize_keyboard=True)
NEWS_kb.add(button_NEWS)