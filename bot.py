from aiogram import Bot, Dispatcher, executor, types
import requests
import logging
from bs4 import BeautifulSoup as bs


url = "https://www.securitylab.ru/news/"
request = requests.get(url)
soup = bs(request.text, "html.parser")
content = soup.find_all("div", class_="article-card-details")

for content in content:
    print(content.text)


API_TOKEN = '...'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Привет, пришли мне ссылку на ресурс')

@dp.message_handler()
async def message(message: 'https://www.securitylab.ru/news/' ):
    await message.answer(content.text)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
