import requests
from bs4 import BeautifulSoup
import wikipedia
from bot.config import bot


def wiki_pars(message):
    global answer
    answer = message.text.replace(' ', '_')
    wikipedia.set_lang("ru")
    response_text = requests.get(f"https://ru.wikipedia.org/wiki/{answer}?redirect=no")
    response_text.raise_for_status()
    response_photo = requests.get(f"https://ru.wikipedia.org/wiki/{answer}")
    response_photo.raise_for_status()
    soup_text = BeautifulSoup(response_text.text, 'html.parser')
    soup_photo = BeautifulSoup(response_photo.text, 'html.parser')
    text = soup_text.find('title')
    photo = soup_photo.find('img')
    info = wikipedia.summary(text, 4)
    bot.send_photo(message.chat.id, photo=photo["src"][2:], caption=info)
    bot.send_message(message.chat.id, text=f"Ссылка на статью: https://ru.wikipedia.org/wiki/{answer}")
