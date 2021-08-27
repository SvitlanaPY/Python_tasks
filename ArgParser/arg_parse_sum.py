import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

# args = parser.parse_args(['--sum', '7', '-1', '42'])
# print(args)

# run ~$ python3 arg_parse_sum.py -h
# Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])


args = parser.parse_args()
print(args.accumulate(args.integers))

# run ~$ python3 arg_parse_sum.py 1 2 3 4
# 4

# run ~$ python3 arg_parse_sum.py 1 2 3 4 --sum
# 10


