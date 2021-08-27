import argparse
import argparse

parser = argparse.ArgumentParser(description='A tutorial of argparse!')

parser.add_argument('-1', '--one', choices=['1', 'two', '3'], help='This will be option One')
args = parser.parse_args()
print(args)

# аргумент к опции должен быть только из предложенного списка:
# run ~$ python3 arg_parse_choises_2.py -1 two
# Namespace(one='two')


# усли аргумент к опции не из предложенного списка, тогда будет error:
# run ~$ python3 arg_parse_choises_2.py -1 2
# usage: arg_parse_choises_2.py [-h] [-1 {1,two,3}]
# arg_parse_choises_2.py: error: argument -1/--one: invalid choice: '2' (choose from '1', 'two', '3')

# run ~$ python3 arg_parse_choises_2.py -1
# usage: arg_parse_choises_2.py [-h] [-1 {1,2,3}]
# arg_parse_choises_2.py: error: argument -1/--one: expected one argument

