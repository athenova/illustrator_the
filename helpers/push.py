
from datetime import datetime
from datetime import timedelta
import json
import os
import operator as op
import itertools as it

TOPIC_WORD_LIMIT = 100

tasks_file = 'files/in_progress/tasks.json'

def roundrobin(*iterables):
    sentinel = object()
    return (a for x in it.zip_longest(*iterables, fillvalue=sentinel) 
            for a in x if a != sentinel)

if not os.path.exists(tasks_file):
    tasks = []
    for root, dirs, files in os.walk('files/backlog'):
        for i, folder in enumerate(dirs):
            data_file = f"{root}/{folder}/data.json"
            if os.path.exists(data_file):
                data = json.load(open(data_file, "rt", encoding="UTF-8"))
                text_type = data["text_type"]
                image_type = data["image_type"]
                for subject in data["subjects"]:
                    task = { 
                        "index": i + 1,
                        "name" : subject['name'],
                        "text_prompt": f"Опиши {text_type} '{subject['name']}' из книги '{subject['book']}' автора {subject['author']}, используй не более {TOPIC_WORD_LIMIT} слов, используй смайлики",
                        "image_prompt": f"Нарисуй рисунок, вдохновлённый {image_type} '{subject['name']}' из книги '{subject['book']}' автора {subject['author']}",
                        "folder": folder,
                    }
                    tasks.append(task)
                os.rename(f"files/backlog/{folder}", f"files/in_progress/{folder}")

    x = [list(v) for k, v in it.groupby(tasks, key=op.itemgetter('index'))]
    tasks = list(roundrobin(*x))

    curr_date = datetime.today() + timedelta(days=1)
    for task in tasks:
        task["date"] = curr_date.strftime("%Y-%m-%d")
        curr_date += timedelta(days=1)

    json.dump(tasks, open(tasks_file, 'wt', encoding='UTF-8'), indent=4, ensure_ascii=False)
    print(f"{len(tasks)} tasks created")
else: 
    print("Tasks already exists, revert before push")