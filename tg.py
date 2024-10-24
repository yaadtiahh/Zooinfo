from telebot import types

from pars_wiki import wiki_pars
from config import bot


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


@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Поиск по названию🔍")
    btn2 = types.KeyboardButton("Поиск по породе собак🐶")
    btn3 = types.KeyboardButton("Поиск по породе кошек😺")
    markup.add(btn1).row(btn2, btn3)
    bot.send_message(
        message.chat.id,
        "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user),
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def animal_search(message):
    if message.text == "Поиск по названию🔍":  # поиск по названию
        bot.send_message(message.chat.id, text="Введите название животного")
        bot.register_next_step_handler(message, wiki_pars)

    elif message.text == "Поиск по породе собак🐶":  # поиск по собакам
        bot.send_message(message.chat.id, text="Вот 10 самых популярных пород собак:")

        for breed in BREEDS_DOGS:
            bot.send_message(message.chat.id, breed)

        bot.send_message(message.chat.id, text="Какая вас интересует?")
        bot.register_next_step_handler(message, process_breed_dog_selection)

    elif message.text == "Поиск по породе кошек😺":
        bot.send_message(message.chat.id, text="Вот 10 самых популярных пород кошек:")

        for breed in BREEDS_CATS:
            bot.send_message(message.chat.id, breed)

        bot.send_message(message.chat.id, text="Какая вас интересует?")
        bot.register_next_step_handler(message, process_breed_cat_selection)

    else:
        bot.send_message(message.chat.id, text="На такое я не запрограммирован :(")


def process_breed_dog_selection(message):
    if message.text in BREEDS_DOGS:
        wiki_pars(message)
    else:
        bot.send_message(message.chat.id, text="Эта порода не найдена. Попробуйте снова.")
        bot.register_next_step_handler(message, process_breed_dog_selection)


def process_breed_cat_selection(message):
    if message.text in BREEDS_CATS:
        wiki_pars(message)
    else:
        bot.send_message(message.chat.id, text="Эта порода не найдена. Попробуйте снова.")
        bot.register_next_step_handler(message, process_breed_cat_selection)


if __name__ == "__main__":
    bot.infinity_polling()
