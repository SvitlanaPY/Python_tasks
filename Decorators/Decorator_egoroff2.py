# функції, які декоруються, втрачають своє імя та документацію.
# щоб цього уникнути, можна:
# 1. імпортнути декоратор wraps із модуля functools та повісити цей декоратор на нашу функцію inner
# і передати декоратору wraps нашу функцію;
# 2. у функції-декораторі (def table()) добавити рядки із перезаписом __name__ та __doc__ для функції inner:
  # inner.__name__ = func.__name__
  # inner.__doc__ = func.__doc__

from functools import wraps

def table(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print("<table>")
        func(*args, **kwargs)
        print("</table>")
    # inner.__name__ = func.__name__
    # inner.__doc__ = func.__doc__
    return inner

def say():
    print("Hello world")


def sqr(x):
    """
    Функція підносить до квадрату х
    :param x:
    :return:
    """
    print(x**2)

sqr = table(sqr)
print(sqr(2))
print(sqr.__name__)
print(help(sqr))



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