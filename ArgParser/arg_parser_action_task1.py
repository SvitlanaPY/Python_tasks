import argparse

parser = argparse.ArgumentParser()

# ‘store_const’ — сохраняет значение, заданное ключём const;
# Удобно использовать для передачи различных флагов.

parser.add_argument('--one', action='store_const', const='1', help='This will be option One')
args = parser.parse_args()
print(args)

# if parser.parse_args().one == '1':
if args.one == '1':
    print("That's it!")
else:
    print("Here is nothing :-(")

# run ~$ python3 arg_parser_action_task1.py --one
# Namespace(one='1')
# That's it!

# run ~$ python3 arg_parser_action_task1.py
# Namespace(one=None)
# Here is nothing :-(
