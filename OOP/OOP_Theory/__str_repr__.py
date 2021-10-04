"""
repr - для серіалізації та відладки, є виводом, який є читабельним для інтерпретатора Python.
__repr__ дає строку, оціночне строкове представлення об'єкта.
>>> x = 'foo'
>>> x.__repr__()
"'foo'"
>>> repr(x)
"'foo'"

str - використовується для створення виводу, який має бути читабельним для кінцевого користувача,
це по суті є print()
>>> str('hello world')
'hello world'
----------
>>> repr('hello world')
"'hello world'"
"""

class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person has name {self.name}"

    def __str__(self):
        return f"My name is {self.name}"

    def info(self):
        print(self)

hum = Human('СВІТЛАНА')
hum.info()
# викличеться метод __str__, а не __repr__ і виведе на друк:
# My name is СВІТЛАНА
print("hum: ", hum)
# hum:  My name is СВІТЛАНА


import datetime
today = datetime.datetime.now()
print(str(today))    # 2021-08-30 18:49:00.352057
print(repr(today))   # datetime.datetime(2021, 8, 30, 18, 49, 0, 352057) - официальное представление обєкта дати


# >>> str('hello world')
# 'hello world'
# >>> repr('hello world')
# "'hello world'"
