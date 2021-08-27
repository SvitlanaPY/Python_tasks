import argparse

parser = argparse.ArgumentParser(description="Open and read file")

parser.add_argument("--file", help="Please, write the path to the file you want to open")
parser.add_argument("--write", help="You can write something into the file")

args = parser.parse_args()

if args.write:
    f = open(args.file, 'a+')
    f.write(('\n' + args.write))
else:
    f = open(args.file, 'r')
    x = f.read().splitlines()
    print(x)

# run ~$ python3 arg_parser_writeFile.py --file text.txt --write lol
# run ~$ python3 arg_parser_writeFile.py --file text.txt
# ['hello', 'hi', 'how are you?', 'bye', 'lol']


f.close()