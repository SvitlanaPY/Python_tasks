import argparse

parser = argparse.ArgumentParser()

# ‘store_true’ или ‘store_false’ — сохраняет значение True или False
# Похож по действию на store_const, с той разницей что хранит только True или False.

parser.add_argument('-1', '--one', action='store_true', help='This will be option One')

res = parser.parse_args()

if res.one:
    print("First is True!")
else:
    print(" First is nothing :-( ")

# run ~$ python3 arg_parser_action_task2.py
#  First is nothing :-(

# run ~$ python3 arg_parser_action_task2.py --one
# First is True!
