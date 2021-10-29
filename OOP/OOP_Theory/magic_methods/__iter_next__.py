"""
За допомогою магічних методів __iter__ та __next__ - наш клас можна зробити ітерабельним і
екземпляри класу зможуть ітеруватись, тобто екземпляри класу можна буде обходити в циклі for.
Отже, ці магічні методи дозволять обходити екземпляри класу у циклі for:
__iter__ -
__next__ -
"""


class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks


igor = Student('Igor', 'Nikolaev', [3, 4, 5, 4, 5])


"""
Якщо ми спробуємо обійти наш екземпляр igor класу Student в циклі for:
for i in igor:
    print(i)
то отримаємо помилку: TypeError: 'Student' object is not iterable

Списки є ітерабельними об"єктами, тобто їхні елементи можна обійти в циклі for.
Ітерабельний об"єкт - об"єкт, з якого можна зробити ітератор, тобто до якого можна застосувати метод iter(), 
напр. до списків/словників/кортежів/стрічок/range можна застосувати метод iter().
a = [1, 2, 3, 4, 5]
ОТЖЕ,
Ітерабельними є об"єкти, які:
1. дають можливість обходити свої елементи по черзі в циклі, і 
2. можуть бути перетворені до ітератора за допомогою ф-ії iter(): b = iter(a)
print(b)   # <list_iterator object at 0x7f1ad0f7b2e0>

Ітератор представляє собою колекцію, елементи якої можна по-черзі обійти лише ОДИН раз, 
а обхід елементів цієї колекції відбувається шляхом виклику ф-ії next(),
тобто до ітератора можна застосувати ф-ію next():
print(next(b))   # 1
print(next(b))   # 2
print(next(b))   # 3
print(next(b))   # 4
print(next(b))   # 5
І коли ітератор підійде до кінця - то виникає помилка StopIteration:
print(next(b))   # StopIteration

І щоб обійти знову цю колекцію - потрібно створити інший ітератор
і створити ітератор можна шляхом виклику магічного метода __iter__:
с = a.__iter__()
print(с)   # <list_iterator object at 0x7f1900f77d00>
і ми можемо НЕ викликати ф-ію next() до нашої змінної с, а ми можемо тепер викликати магічний метод __next__ від змінної с:
с.__next__():
print(с.__next__())   # 1
print(с.__next__())   # 2
print(с.__next__())   # 3
print(с.__next__())   # 4
print(с.__next__())   # 5

Щоразу, коли ми будь-яку колекцію(список, словник...) обходимо в циклі for, 
то під капотом пайтон перетворює це все в ітератор і до цього ітератора викликається ф-ія next().
І коли ітератор дійде до кінця, тобто ми обійдемо всі елементи, то викличеься помилка StopIteration.
Але в циклі for це виключення/помилка обробляється, і тому ми не бачимо StopIteration повідомлення.

Наш клас можна також зробити ітерабельним.
За допомогою магічних методів __iter__ та __next__ - наш клас можна зробити ітерабельним і
екземпляри класу зможуть ітеруватись, тобто екземпляри класу можна буде обходити в циклі for.
Отже, ці магічні методи дозволять обходити екземпляри класу у циклі for.
"""


"""
Якщо в класі реалізований магічний метод __getitem__, то пайтон використає його для обходу елементів колекції.
"""
class Student_1:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]


ivan = Student_1('IVAN', 'Nikolaev', [3, 4, 5, 4, 5])
for i in ivan:
    print(i)
# I
# V
# A
# N


"""
Проте __getitem__ метод не є основним способом для організації/реалізації ітерації.
Основним способом обходити колекцію є метод __iter__
"""
class Student_2:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]

    def __iter__(self):
        print("__iter__  called")
        return iter(self.name)   # повертаємо ітератор у типу строки (бо name - це строка)
        # і у самої строки name буде викликатись метод/ф-ія next(), цей метод next() викликається всередині класу str,
        # а не всередині даного методу __iter__


taras = Student_2('Taras', 'Shevchuk', [3, 4, 5, 4, 5])
for i in taras:
    print(i)


"""
Щоб обходити екземпляр класу в циклі for.
Коли ми вказуємо методу __iter__, що хочемо обходити наш власний клас, який ми створили, 
то нам знадобиться метод __next__, де описуємо логіку отримання наших елементів, 
наприклад логіку отримання кожної букви з імені(атрибуту name)
"""

class Marks:
    def __init__(self, values):
        self.values = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print("call __next__ in class Marks")
        if self.index >= len(self.values):
            self.index = 0
            raise StopIteration
        letter = self.values[self.index]
        self.index += 1
        return letter


class Student_3:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        print("__iter__  called")
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print("call __next__ in class Student_3")
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter

m = Marks([3, 4, 5, 4, 5])
roman = Student_3('Roman', 'Shevchuk', m)
for i in roman:
    print(i)


"""
Щоб екземпляр класу став ітератором, потрібно всередині класу визначити метод  __next__.
Об"єкт є ітератором, якщо він має метод __next__
"""

from random import random
class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

x = RandomIterator(3)
print(next(x))
print(next(x))
print(next(x))
# print(next(x))   # StopIteration

"""
Щоб можна було використовувати наш ітератор в циклі for, 
ми повинні вміти викликати ф-ію __iter__ від нашого х.
Тобто, щоб ми могли проітерувати наш об"єкт класу (перерахувати його елементи), у нього має бути визначений метод __iter__, який повертається нам ітератором.
А щоб об"єкт був ітератором, у нього має бути визначений метод __next__()
"""
class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration

for i in RandomIterator(10):
    print(i)

