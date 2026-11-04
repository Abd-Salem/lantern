import argparse
import storage

parser = argparse.ArgumentParser(prog='lantern')
sub = parser.add_subparsers(dest='command')

add_parser = sub.add_parser('add')
add_parser.add_argument('title')

list_parser = sub.add_parser('list')

args = parser.parse_args()

if args.command == 'add':
    print(f'Added Task: {args.title}')
elif args.command == 'list':
    tasks = storage.load()
    if not tasks:
        print('No tasks yet.')
    for task in tasks:
        print(task['title'])
else:
    parser.print_help()