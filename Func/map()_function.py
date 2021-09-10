# map(function, iterable1, iterable2, ...)  ---> map object
# Ф-ія map() приймає ф-ію, а потім довільну к-ість ітерабельних послідовностей
# (списки, кортежі, словники, ф-ія range, строки...):
# і повертає mab-object, який є ітератором,
# який обчислює результат роботи переданої ф-ії на кожен елемент/аргумент із переданої послідовності
a = [-1, 2, -3, 4, 5]
b = map(abs, a)
print(b)    # <map object at 0x7f7be0b6fe20>

# оскільки map object - це є ітератор, а ітератор являє собою таку колекцію,
# яку можна ітерувати (елементи якої можна обходити в циклі фор) а також використовувати ф-ії, які
# діють над колекціями: max, min, sum ..., а також ітератори можна перетворювати в інші типи/колекції:
# list, tuple, dict;
# отже, щоб побачити результат роботи map(), потрібно обернути ф-ію map() у ф-ію list():
b = list(map(abs, a))
print(b)   # [1, 2, 3, 4, 5]
# до кожного елементу списку "a" застосувалась вбудована ф-ія abs()

# ВСЕ, що написано за допомогою ф-ії map(), можна написати за допомогою comprehensions:
b = [abs(i) for i in a]


print()
# в якості першого аргументу у ф-ію map() можна передавати:
# №1: вбудовані ф-ії:
a = [-1, 2, -3, 4, 5]
b = list(map(abs, a))
print("№1.1", b)
# №1.1 [1, 2, 3, 4, 5]

c = ['hello', 'hi', 'good morning']
b = list(map(len, c))
print("№1.2 - ", b)
# №1.2 -  [5, 2, 12]

b = list(map(lambda x: x ** 2, range(11, 16)))
print("№1.3", b)
# №1.3 [121, 144, 169, 196, 225]


# №2: ф-ії, які самі написали
print()
def f(x):
    return x**2
b = list(map(f, [-1, 2, -3, 4, 5]))
print("№2", b)
# №2 [1, 4, 9, 16, 25]


# №3: вбудовані метод нашого об"єкту:
print()
c = ['hello', 'hi', 'good morning']
b = list(map(str.upper, c))
print("№3 - ", b)
# №3 -  ['HELLO', 'HI', 'GOOD MORNING']


# №4: анонімні ф-ії (lambda):
print()
c = ['hello', 'hi', 'good morning']
b = list(map(lambda x: x[::-1], c))
print("№4.1 - ", b)
# №4.1 -  ['olleh', 'ih', 'gninrom doog']


b = list(map(lambda x: x + '!', ['hello', 'hi', 'good morning']))
print("№4.2 - ", b)
# №4.2 -  ['hello!', 'hi!', 'good morning!']


print()
# SOME INTERESTING EXAMPLES:
c = ['hello', 'hi', 'good morning']
b = list(map(list, c))
print("Ex1: ", b)
# Ex1:  [['h', 'e', 'l', 'l', 'o'], ['h', 'i'], ['g', 'o', 'o', 'd', ' ', 'm', 'o', 'r', 'n', 'i', 'n', 'g']]


c = ['hello', 'hi', 'good morning']
b = list(map(list, c))
d = list(map(sorted, b))
print("Ex2: ", d)
# Ex2:  [['e', 'h', 'l', 'l', 'o'], ['h', 'i'], [' ', 'd', 'g', 'g', 'i', 'm', 'n', 'n', 'o', 'o', 'o', 'r']]


s = list(map(int, input("Enter few numbers in a line: ").split()))   # 1 2 3 4 5
print("Ex3: ", s)
# Ex3:  [1, 2, 3, 4, 5]


lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))
# OUTPUT: [10, 36, 2, 48, 66, 30, 26, 110]


# в map() можна передавати множину/кілька ітерабельних послідовностей
# 23*. Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
print(list(map(lambda x, y: x ** y, list_A, list_B)))
# OUTPUT: [32, 729, 16384]
