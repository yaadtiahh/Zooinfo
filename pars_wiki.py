import wikipedia
from bs4 import BeautifulSoup
import requests
import os
import telebot
from dotenv import load_dotenv


load_dotenv()
tg_bot_token = os.environ.get("TG_BOT_TOKEN")
bot = telebot.TeleBot(tg_bot_token)


def wiki_pars(message):  # парсер википедии на поиск по названию
    global answer
    answer = message.text
    wikipedia.set_lang("ru")
    response = requests.get(f"https://ru.wikipedia.org/wiki/{answer}")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title')
    info = wikipedia.summary(title)
    bot.send_message(message.chat.id, text=info)
    bot.send_message(message.chat.id, text=f"https://ru.wikipedia.org/wiki/{answer}")
