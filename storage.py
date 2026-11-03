import json
import os

FILE = "tasks.json"


def load():
    """Return the saved tasks, or an empty list if there is no file yet."""
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)


def save(tasks):
    """Write all tasks to tasks.json."""
    with open(FILE, "w") as f:
        json.dump(tasks, f, sort_keys=True)
