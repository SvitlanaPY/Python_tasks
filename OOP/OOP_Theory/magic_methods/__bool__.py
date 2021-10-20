"""
magic methods = dunder methods (Double UNDERscore) -
це спеціальні методи, які починаються і закінчуються на два нижніх підкреслення.
Ці методи мають певний функціонал і викликаються всередині класу у певний момент.

__bool__
bool від екземпляру класу завжди буде True, навіть якщо цей метод у класі не визначено
p1 = Person(0, 0)   # p1 - екземпляр класу Point
bool(p1) = True
Якщо метод __bool__ не реалізовано в класі, а метод __len__ - реалізований, то пайтон буде дивитись на метод __len__.
Якщо немає ні метода __bool__, ні метода __len__, то екземпляри завжди будуть True.
"""


"""
Якщо в класі не реалізовано ні метода __bool__, ні метода __len__, то екземпляри завжди будуть True
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(0, 0)
print(bool(p1))   # True, хоча мало б бути False, бо bool() від нуля - False


print("-----------------------------")
"""
Якщо даного методу немає в класі, то пайтон буде дивитись на метод __len__
"""
class PointTest:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("call __len__")
        return abs(self.x - self.y)


p2 = PointTest(3, 9)
print(bool(p2))
# call __len__
# True
print(bool(PointTest(9, 9)))
# call __len__
# False
print(bool(PointTest(0, 0)))
# call __len__
# False


print("++++++++++++++++++++")
class PointNew:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("call __len__")
        return abs(self.x - self.y)

    def __bool__(self):
        print("call __bool__")
        return 5

p3 = PointNew(3, 4)
# print(bool(p3))    # TypeError: __bool__ should return bool, returned int


print("=============================")
class PointGood:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("call __len__")
        return abs(self.x - self.y)

    def __bool__(self):
        print("call __bool__")
        return self.x != 0 or self.y != 0


p4 = PointGood(3, 4)
print(bool(p4))
# call __bool__
# True
print(bool(PointGood(0, 0)))
# call __bool__
# False
print(bool(PointGood(0, -5)))
# call __bool__
# True


print("************************")
"""
__bool__ можна викликати неявно: 
вираз "if point_"  еквівалентний виразу  "bool(point_)"
"""
point_ = PointGood(2, 3)
if point_:           # = bool(point_)
    print('HELLO')
# call __bool__
# HELLO


print("_____________________________")
ppoint_ = PointGood(0, 0)
if ppoint_:            # = bool(ppoint_)
    print('HELLO')
# call __bool__


print("% "*15)
"""
12*. Making Your Objects Truthy or Falsey Using __bool__().
Create class MyOrder with cart and customer instance attributes.
Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
e.g.:
order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
bool(order_1)
True
bool(order_2)
False
"""

class MyOrder:
    def __init__(self, cart= [], customer=''):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) != 0:
            return True
        return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
# OUTPUT: True
print(bool(order_2))
# OUTPUT: False
