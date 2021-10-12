
class Rectangle:
    __slots__ = 'width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def perymetr(self):
        return (self.width + self.height) * 2

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
print("height =", r.height, "width =", r.width)

print("area: ", r.area)
print("perymetr: ", r.perymetr)


class RectangleSlots:
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a    # setter is called, new private __width attribute is created and then returned by getter
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print("setter called")
        self.__width = value

rs = RectangleSlots(5, 6)   # setter called
# setter called, бо створюється об"єкт rs, і в __init__ запускається self.width = a,
# який дьоргає сеттер, де відбувається print("setter called") та створюється новий private __width attribute
print("width =", rs.width)   # width = 5: доступаємось до width вже через проперті
print("__width =", rs._RectangleSlots__width)


class Rectngl:
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a    # setter is called, new private __width attribute is created and then returned by getter
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print("setter called")
        self.__width = value


class Square(Rectngl):
    pass

s = Square(4, 5)
"""
дочірні класи, незважаючи на те, що у парентів є __slots__, вже будуть мати магічну змінну __dict__, 
тому в s ми можемо присвоювати різні атрибути
"""
print(s.__dict__)   # {}
s.att1 = 10
print(s.att1)   # 10
print(s.__dict__)   # {'att1': 10}

"""
Щоб в дочірніх класах задати параметри __slots__, потрібно їх прописати і в дочірньому класі
Але ми не мусимо дублювати значення, а достатньо лише розширити параметрами дочірнього класу: 
__slots__ = "color"

"""

print("% "*20)
class Rectngl1:
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a    # setter is called, new private __width attribute is created and then returned by getter
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print("setter called")
        self.__width = value


class Square1(Rectngl1):
    __slots__ = 'color'   # __slots__ дочірнього класу розширюють __slots__ батьківського класу

    def __init__(self, a, b, color):
        self.color = color
        super().__init__(a, b)


m = Square1(5, 5, 'red')
# setter called
print(m.color, m.height, m.width)   # red 5 5
# магічна змінна __dict__ тепер недоступна
# print(m.__dict__)  # AttributeError: 'Square1' object has no attribute '__dict__'

print("= "*20)
"""
Якщо ми НЕ хочемо додавати нові атрибути в __slots__ (не хочемо розширювати список __slots__), 
то в дочірньому класі достатньо лише задати порожню колекцію:
__slots__ = tuple() 
"""

class Square1(Rectngl1):
    __slots__ = tuple()

    def __init__(self, a, b):
        super().__init__(a, b)