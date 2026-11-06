import csv
import sys


def export_csv(tasks, out=sys.stdout):
    writer = csv.writer(out)
    writer.writerow(['title', 'done'])
    for task in tasks:
        writer.writerow([task['title'], task.get('done', False)])