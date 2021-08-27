import argparse

parser = argparse.ArgumentParser(description="Open and read file")

parser.add_argument("--file", help="Please, write the path to the file you want to open")
args = parser.parse_args()
f = open(args.file, 'r')
# x = f.readline()   # read only first line and print first line + empty second line
# print(x)
# run ~$ python3 arg_parser_openFile.py --file text.txt
# hello
#


# x = f.readlines()   # read all lines with but add \n: ['hello\n', 'hi\n', 'how are you?\n', 'bye']
# print(x)
# run ~$ python3 arg_parser_openFile.py --file text.txt


# x = f.read().splitlines()
# print(x)
# run ~$ python3 arg_parser_openFile.py --file text.txt
# ['hello', 'hi', 'how are you?', 'bye']


# x = f.read().splitlines()
# for i in x:
#     print(i)
# run ~$ python3 arg_parser_openFile.py --file text.txt
# hello
# hi
# how are you?
# bye


x = f.readlines()
for i in x:
    print(i)
# run ~$ python3 arg_parser_openFile.py --file text.txt
# hello
#
# hi
#
# how are you?
#
# bye

f.close()