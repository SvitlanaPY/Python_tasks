"""
ENCAPSULATION/ ІНКАПСУЛЯЦІЯ - підхід/механізм/принцип, що полягає у обмеженні прямого доступу до даних
(полів, проперті, методів, атрибутів...)

INHERETANCE/ НАСЛІДУВАННЯ - підхід/механізм/принцип за яким об"єк/клас(підклас/дочірній клас) набуває деяких/чи усіх властивостей іншого об"єкту
(атрибутів та методів від іншого(батьківського) класу).
Це підхід до спільного використання якихось спільних функцій у класах, дає можливість уникати дублювання коду в класі,
(тобто ф-ій, методів, які вже має інший клас).
В наслідування як правило визначається два типи класів: батьківський клас/базовий клас (клас, який успадковується)
та дочірній клас/ похідний клас (клас, який успадковує ін клас)
Наслідування викор-ся для того, щоб ми могли розширити функціонал нашого класу.
Це забезпечує можливість НЕ дублювати код в класах, які потребують певної функціональності від ін класів.

При наслідуванні потрібно викликати super().
super() нам дає можливість використовувати атрибути і загалом методи, які у нас будуть в батьківському класі,
без super() ми не зможемо доступатись до атрибутів батьківського класу, визначених в методі __init__.

POLYMORPHISM/ ПОЛІМОРФІЗМ - спосіб по-різному обробляти об"єкти, в залежності від їх типу,
шляхом вкористання одного і того ж за назвою методу (але різного за функціональністю)
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
