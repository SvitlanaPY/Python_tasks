import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--aa", default="hello world!", help="This is the 'aa' variable")

args = parser.parse_args()
print(args)   # Namespace(a='hello world!')

# a = args.aa
# print(a)   # hello world!
#
# print(args.aa)   # hello world!


# run ~$ python3 arg_parse_variable.py -h
# usage: arg_parse_variable.py [-h] [--aa A]
# A tutorial of argparse!
# optional arguments:
#   -h, --help  show this help message and exit
#   --aa A       This is the 'aa' variable

# run ~$ python3 arg_parse_variable.py
# Namespace(a='hello world!')

# run ~$ python3 arg_parse_variable.py --aa 11111111
# Namespace(aa='11111111')
