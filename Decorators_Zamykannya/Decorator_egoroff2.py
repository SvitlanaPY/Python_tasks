# функції, які декоруються, втрачають своє імя та документацію.
# щоб цього уникнути, можна:
# 1. імпортнути декоратор @wraps із модуля functools та повісити цей декоратор на нашу функцію inner
# і передати декоратору @wraps нашу функцію у якості аргумента.
# 2. у функції-декораторі (def table()) добавити рядки із перезаписом __name__ та __doc__ для функції inner:
  # inner.__name__ = func.__name__
  # inner.__doc__ = func.__doc__


print("\n1: check name for def say() BEFORE decoration")
def table(func_):
    def inner(*args, **kwargs):
        print('<table>')
        func_(*args, **kwargs)
        print('</table>')
    return inner

def say():
    print('hello world!')

say()    # hello world!
print(say)   # <function say at 0x7f35fc79c0d0>
print(say.__name__, " --> name for def say() BEFORE decoration")


print("\n2. check name for def say() AFTER decoration")
def table(func_):
    def inner(*args, **kwargs):
        print('<table>')
        func_(*args, **kwargs)
        print('</table>')
        # inner.__name__ = func.__name__
        # inner.__doc__ = func.__doc__
    return inner

@table
def say():
    print('hello world!')

say()
print(say)   # <function table.<locals>.inner at 0x7fe76afcc160>
print(say.__name__, " --> name for def say() AFTER decoration")  # inner


print("\n3. check documentation/help on function def sqr() BEFORE decoration")
from functools import wraps

def table(func):

    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")
    return inner

def sqr(x):
    """
    Функція підносить до квадрату х
    :param x:
    :return:
    """
    print(x**2)

print(sqr)   # <function sqr at 0x7f9ff84b61f0>
print(sqr.__name__)
# sqr
sqr(2)   # 4
print(help(sqr))
# Help on function sqr in module __main__:
#
# sqr(x)
#     Функція підносить до квадрату х
#     :param x:
#     :return:
# None


print("\n4. check DOC/help on function def sqr() BEFORE decoration")
def table1(func):

    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner

@table1
def sqr(x):
    """
    Функція підносить до квадрату х
    :param x:
    :return:
    """
    print(x**2)

print(sqr)   # <function table1.<locals>.inner at 0x7f908d6fc550>
print(sqr.__name__)
# inner
sqr(2)
# <table>
# 4
# </table>
print(help(sqr))
# Help on function inner in module __main__:
#
# inner(*args, **kwargs)   # справка по ф-ії inner, в якій нічого немає
# None


print("\n5. у функції-декораторі (def table()) добавити рядки із перезаписом __name__ та __doc__ для функції inner")
def table1(func):

    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")
    inner.__name__ = func.__name__
    inner.__doc__ = func.__doc__
    return inner

@table1
def sqr(x):
    """
    Функція підносить до квадрату х
    :param x:
    :return:
    """
    print(x**2)

print(sqr)   # <function table1.<locals>.inner at 0x7f489a1ee670>
print(sqr.__name__)
# sqr   # !!!!!!!!!!!!!!!!! імя ф-ії НЕ міняється на inner, а залишилось sqr
sqr(2)
# <table>
# 4
# </table>
print(help(sqr))
# Help on function sqr in module __main__:
#
# sqr(*args, **kwargs)
#     Функція підносить до квадрату х
#     :param x:
#     :return:
#
# None


print("\n6. використання декоратора @wraps із модуля functools, який вішається на функцію inner і приймає параметрои ф-ію-начинку")
from functools import wraps

def table1(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")
    return inner

@table1
def sqr(x):
    """
    Функція підносить до квадрату х
    :param x:
    :return:
    """
    print(x**2)

print(sqr)   # <function table1.<locals>.inner at 0x7f489a1ee670>
print(sqr.__name__)
# sqr   # !!!!!!!!!!!!!!!!! імя ф-ії НЕ міняється на inner, а залишилось sqr
sqr(2)
# <table>
# 4
# </table>
print(help(sqr))
# Help on function sqr in module __main__:
#
# sqr(x)
#     Функція підносить до квадрату х
#     :param x:
#     :return:
#
# None


print("\n7. ++++++++++++++++++++++++++")
def get_names_page(names_list) -> str:
    template_head = "<h3> User names: </h3>\n"
    string_info = template_head
    for i, name in enumerate(names_list):
        if i + 1 == len(names_list):
            template = f"<p> {name} </p>"
            string_info += template
        else:
            template = f"<p> {name} </p>\n"
            string_info += template

    return string_info


print(get_names_page(["Misha", "Olya", "Vitaliy", "Vita"]))
