tasks = []

def add_task(title):
    task = {'title': title.strip(), "done": False}
    return task


def list_tasks():
    return tasks