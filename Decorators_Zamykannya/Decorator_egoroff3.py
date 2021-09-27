print("\n1: check name and DOC for def say() BEFORE decoration")
def table(func_):
    def inner(*args, **kwargs):
        print('<table>')
        func_(*args, **kwargs)
        print('</table>')
    return inner

def say():
    """
    Функція say() друкує привітання
    :return: str

    """
    print('hello world!')

say()
# hello world!
print(say)   # <function say at 0x7f9397c3b8b0>
print(say.__name__)
# say   # ім"я функції
print(help(say))
# Help on function say in module __main__:
#
# say()
#     Функція say() друкує привітання
#     :return: str
#
# None


print("\n2: check name and DOC for def say() AFTER decoration")
def table1(func_):
    def inner1(*args, **kwargs):
        print('<table>')
        func_(*args, **kwargs)
        print('</table>')
    return inner1

@table1
def say():
    """
    Функція say() друкує привітання
    :return: str

    """
    print('hello world!')

say()
# <table>
# hello world!
# </table>
print(say)   # <function table1.<locals>.inner1 at 0x7f2ef6dfc430>
print(say.__name__)
# inner1    # ім"я ф-ії say змінюється на inner1 при декоруванні
print(help(say))
# Help on function inner1 in module __main__:
#
# inner1(*args, **kwargs)
#
# None


# функції при декоруванні, втрачають своє імя та документацію.
# щоб цього уникнути, можна:
# 1. у функції-декораторі (def table()) добавити рядки із перезаписом __name__ та __doc__ для функції inner:
  # inner.__name__ = func.__name__
  # inner.__doc__ = func.__doc__
# 2. імпортнути декоратор @wraps із модуля functools та повісити цей декоратор на нашу функцію inner
# і передати декоратору @wraps нашу функцію у якості аргумента.


# 1.
print("\n3: перезаписуємо __name__ та __doc__ для функції inner ")
def table_t(func_):
    def inner11(*args, **kwargs):
        print('<table>')
        func_(*args, **kwargs)
        print('</table>')
    inner11.__name__ = func_.__name__
    inner11.__doc__ = func_.__doc__
    return inner11

@table_t
def say():
    """
    Функція say() друкує привітання
    :return: str

    """
    print('hello world!')

say()
print(say)
# <table>
# hello world!
# </table>
print(say.__name__)   # <function table_t.<locals>.inner11 at 0x7fa740541550>
# say    # імя функції НЕ змінюється на inner11, а залишається say
print(help(say))
# Help on function say in module __main__:
#
# say(*args, **kwargs)
#     Функція say() друкує привітання
#     :return: str


# 2. імпортнути декоратор @wraps із модуля functools та повісити цей декоратор на нашу функцію inner
# і передати декоратору @wraps нашу функцію у якості аргумента.
print("\n4: використання декоратора @wraps із модуля functools, який вішається на функцію inner22 і приймає параметром ф-ію-начинку")
from functools import wraps

def table_tt(func_):

    @wraps(func_)
    def inner22(*args, **kwargs):
        print('<table>')
        func_(*args, **kwargs)
        print('</table>')
    return inner22

@table_tt
def say():
    """
    Функція say() друкує привітання
    :return: str

    """
    print('hello world!')

say()
# <table>
# hello world!
# </table>
print(say)   # <function say at 0x7f424ffb1430>
print(say.__name__)
# say   # імя функції НЕ змінюється на inner22, а залишається say
print(help(say))
# Help on function say in module __main__:
#
# say()
#     Функція say() друкує привітання
#     :return: str
#
# None
