"""
ENCAPSULATION/ ІНКАПСУЛЯЦІЯ - підхід/механізм/принцип, що полягає у обмеженні прямого доступу до даних
(полів, проперті, методів, атрибутів...)
INHERETANCE/ НАСЛІДУВАННЯ - підхід/механізм/принцип за яким об"єк/клас(підклас/дочірній клас) набуває деяких/чи усіх властивостей іншого об"єкту
(атрибутів та методів від іншого(батьківського) класу).
Наслідування викор0ся для того, щоб ми могли розширити функціонал нашого класу.
Це забезпечує можливість НЕ дублювати код в класах, які потребують певної функціональності від ін класів.
POLYMORPHISM/ ПОЛІМОРФІЗМ -
"""


class Person:   # parent class/ base class
    def can_breath(self):
        print('I can breath, I am human')

    def can_walk(self):
        print('I can walk')

class Doctor(Person):   # sub-class/ child class/ derived class
    # def can_breath(self):
    #     print('I can breath, I am human')
    #
    # def can_walk(self):
    #     print('I can walk')

    def can_cure(self):
        print('I can cure')

class Architect(Person):
    # def can_breath(self):
    #     print('I can breath, I am human')
    #
    # def can_walk(self):
    #     print('I can walk')
    #
    def can_build(self):
        print('I can build a house')

class Ortoped(Doctor):
    def can_cure_skeletal_system(self):
        print('I can cure skeletal system')


d = Doctor()
a = Architect()
print(issubclass(Doctor, Person))   # True
print(issubclass(Person, Doctor))   # False
print(isinstance(d, Doctor))    # True
print(isinstance(d, Person))    # True
print(isinstance(d, Architect))    # False
# print(Doctor.__mro__)

d.can_cure()
d.can_breath()
d.can_walk()

a.can_build()
a.can_breath()
a.can_walk()
