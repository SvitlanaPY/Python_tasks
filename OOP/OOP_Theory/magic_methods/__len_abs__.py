"""
Магічні методи __len__ та __abs__ будуть спрацьовувати тоді, коли ми до об"єкту будемо викликати методи len() та abs()
"hello".__len__()  =  len("hello")
(-78).__abs__()  =  abs(-78)
"""

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)

a = Person("Anna", "Smirnova")
print("a: ", len(a))
b = Person("Svitlana", "Pushchalo")
print("b: ", b.__len__())


print("hello".__len__())
print(len("hello"))
print((-78).__abs__())
print(abs(-78))


class Vidrizok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)   # self.__abs__()

    def __abs__(self):
        return abs(self.x2 - self.x1)

t1 = Vidrizok(5,9)
print("t1:", len(t1))

t2 = Vidrizok(10,5)
print("t2:", len(t2))

