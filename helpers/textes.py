import os
import json
import glob

from datetime import date
from datetime import timedelta
from openai import OpenAI

AI_TEXT_MODEL = 'chatgpt-4o-latest'

check_date = date.today() + timedelta(days=1)

tasks = json.load(open('files/in_progress/tasks.json', 'rt', encoding='UTF-8'))

def gen(count):
    for i, task in enumerate(tasks):
        if i < count:
            folder_name = glob.escape(f"files/in_progress/{task['folder'].replace('/', ',')}/data")
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            folder_name = glob.escape(f"{folder_name}/{task['name'].replace('/', ',')}")
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            text_file_name = f"{folder_name}/text.txt"

            if not os.path.exists(text_file_name):
                client = OpenAI()
                text_prompt = task["text_prompt"]
                text = client.chat.completions.create(
                            model=AI_TEXT_MODEL,
                            messages=[
                                { "role": "system", "content": f"Ты - книгоман" },
                                { "role": "user", "content": text_prompt },
                            ]
                        ).choices[0].message.content
                open(text_file_name, 'wt', encoding="UTF-8").write(text)

gen(10)