import argparse

parser = argparse.ArgumentParser()

# add_argument — ACTION:
# -- ‘store_const’ — сохраняет значение, заданное ключём const;

parser = argparse.ArgumentParser()
parser.add_argument('-2', '--two', action='store_const', const='2', help='This will be option Two')
args = parser.parse_args()
print(args)

# run ~$ python3 arg_parser_action_2.py --two
# Namespace(two='2')

