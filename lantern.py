import argparse
import storage

parser = argparse.ArgumentParser(prog='lantern')
sub = parser.add_subparsers(dest='command')

add_parser = sub.add_parser('add')
add_parser.add_argument('title')

list_parser = sub.add_parser('list')
list_parser.add_argument('--sort', action='store_true', help='sort tasks by title')

args = parser.parse_args()

if args.command == 'add':
    print(f'Added Task: {args.title}')
elif args.command == 'list':
    tasks = storage.load()
    if args.sort:
        tasks = sorted(tasks, key=lambda t: t['title'].lower())
    if not tasks:
        print('No tasks yet.')
    for task in tasks:
        print(task['title'])
else:
    parser.print_help()
