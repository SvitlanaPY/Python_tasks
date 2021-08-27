# https://rtfm.co.ua/python-modul-argparse-opcii-komandnoj-stroki-v-primerax/#add_argument_-_name_%D0%B8%D0%BB%D0%B8_flags

# Ситаксис add_argument:
# add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
# name или flags — имя опции, например foo или -f, —foo
# action — тип действия, которое будет выполнятся при вызове опции (см. ниже action='store');
# nargs — количество аргументов к опции, которые могут (должны) быть использованы;
# const — константа, может потребовать некоторым типам действий или аргументам;
# default — действие по-умолчанию, если опция пропущена (не вызвана), прмиеняется ко всем опциям, которым не назначен отдельный ключ default;
# type — тип данных, в котором должен быть сохранён объект (данные), переданные аргументом к опции, например — str или int;
# choices — контейнер допустимых значений для аргумента;
# required — указатель, является ли опция обязательной;
# help — краткое описание опции, используется в --help;
# metavar — имя аргумента для опции, которое будет выводится в --help;
# dest — имя опции, которое будет передано методу parse_args().
#
# Тут отдельно надо остановиться на ключе «action«.
#
# Ключ action может принимать такие значения:
#
# 'store' — просто сохраняет в переменной «имя_опции» значение, переданное опции (действие по-умолчанию);
# 'store_const' — сохраняет значение, заданное ключём const;
# 'store_true' или 'store_false' — сохраняет значение True или False;
# 'count' — счётчик количества экземпляров опции.

import argparse

parser = argparse.ArgumentParser()

# add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
# add_argument — NAME или FLAGS
# Опции, задаваемые со знаком «-» будут считаться опциональными,
# тогда как заданные просто в виде "имя" — обязательными.
# parser.add_argument('--one', help='This will be option One')     # optional argument (one -це назва optional змінної; "-" означає, що це optional змінна)
# parser.add_argument('two', help='This will be option Two')       # positional argument (two -це назва positional змінної)

parser.add_argument('-1', '--one', help='This will be option One')

# add_argument — ACTION:
# -- ‘store’ — сохраняет значение, переданное опции (действие по-умолчанию)

args = parser.parse_args()
print(args)
# run ~$ python3 arg_parser_action_1.py -1 first_argument
# Namespace(one='first_argument')

# run ~$ python3 arg_parser_action_1.py --one first_argument
# Namespace(one='first_argument')


