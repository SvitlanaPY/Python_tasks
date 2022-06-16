# ()
# print("Здравствуй,", input())
#
# ()
# surname = input()
# name = input()
# text = "Новый зарегистрированный пользователь:"
# print(text, name, surname)
#
# ()
# day = input()
# month = input()
# year = input()
# info = "Дата рождения пользователя:"
# print(info, year, "-", month, "-", day)
#
# ()
# word = input()
# print(word, "действительно есть в нашем словаре!")
#
# ()
# author = input("Введіть автора: ")
# book = input("Введіть назву книги: ")
# print(author, "- автор бестселлера %s" % book, "- выпустил новую книгу! Спешите приобрести ее в магазине Питонист!")
#
# ()
# 11 22 33
# a, b, c = map(int, input().split())
# print(a, b, c)   # 11 22 33
#
# ()
# sep - спрацює, лише коли є більше одного значення в print: print(1, 2, 3, sep=', ')
# print(1, 2, 3, sep=', ')   # 1, 2, 3
# print(4, 5, sep="???", end=" !!! ")
# print(6, 7)
# 1, 2, 3
# 4???5 !!! 6 7
# sep - НЕ спрацює, коли є лише одне значення в print-і: print(1 sep=', ')
# ()
# 111 222 333
# a, b, c = input('Enter a b c: ').split()
# print(a, b, c)   # 111 222 333
#
# ()
# 111 222 333
# A = input('Enter a b c : ').split()
# print(A)   # ['111', '222', '333']

# print(#'hkhkjjhkhkjh')   # SyntaxError: unexpected EOF while parsing

# print('#hkhkjjhkhkjh')   # #hkhkjjhkhkjh

s = """hello
world
hi
Earth!"""
# 'hello\nworld\nhi\nEarth!'
# print(s)
# hello
# world
# hi
# Earth!

# m = 'hello\nworld\nhi\nEarth!'
# print(m)
# hello
# world
# hi
# Earth!

l = 'hi\nworld'
print(len(l))   # 8 (symbol \n is counted as one symbol, although it contains two signs)

a = '  /~~~\ '
b = " //^ ^\\"
c = "(/(_*_)\)"
d = "_/''*''\_"
e = "(/_)^(_\)"
print(a, b, c, d, e, sep='\n'
