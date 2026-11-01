tasks = []

def add_task(title):
    task = {'title': title}
    tasks.append(task)
    return task


def list_tasks():
    return tasks