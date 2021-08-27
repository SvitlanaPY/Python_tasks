
import argparse

parser = argparse.ArgumentParser()
parser2 = argparse.ArgumentParser()

parser2.add_argument('-4', '--four', help='This will be option Four')     # optional argument
parser2.add_argument('five', help='This will be option Five')       # positional argument
parser2.add_argument('six', help='This will be option Six')   # positional argument

args = parser2.parse_args()
print(args)
# print(args.five)   # 5five5

# run ~$ python3 arg_parser4.py -h
# usage: arg_parser4.py [-h] [-4 FOUR] five six
#
# positional arguments:
#   five                  This will be option Five
#   six                   This will be option Six
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -4 FOUR, --four FOUR  This will be option Four


# run ~$ python3 arg_parser4.py -4 4four4 5five5 6six6
# OUTPUT: Namespace(five='5five5', four='4four4', six='6six6')

