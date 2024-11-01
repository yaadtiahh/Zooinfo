import requests
from bs4 import BeautifulSoup
import wikipedia
from config import bot


def wiki_pars_tg(message):
    global answer
    answer = message.text.replace(' ', '_')
    wikipedia.set_lang("ru")

    try:
        response_text = requests.get(f"https://ru.wikipedia.org/wiki/{answer}?redirect=no")
        response_text.raise_for_status()

        response_photo = requests.get(f"https://ru.wikipedia.org/wiki/{answer}")
        response_photo.raise_for_status()

        soup_text = BeautifulSoup(response_text.text, 'html.parser')
        soup_photo = BeautifulSoup(response_photo.text, 'html.parser')

        text = soup_text.find('title')
        photo = soup_photo.find('img')["src"][2:]

        if not photo:
            raise ValueError("Изображение не найдено")
        info = wikipedia.summary(text, 4)
        article_url = f"https://ru.wikipedia.org/wiki/{answer}"

        results_of_search = {
            'photo': photo,
            'info': info,
        }

        bot.send_photo(message.chat.id, photo=results_of_search["photo"], caption=results_of_search["info"])
        bot.send_message(message.chat.id, text=f"Ссылка на статью:{article_url}")

    except:
        bot.send_message(message.chat.id, text=f'По запросу "{answer}" ничего не найдено :(')
        bot.send_message(message.chat.id, text="Пожалуйста, проверьте правильность запроса.")
