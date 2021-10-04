"""
ЯК перевизначати магічні методи батьківського класу
"""

class Person:   # parent class

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print("Person can breathe")


class Doctor(Person):    # sub-class
    def breathe(self):
        print("Doctor can also breathe")


p = Person('John')
# init Person
d = Doctor("Adam")
# init Person
print(p.name, d.name)
# John Adam


print()
class Human:   # parent class

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print("Human can breathe")


class Doc(Human):    # sub-class
    def breathe(self):
        print("Doctor can also breathe")

    def __str__(self):
        return f"Лікар {self.name}"


pp = Human('Tom')
# init Person
dd = Doc("Tina")
# init Person
print(pp.name, '  ', dd.name)
# Tom    Tina
print("pp:", pp)
# pp: <__main__.Human object at 0x7fa84fea02b0>
print("dd:", dd)
# dd: Лікар Tina
# коли ми друкуємо об"єкт pp класу Human, то він намагається знайти метод __str__ всередині свого класу Human, його там немає,
# і тоді він йде вверх по ланцюжку до свого батьківського класу, тобто до класу object,
# і користується методом __str__, який є у класі object
# тому і виводиться: pp: <__main__.Human object at 0x7fa84fea02b0>
# а об"єкт dd класу Doc знайде метод __str__ всередині свого класу Doc і виведе - Лікар Tina


print()
class Human2:   # parent class

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print("Human can breathe")

    def __str__(self):
        return f"Лікар {self.name}"


class Doc2(Human2):    # sub-class
    def breathe(self):
        print("Doctor can also breathe")


ppp = Human2('Sam')
# init Person
ddd = Doc2("Sally")
# init Person
print("ppp:", ppp, "   ddd:", ddd)
# ppp: Лікар Sam    ddd: Лікар Sally


print()
class Human3:   # parent class
    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print("Human can breathe")

    def __str__(self):
        return f"Person {self.name}"


class Doc3(Human3):    # sub-class
    def breathe(self):
        print("Doctor can also breathe")

    def __str__(self):
        return f"Лікар {self.name}"


h = Human3('Roy')
# init Person
g = Doc3("Ruslana")
# init Person

print("h:", h, "   g:", g)
# h: Person Roy    g: Лікар Ruslana


print()
"""
COMBO EXAMPLE
"""
class Person:   # parent class

    def __init__(self, name):
        print('init Person')
        self.name = name

    def breathe(self):
        print("Person can breathe")

    def walk(self):
        print('Person can walk')

    def sleep(self):
        print('Person can sleep')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f"Person {self.name}"


class Doctor(Person):    # sub-class

    def breathe(self):
        print("Doctor can also breathe")

    def __str__(self):
        return f"Лікар {self.name}"


aa = Person('JEP')
# init Person
bb = Doctor("Jessika")
# init Person
aa.combo()
# Person can breathe
# Person can walk
# Person can sleep
bb.combo()
# Doctor can also breathe
# Person can walk
# Person can sleep
print(aa, '   ', bb)
# Person JEP    Лікар Jessika


