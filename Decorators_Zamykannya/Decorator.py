#  decorator - it is a function (def decorator()) that accept another function (func) and returns the function (inner)
# def decorator(func):
#  decorator is used when we want to add another behaviour in our function (def say():)
# say = decorator(say):
# say()

def decorator(func):   # func = say()
    def inner():
        print('start decorator...')
        func()
        print('finish decorator')
    return inner
def say():
    print('Hello world!')
say = decorator(say)
say()
# OUTPUTS:
# start decorator...
# Hello world!
# finish decorator
print(say)   # <function decorator.<locals>.inner at 0x7f45178c8f70>

d = decorator(say)
print(d)   # <function decorator.<locals>.inner at 0x7fb1e7fb8ee0>



def decorator1(func):
    def inner(m):
        print('start decorator...')
        func(m)
        print('finish decorator...')
    return inner
def say1(name):
    print('Hello world!', name)

say1 = decorator1(say1)
say1('Vasya')
# start decorator...
# Hello world! Vasya
# finish decorator...


def decorator2(func):
    def inner(*args, **kwargs):
        print('start decorator...')
        func(*args, *kwargs)
        print('finish decorator...')
    return inner
def say2(name, surname, age):
    print('Hello,', name, surname, age)

say2 = decorator2(say2)
say2('Vasya', 'Ivanov', 35)

# start decorator...
# Hello, Vasya Ivanov 35
# finish decorator...


def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, *kwargs)
        print('</h1>')
    return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table')
        func(*args, **kwargs)
        print('</table')
    return inner
def say3(name, surname, age):
    print('Hello,', name, surname, age)

say3 = table(header(say3))   # header in table
say3('Vasya', 'Ivanov', 35)
# <table
# <h1>
# Hello, Vasya Ivanov 35
# </h1>
# </table

# HOW IT WORKS:
# header is the first function that is called, and this function returns inner:
# (<h1>
# Hello, Vasya Ivanov 35
# </h1>)
# this result is sent in our inner function table

# @header
# @table
# say3 = header(table(say3))
# say3 = table(header(say3))   # header in table
# say3('Vasya', 'Ivanov', 35)
#



