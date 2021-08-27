import sys
#
# args = sys.argv
# # argv - Метод argv возвращает аргументы командной строки, переданные скрипту Python, в виде списка.
# Важно отметить, что первый аргумент (с индексом 0) в списке — это название самого скрипта.
# Остальные представлены в виде последовательности.
#
# print(args[0])    # sys_1.py
# print(args[1])    # hello
# print(sys.argv)   # ['sys_1.py', 'hello', 'bye', 'hi']

# run in Terminal:
# svitlana@svitlana-HP-ProBook-455-G1:~/Projects/HWs/ArgumentParser$ python3 sys_1.py hello bye hi
# sys_1.py
# hello
# ['sys_1.py', 'hello', 'bye', 'hi']


print("Привет {}. Добро пожаловать в руководство по  {} на {}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
# ~$ python3 sys_1.py Svitlana sys Python
# Привет Svitlana. Добро пожаловать в руководство по  sys на Python