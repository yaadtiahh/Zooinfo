import schedule
import time
import random
from bot.config import bot, tg_chat_id


def send_message():
    with open("facts.txt") as inp:
        lines = inp.readlines()
        random_line = random.choice(lines).strip()
    bot.send_message(tg_chat_id, random_line)


schedule.every().day.at("15:00").do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)
