import requests
from bs4 import BeautifulSoup
import wikipedia


def wiki_pars_web(animal):
    wikipedia.set_lang("ru")
    try:
        response_text = requests.get(f"https://ru.wikipedia.org/wiki/{animal}?redirect=no")
        response_text.raise_for_status()

        response_photo = requests.get(f"https://ru.wikipedia.org/wiki/{animal}")
        response_photo.raise_for_status()

        soup_text = BeautifulSoup(response_text.text, 'html.parser')
        soup_photo = BeautifulSoup(response_photo.text, 'html.parser')

        text = soup_text.find('title').text
        photo = soup_photo.find('img')

        if not photo:
            raise ValueError("Изображение не найдено")
        img_url = "https://" + photo["src"][2:]
        info = wikipedia.summary(text)
        article_url = f'https://ru.wikipedia.org/wiki/{animal}'

        results_of_search = {
            'img_url': img_url,
            'info': info,
            'article_url': article_url

        }
        return results_of_search

    except (requests.RequestException, wikipedia.exceptions.PageError, ValueError) as e:
        return f'По запросу "{animal}" ничего не найдено :('
