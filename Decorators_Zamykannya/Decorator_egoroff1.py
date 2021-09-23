#  decorator - it is a function (def decorator()) that accept another function (func) and returns the function (inner)
# def decorator(func):
#  decorator is used when we want to add another behaviour in our function (def say():)
# say = decorator(say):
# say()

# Декоратор - це функція, яка приймає аргументом іншу функцію і повертає ф-ію;
# декоратори потрібні, щоб розширити функціонал якоїсь існуючої ф-ії.
#
# У декораторі ми говоримо про ТРИ функції:
# 1. ф-ія-НАЧИНКА: це ф-ія, яку декорують, ф-ія, функціонал якої розширюють:
# def say():
    # print('Hello world!')
# 2. ф-ія-ОБГОРТКА: це ф-ія, яка декорує, яка розширює функціонал ф-ії-начинки;
# як правило їй дають назву: def wrapper чи def inner.
# Ф-ія-обгортка як правило приймає ті ж аргументи, що і ф-ія-начинка.
# Ф-ія-обгортка в своєму тілі викликає ф-ію начинку,
# а також містить додатковий код, який розширює функціонал ф-ії-начинки.
# Ф-ія-обгортка є внутрішньою функцією ф-ії-декоратора.
#     def inner():
#         print('start decorator...')
#         func()
#         print('finish decorator')
# 3. Ф-ія-ДЕКОРАТОР/ ф-ія ініціалізації декоратора; ця ф-ія на вхід приймає ф-ію начинку (ф-ію, яка розширюється),
# а повертає ф-ію-обгортку(ф-ію, яка розширює).
# def decorator_(func_):   # func_ - це є ф-ія-начинка: def say()
#     def inner():      # ф-ія-обгортка
#         <код1 ... >   # розширення функціоналу ф-ії-начинки def say()>
#         func_()       # виклик ф-ії-начинки def say()
#         <код2 ... >   # розширення функціоналу ф-ії-начинки def say()>
#     return inner      # повертаємо ф-ію-обгортку БЕЗ її виклику: тобто БЕЗ дужок ()

# У основному коді ми декоруємо ф-ію-начинку, а саме:
# викликаємо ф-ію-декоратор def decorator_, якій параметром передаємо нашу ф-ію-начинку(назву ф-ії-начинки),
# а тоді цей виклик зберігаємо по імені ф-ії-начинки: say = decorator_(say)
# АБО ж:
# навішуємо ф-ію-декоратор на ф-ію-начинку за допомогою @:
# @decorator_
# def say():
#    <код ф-ії say() ... >
# print(say())


print("\n1. ----------------- ")
def decorator_(func_):   # func_ = say()
    def inner():
        print('start decorator...')
        func_()
        print('finish decorator !!!')
    return inner

# @decorator_
def say():
    print('HELLO world!')

# print(say())

say = decorator_(say)
say()


print("\n2. ----------------- ")
# Аргументи (к-сть аргументів) ф-ії-начинки можуть змінюватись.
# Тому, при описі ф-ії-обгортки, всі аргументи, які вона приймає на вхід,
# навіть незалежно, чи вони є, чи їх немає, прописуйте через *args, **kwargs: def inner(*args, **kwargs)

def decorator_1(func_):   # func_ = say()
    def inner(*args, **kwargs):   # def inner(*args, **kwargs)
        print('start decorator_1...')
        func_(*args, **kwargs)   # def func_(*args, **kwargs)
        print('finish decorator_1...')
    return inner

# @decorator_1
def say_1():
    print('HELLO world!')

say_1 = decorator_1(say_1)
say_1()


# EXAMPLES:
print("\n3. ----------------- ")
def decorator3(func):   # func = hello() and then func = bye()
    def inner():
        print('start decorator...')
        func()
        print('finish decorator')
    return inner

# @decorator3
def hello():
    print('HELLO world!')

# @decorator3
def bye():
    print('BYE world!')


hello = decorator3(hello)
hello()
bye = decorator3(bye)
bye()
# OUTPUTS:
# start decorator...
# HELLO world!
# finish decorator
# start decorator...
# BYE world!
# finish decorator

# print(hello)   # <function decorator.<locals>.INNER at 0x7f45178c8f70>


print("\n4. ----------------- ")
def decorator4(func):
    def inner(n):
        print('start decorator...')
        func(n)
        print('finish decorator...')
    return inner

def say4(name):
    print('Hello,', name)

say4 = decorator4(say4)
say4('Vasya')
# start decorator...
# Hello, Vasya
# finish decorator...


print("\n5. ----------------- ")
def decorator5(func):
    def inner(n, s):
        print('start decorator...')
        func(n, s)
        print('finish decorator...')
    return inner

def say5(name, surname):
    print('Hello,', name, surname)

say5 = decorator5(say5)
say5('Vasya', 'Ivanov')
# start decorator...
# Hello, Vasya Ivanov
# finish decorator...


print("\n6. ----------------- ")
# Аргументи (к-сть аргументів) ф-ії-начинки можуть змінюватись
# Тому при описі ф-ії-обгортки всі аргументи, які вона приймає на вхід,
# навіть незалежно, чи вони є, чи їх немає, прописуйте через *args, **kwargs: def inner(*args, **kwargs)
def decorator6(func):
    def inner(*args, **kwargs):
        print('start decorator...')
        func(*args, *kwargs)
        print('finish decorator...')
    return inner

def say6(name, surname, age):
    print('Hello,', name, surname, age)

say6 = decorator6(say6)
say6('Vasya', 'Ivanov', 35)

# start decorator...
# Hello, Vasya Ivanov 35
# finish decorator...

print("\n7. ----------------- ")
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, *kwargs)
        print('</h1>')
    return inner

def say7(name, surname, age):
    print('Hello,', name, surname, age)

say7 = header(say7)
say7('Vasya', 'Ivanov', 35)


# На одну ф-ію можна навісити КІЛЬКА декораторів
print("\n8. ----------------- ")
def header(func):
    def inner1(*args, **kwargs):
        print('<h1>')
        func(*args, *kwargs)
        print('</h1>')
    return inner1

def table(func):
    def inner2(*args, **kwargs):
        print('<table')
        func(*args, **kwargs)
        print('</table')
    return inner2

def say_say(name, surname, age):
    print('Hello,', name, surname, age)

say_say = table(header(say_say))   # header in table
say_say('Vasya', 'Ivanov', 35)

# ЯК ЦЕ ПРАЦЮЄ:
# Спершу викликалась ф-ія header() і вона поверне нам нашу ф-ію inner1()
# <h1>
# Hello, Vasya Ivanov 35
# </h1>
# і цей результат буде передаватись всередину нашої ф-ії table() і отримуємо наступне:
# <table
# <h1>
# Hello, Vasya Ivanov 35
# </h1>
# </table
#


print("\n9. ----------------- ")
# або можна записати ще отак:
# навісити над ф-ією def say_say(name, surname, age) два наших декоратори
# @header
# @table
# і викликати ф-ію з параметрами:
# say_say('Vasya', 'Ivanov', 35)

def header(func):
    def inner1(*args, **kwargs):
        print('<h1>')
        func(*args, *kwargs)
        print('</h1>')
    return inner1

def table(func):
    def inner2(*args, **kwargs):
        print('<table')
        func(*args, **kwargs)
        print('</table')
    return inner2


@header   # say_say = header(say_say)
@table    # say_say = header(table(say_say))
def say_say(name, surname, age):
    print('Hello,', name, surname, age)

# say_say = header(table(say_say))   # table IN header
say_say('Vasya', 'Ivanov', 35)
# <h1>
# <table
# Hello, Vasya Ivanov 35
# </table
# </h1>
