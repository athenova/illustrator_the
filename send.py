import os
import telebot
import json
import glob

from datetime import date

BOT_TOKEN_NAME = "ATHE_BOT_TOKEN"
BOT_TOKEN = os.environ.get(BOT_TOKEN_NAME)
CHAT_ID = '@illustrator_the'

check_date = date.today()

tasks = json.load(open('files/in_progress/tasks.json', 'rt', encoding='UTF-8'))

for i, task in enumerate(tasks):
    if task["date"] == check_date.strftime('%Y-%m-%d'):
        folder_name = glob.escape(f"files/in_progress/{task['folder'].replace('/', ',')}/data/{task['name'].replace('/', ',')}")
        text_file_name = f"{folder_name}/text.txt"
        image_file_name = f"{folder_name}/image.png"

        bot = telebot.TeleBot(BOT_TOKEN)
        if os.path.exists(text_file_name) and os.path.exists(image_file_name):
            bot.send_photo(chat_id=CHAT_ID, photo=open(image_file_name, 'rb'), disable_notification=True)
            bot.send_message(chat_id=CHAT_ID, text=open(text_file_name, 'rt', encoding='UTF-8').read(), parse_mode="Markdown")
