"""
ПОЛІМОРФІЗМ - спосіб по-різному обробляти об"єкти, в залежності від їх типу,
шляхом вкористання одного і того ж за назвою методу (але різного за функціональністю)
наприклад метод len():
len("Hello") ---> 5
len([10, 2, 5, 4, 7, 8])  ---> 6
len({"name": "Anna", "age": 25}) ---> 2
"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle: {self.a}*{self.b} = "

class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2

    def __str__(self):
        return f"Square: {self.a} ** 2 = "


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r ** 2

    def __str__(self):
        return f"Circle radius = {self.r}"
