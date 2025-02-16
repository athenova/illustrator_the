import os
import json
import glob

tasks = json.load(open('files/in_progress/tasks.json', 'rt', encoding='UTF-8'))

for i, task in enumerate(tasks):
    folder_name = glob.escape(f"files/in_progress/{task['folder'].replace('/', ',')}/data")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    folder_name = glob.escape(f"{folder_name}/{task['name'].replace('/', ',')}")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)