import argparse

parser = argparse.ArgumentParser(prog='lantern')
sub = parser.add_subparsers(dest='command')

add_parser = sub.add_parser('add')
add_parser.add_argument('title')

list_parser = sub.add_parser('list')
list_parser.add_argument('--done', action='store_true', help='show only completed tasks')

args = parser.parse_args()

if args.command == 'add':
    print(f'Added Task: {args.title}')
elif args.command == 'list':
    if args.done:
        print('listing completed tasks')
    else:
        print('listing Tasks')
else:
    parser.print_help()