import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--one', help='This will be option One')     # optional argument (one -це назва optional змінної; -- означає, що це optional змінна)
parser.add_argument('two', help='This will be option Two')       # positional argument (two -це назва positional змінної)
parser.add_argument('three', help='This will be option Three')   # positional argument (three -це назва positional змінної)

args = parser.parse_args()
print(args)
print(args.one)

# run ~$ python3 arg_parser3.py --one first one two    ==> передаємо значення для optional arguments(--one) i для positional arguments (two, three):
# print(args): OUTPUT: Namespace(one='first', two='one', three='two')
# print(args.one): OUTPUT: first

# $ python3 arg_parser3.py 2two2 3three3   ==> передаємо значення для positional arguments:
# Namespace(one=None, three='3three3', two='2two2')


# опция -h (или --help) НЕ задаётся вручную,
# она обрабатывается модулем «автоматически» (хотя это можно переназначить)
# run ~$ python3 arg_parser3.py -h
# usage: arg_parser3.py [-h] [--one ONE] two three
#
# positional arguments:
#   two         This will be option Two
#   three       This will be option Three
#
# optional arguments:
#   -h, --help  show this help message and exit
#   --one ONE   This will be option One



# Список методов класса можно получить так:
# for i in dir(argparse.ArgumentParser):
#     if not i.startswith('_'):
#         print(i)

# add_argument
# add_argument_group
# add_mutually_exclusive_group
# add_subparsers
# convert_arg_line_to_args
# error
# exit
# format_help
# format_usage
# get_default
# parse_args
# parse_intermixed_args
# parse_known_args
# parse_known_intermixed_args
# print_help
# print_usage
# register
# set_defaults
#
