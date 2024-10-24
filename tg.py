import os
import random
from telebot import types
import time
from pars_wiki import wiki_pars, bot


BREEDS_DOGS = [
    'Немецкий шпиц',
    'Йоркширский терьер',
    'Чихуахуа',
    'Немецкая овчарка',
    'Лабрадор-ретривер',
    'Хаски',
    'Джек-рассел-терьер',
    'Среднеазиатская овчарка',
    'Кавказская овчарка',
    'Вельш-корги пемброк',
]
BREEDS_CATS = [
    'бурманская кошка',
    'тонкинская кошка',
    'бирманская кошка',
    'норвежская лесная кошка',
    'корниш-рекс',
    'девон-рекс',
    'ориентальная кошка',
    'американская короткошерстная',
    'британская короткошерстная',
    'экзотическая кошка'
]


@bot.message_handler(commands=['start'])  # кнопки поиска
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Поиск по названию🔍")
    btn2 = types.KeyboardButton("Поиск по породе собак🐶")
    btn3 = types.KeyboardButton("Поиск по породе кошек😺")
    markup.add(btn1).row(btn2, btn3)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def animal_search(message):
    if message.text == "Поиск по названию🔍":  # поиск по названию
        bot.send_message(message.chat.id, text="Введите название животного")
        bot.register_next_step_handler(message, wiki_pars)

    elif (message.text == "Поиск по породе собак🐶"):  # поиск по собакам
        bot.send_message(message.chat.id, text="Вот 10 самых популярных пород собак:")
        breeds_dogs_search(message)
        time.sleep(3)
        bot.send_message(message.chat.id, text="Какая вас интересует?")
        # bot.register_next_step_handler(message, breeds_dogs_search)
        # bot.send_message(message.chat.id, text="Введите породу собаки:")

    elif (message.text == "Поиск по породе кошек😺"):  # поиск по кошкам
        bot.register_next_step_handler(message, breeds_cats_search)
        # bot.send_message(message.chat.id, "Введите породу кошки")

    elif (message.text == "Вернуться в главное меню"):
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню")


def breeds_dogs_search(message):
    breeds_dogs = BREEDS_DOGS
    for breed in breeds_dogs:
        bot.send_message(message.chat.id, breed)


def breeds_cats_search(message):
    breeds_cats = BREEDS_CATS
    bot.send_message(message.chat.id, text=breeds_cats)


def send_facts_tg_bot(chat_id, hours):  # рандомный факт в день
    while True:
        with open("facts.txt") as inp:
            lines = inp.readlines()
            random_line = random.choice(lines).strip()
        bot.send_message(chat_id=chat_id, text=random_line)
        time.sleep(int(hours*3600))


if __name__ == "__main__":
    answer = ''
    hours = int(os.environ.get("TG_TIME"))
    chat_id = os.environ.get("TG_CHAT_ID")
    bot.infinity_polling()
