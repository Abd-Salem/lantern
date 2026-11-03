tasks = []

def add_task(title):
    task = {'title': title, "done": False}
    tasks.append(task)
    return task


def list_tasks():
    return tasks