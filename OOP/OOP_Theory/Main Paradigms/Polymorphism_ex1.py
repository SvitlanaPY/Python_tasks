"""
ПОЛІМОРФІЗМ - спосіб по-різному обробляти об"єкти, в залежності від їх типу,
шляхом вкористання одного і того ж за назвою методу (але різного за функціональністю).
Це здатність декількох типів об"єктів реалізовувати одну і ту ж саму функціональність:
різні об"єкти класу, які можуть виконувати одну і ту ж функціональність, але працювати по-різному.

"""
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rect_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_square_area(self):
        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_area(self):
        return 3.14 * self.r ** 2
