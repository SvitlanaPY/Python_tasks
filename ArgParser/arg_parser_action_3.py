import argparse

parser = argparse.ArgumentParser()

# add_argument — ACTION:
# ‘store_true’ или ‘store_false’ — сохраняет значение True или False
# Похож по действию на store_const, с той разницей что хранит только True или False.

parser = argparse.ArgumentParser()
parser.add_argument('-3', '--three', action='store_true', help='This will be option One')
args = parser.parse_args()
print(args)

# run ~$ python3 arg_parser_action_3.py --three
# Namespace(three=True)

# run ~$ python3 arg_parser_action_3.py
# Namespace(three=False)

# run ~$ python3 arg_parser_action_3.py -3
# Namespace(three=True)

