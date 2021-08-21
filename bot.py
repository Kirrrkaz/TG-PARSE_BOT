from aiogram import Bot, Dispatcher, executor, types
import requests
import logging
from bs4 import BeautifulSoup as bs

NEWS = {}

url = "https://www.securitylab.ru/news/"
request = requests.get(url)
soup = bs(request.text, "html.parser")
article_cards = soup.find_all("a", class_="article-card")

for article in article_cards:
    
    article_url = f'https://www.securitylab.ru{article.get("href")}'
    
    NEWS[article_url] = f'https://www.securitylab.ru{article.get("href")}'


API_TOKEN = '1930176020:AAEhndgdSgm9SSUiwpg_NAlCgJoy-2EK3Bk'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет,напиши /news и я вышлю инфу')

@dp.message_handler()
async def message(message: '/news' ):
    for i in NEWS:
        await message.answer(i)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
