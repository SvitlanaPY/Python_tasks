import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--input', action='store', type=int, required=True)
my_parser.add_argument('--id', action='store', type=int)

args = my_parser.parse_args()
print(args)
# run ~$ python3 arg_parse_id.py
# usage: arg_parse_id.py [-h] --input INPUT [--id ID]
# arg_parse_id.py: error: the following arguments are required: --input


# run ~$ python3 arg_parse_id.py --input 101
# Namespace(id=None, input=101)


# run ~$ python3 arg_parse_id.py --input 101 --id 101010
# OUTPUT: Namespace(id=101010, input=101)


# run ~$ python3 arg_parse_id.py -h
# usage: arg_parse_id.py [-h] --input INPUT [--id ID]
# optional arguments:
#   -h, --help     show this help message and exit
#   --input INPUT
#   --id ID

