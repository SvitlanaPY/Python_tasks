"""
__eq__  - ==  (equal)
__ne__  - !=  (not equal)
__lt__  - <   (less than)
__le__  - <=  (less equal)
__gt__  - >   (greater than)
__ge__  - >=  (greater equal)
об"єкти/екземпляри класу НЕ підтримують операцій порівняння!

У всіх бінарних операціях з об"єктами - у першого об"єкту (лівого) викликається відповідний магічний метод,
і в цей мегічний метод у якості параметру підставляється інший об"єкт.
a1 == a2 --> a1.__eq__(a2)
a1 < a2 --> a1.__lt__(a2)
"""

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

rec1 = Rectangle(1, 2)
rec2 = Rectangle(3, 4)
# print(rec1 > rec2)   # TypeError: '>' not supported between instances of 'Rectangle' and 'Rectangle'


print("- "*15)
class Rectangle1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print("__eq__ called")
        if isinstance(other, Rectangle1):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print("__lt__ called")
        if isinstance(other, Rectangle1):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        # self == other  -> викличе метод __eq__
        # self < other  -> викличе метод __lt__
        return self == other or self < other


q = Rectangle1(1, 2)
w = Rectangle1(1, 2)
r = Rectangle1(10, 2)
print("??? w == q: ", w == q)
# __eq__ called
# True
print("??? r == w: ", r == w)
# __eq__ called
# False
print("??? r != w: ", r != w)
# __eq__ called
# True

print("??? q < 10: ", q < 10)
# __lt__ called
# True
print("??? q < r: ", q < r)
# __lt__ called
# True
print("??? q <= w: ", q <= w)
# __eq__ called
# ??? q <= w:  True

print("??? q > r: ", q > r)
# __lt__ called
# ??? q > r:  False
print("??? q >= r: ", q >= r)
# __eq__ called
# __lt__ called
# ??? q >= r:  False

