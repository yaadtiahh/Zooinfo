import requests
from bs4 import BeautifulSoup
import wikipedia
from config import bot


def wiki_pars(message):
    global answer
    answer = message.text
    wikipedia.set_lang("ru")
    response = requests.get(f"https://ru.wikipedia.org/wiki/{answer}")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title')
    info = wikipedia.summary(title)
    bot.send_message(message.chat.id, text=info)
    bot.send_message(message.chat.id, text=f"Ссылка на статью: https://ru.wikipedia.org/wiki/{answer}")
