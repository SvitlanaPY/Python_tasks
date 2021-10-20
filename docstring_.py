"""
docstring - спеціальний механізм, що дозволяє додавати пояснення всередину коду певним чином і в певному місці.
docstring - строка документування, і як правило у всіх вбудованих (built-in) об"єктів вона існує
і щоб отримати доступ до неї - потрібно викликати ф-ію help() і звернутись до об"єкту, який нас цікавить:
help(abs)
або
abs.__doc__
Але не у всіх об"єктів цей атрибут __doc__ є присутній.
"""
help(abs)
"""

Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
"""
print(abs.__doc__)   # Return the absolute value of the argument.


help(print)
"""
Help on built-in function print in module builtins:
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
"""

"""
Але не у всіх об"єктів цей атрибут __doc__ є присутній.
Щоб його створити, потрібно у ф-ії/методі/модулі/класі на першій строці/рядку після визначення ф-ії/метода/модуля/класу додати строку з текстом/поясненням до ф-ії.
Але лише перша строка/рядок, яка написана після визначення ф-ії/метода/модуля/класу попаде в атрибут __doc__, 
але як правило пояснення складається з кількох стрічок, тому краще одразу створювати багатострокову стрічку (в потрійних лапках)
"""
"""
Де писати docstring-и:
1. у Функції
2. у Модулі (на самому початку в основному коді)
import random
help(random)
3. в класі
За допомогою команди Ctrl + Q ми можемо звертатись до docstring-и
"""
# 1. ФУНКЦІЯ
def get_even(lst):
    """Функція створює список із парних чисел
    even_lst - новий список з парних чисел"""   # ця строка іде в атрибут __doc__
    even_lst = []
    for elem in lst:
        if elem % 2 == 0:
            even_lst.append(elem)
    return even_lst

print(get_even.__doc__)
"""
Функція створює список із парних чисел
     even_lst - новий список з парних чисел
"""

help(get_even)
"""
Help on function get_even in module __main__:

get_even(lst)
    Функція створює список із парних чисел
"""

# 2. МОДУЛЬ
import docstring_test
help(docstring_test)
"""
Help on module docstring_test:

NAME
    docstring_test - dcstring in module docstring_test

FILE
    /home/svitlana/Projects/Python_Tasks/docstring_test.py
"""

# 3. КЛАС
help(docstring_test.MMM)
"""
Help on class MMM in module docstring_test:

class MMM(builtins.object)
 |  dcstring in class MMM
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
"""

"""
Існує кілька варіантів/стилів оформлення docstring-ги:
File | Settings | Tools | Python Integrated Tools: Docstring format
https://www.datacamp.com/community/tutorials/docstrings-python
"""
