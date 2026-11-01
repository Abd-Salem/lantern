import argparse

parser = argparse.ArgumentParser(prog='lantern')
sub = parser.add_subparsers(dest='command')

add_parser = sub.add_parser('add')
add_parser.add_argument('title')