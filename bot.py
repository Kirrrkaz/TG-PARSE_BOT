# -*- coding: utf8 -*-
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
from aiogram import Bot, Dispatcher, executor, types
import requests
import logging
from bs4 import BeautifulSoup as bs


url = "https://www.securitylab.ru/news/"
request = requests.get(url)
soup = bs(request.text, "html.parser")
article_cards = soup.find_all("a", class_="article-card")
'''
for article in article_cards:
    title = article.find_all("h2", class_="article-card-title")
    
    for title in title:
        print(title.text)
'''

for article in article_cards:
    article_title = article.find("h2", class_="article-card-title")
    article_title = str(article_title).split('<h2 class="article-card-title">')[1].split('  </h2>')[0]
    article_desc = article.find("p")
    article_url = f'https://www.securitylab.ru{article.get("href")}'
    #article_date_time = article.find("time")


    #print(f"{article_title} \n {article_url}")

#for title in title:
#print(title.text)



API_TOKEN = '...'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет,напиши /news и я вышлю инфу')

@dp.message_handler()
async def message(message: '/news' ):
    await message.answer(article_title)
    await message.answer(article_url)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
