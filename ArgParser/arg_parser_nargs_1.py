import argparse
parser = argparse.ArgumentParser()
# add_argument — NARGS

# Ключ nargs поддерживает такие значения:
# N — количество аргументов к опции;
# ? — если присутствует один аргумент — он будет сохранён, иначе — будет использовано значение из ключа default; При вызове без аргумента — значение переменной будет задано как None;
# * — все переданные аргументы будут сохранены в один список;
# + — то же, что и * — но если нет хотя бы одного аргумента — будет выдано сообщение об ошибке;


# nargs с «N» аргументов:
# N — количество аргументов к опции;
# parser.add_argument('-1', '--one', nargs=2, help='This will be option One')
# args = parser.parse_args()
# print(args)
# run ~$ python3 arg_parser_nargs_1.py --one a b
# Namespace(one=['a', 'b'])


# nargs с «?» аргументов:
# ? — если присутствует один аргумент — он будет сохранён, иначе — будет использовано значение из ключа default; При вызове без аргумента — значение переменной будет задано как None;
# parser.add_argument('-11', '--one', nargs='?', const='const-one', default='default-one', help='This will be option One')
# parser.add_argument('-22', '--two', nargs='?', const='const-two', default='default-two', help='This will be option Two')

# res = parser.parse_args()
# print(res)

# run ~$ python3 arg_parser_nargs_1.py -11 FIRSTTT -22
# Namespace(one='FIRSTTT', two='const-two')

# run ~$ python3 arg_parser_nargs_1.py -11 FIRSTTT -22 SECONDD
# Namespace(one='FIRSTTT', two='SECONDD')


# nargs с «*» аргументов:
# * — все переданные аргументы будут сохранены в один список;
# parser.add_argument('-4', '--four', nargs='*', help='This will be option FOUR')
# res = parser.parse_args()
# print(res)

# run ~$ python3 arg_parser_nargs_1.py -4
# Namespace(four=[])

# run ~$ python3 arg_parser_nargs_1.py -4 test1 test2 test3 test4 test5 test6
# Namespace(four=['test1', 'test2', 'test3', 'test4', 'test5', 'test6'])

# parser.add_argument('-5', '--five', nargs='*', help='This will be option FIVE')
# res = parser.parse_args()
# print(res)
# for i in res.five:
#     print(i)

#run ~$ python3 arg_parser_nargs_1.py -5 test1 test2 test3 test4 test5 test6
# Namespace(five=['test1', 'test2', 'test3', 'test4', 'test5', 'test6'])
# test1
# test2
# test3
# test4
# test5
# test6


# nargs с «+» аргументов:
# + — то же, что и * — но если нет хотя бы одного аргумента — будет выдано сообщение об ошибке;
parser.add_argument('-6', '--six', nargs='+', help='This will be option SIX')
res = parser.parse_args()
print(res)

# run ~$ python3 arg_parser_nargs_1.py -6 test1 test2 test3 test4 test5 test6
# Namespace(six=['test1', 'test2', 'test3', 'test4', 'test5', 'test6'])

# run ~$ python3 arg_parser_nargs_1.py -6
# usage: arg_parser_nargs_1.py [-h] [-6 SIX [SIX ...]]
# arg_parser_nargs_1.py: error: argument -6/--six: expected at least one argument
