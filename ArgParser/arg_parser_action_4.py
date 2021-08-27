import argparse

parser = argparse.ArgumentParser()

# add_argument — ACTION:
# ‘count’ — счётчик количества экземпляров опции

parser = argparse.ArgumentParser()
parser.add_argument('--one', action='count', help='This will be option One')

args = parser.parse_args()
print(args)

# run ~$ python3 arg_parser_action_4.py -1111111
# Namespace(one=7)
