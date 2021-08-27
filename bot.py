from aiogram import Bot, Dispatcher, executor, types
import requests
import logging
from bs4 import BeautifulSoup as bs
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import API_TOKEN 
import keyboard as kb
NEWS = {}

url = "https://www.securitylab.ru/news/"
request = requests.get(url)
soup = bs(request.text, "html.parser")
article_cards = soup.find_all("a", class_="article-card")

for article in article_cards:
    
    article_url = f'https://www.securitylab.ru{article.get("href")}'
    
    NEWS[article_url] = f'https://www.securitylab.ru{article.get("href")}'


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Приветствую, что хотите узнать?", reply_markup=kb.NEWS_kb)

@dp.message_handler()
async def message(message: 'news' ):
    for i in NEWS:
        await message.answer(i)
       

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
