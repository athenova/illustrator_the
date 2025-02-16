
from datetime import datetime
import json
import os

tasks_file = 'files/in_progress/tasks.json'

if os.path.exists(tasks_file):
    tasks = json.load(open(tasks_file, "rt", encoding="UTF-8"))
    for task in tasks:
        if task["date"] > datetime.today().strftime("%Y-%m-%d"):
            folder = task["folder"]
            src = f"files/in_progress/{folder}"
            dst = f"files/backlog/{folder}"
            if os.path.exists(src):
                os.rename(src, dst)
    os.remove(tasks_file)
    print("Tasks reverted")
else:
    print("Nothing to revert")