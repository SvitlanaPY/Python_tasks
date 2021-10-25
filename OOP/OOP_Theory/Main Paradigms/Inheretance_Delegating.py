"""
ДЕЛЕГУВАННЯ потрібне, коли ми в класі-нащадкові переписуємо/перевизначаємо метод предка.
ДЕЛЕГУВАННЯ - спосіб викликати метод з батьківського класу.
ДЕЛЕГУВАННЯ (при наслідуванні) - це необхідність викликати один і той же ж метод одночасно:
наприклад, щоб в дочірнього класу викликався його метод, а потім викликався такий же ж метод, но батьківський.
Для цього існує ф-ія super(), через яку ми звертаємось до батьківського класу і викликаємо його метод:
super().<назва методу батьківського класу>(): super().breathe() - виконуватиме виклик батьківського методу breathe()
ф-ія super() повертає батьківський клас.
У метод батьківського класу передаються ті атрибути, які є спільними для батьківського і дочірнього класів:
super().__init__(name, surname)
# викликаємо батьківський метод __init__, атрибути name, surname є і в батьківському, і в дочірньому класі

При наслідуванні потрібно викликати super().
super() нам дає можливість використовувати атрибути і загалом методи, які у нас будуть в батьківському класі,
без super() ми не зможемо доступатись до атрибутів батьківського класу, визначених в методі __init__.

У нас НЕмає можливості викликати метод breathe() одночасно і в батьківського, і в дочірнього класу -
викликається або один метод, або інший: p.breathe()  або  d.breathe()
Але інколи така потреба є - вона частіше виникає у дочірніх класах.
Ми хочемо, щоб викликався метод breathe() у дочірнього класу,
а тоді одразу викликався метод breathe() у батьківського класу.
І для цього нам потрібна ф-ія super, через неї ми звертаємось до батьківського класу:
в методі дочірнього класу визначити: super().breathe() - виконує виклик батьківського методу breathe()
і в коді викликати дочірній метод, що містить ф-ію super:
p = Person()
d = Doc()
d.breathe()

З наслідуванням використовуються два вбудовані методи:
isinstance() - перевіряє, чи наш об"єкт відноситься до якогось конкретного класу
та
issubclass() - дозволяє перевірити саме наслідування, чи один клас наслідується від іншого класу
"""


class Person:   # parent class

    def breathe(self):
        print("Person can breathe")


class Doc(Person):    # sub-class

    def breathe(self):
        print("Doctor can breathe")
        super().breathe()   # виконує виклик батьківського методу


p = Person()
d = Doc()
d.breathe()
# Doctor can breathe
# Person can breathe


print()
"""
НАЙчастіше делегування застосовується у методі __init__:
При ініціалізації Human отримує імя та прізвище, і ці атрибути ми як правило зберігаємо в екземпляр класу;
Но метод __init__ може бути перевизначеним і у Doctor, 
і різниця між цими двома методами може бути лише в одному атрибуті.
"""


class Human:   # parent class

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def breathe(self):
        print("Person can breathe")


class Doctor(Human):    # sub-class

    def __init__(self, name, surname, age):
        # self.name = name
        # self.surname = surname
        # попередні дві стрічки коду можна замінити на одну:
        super().__init__(name, surname)   # викликаємо батьківський метод __init__
        self.age = age

    def breathe(self):
        print("Doctor can breathe")


p_ = Human('JEP', 'Pushchalo')
d_ = Doctor("Yarka", "Pushchalo", 12)
print(p_.name, p_.surname)
# JEP Pushchalo
print(d_.name, d_.surname, d_.age)
# Yarka Pushchalo 12


print()
class HumanNew:   # parent class

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"HUMAN {self.name} {self.surname}"

    def info(self):
        print('Parent class')
        print(self)


class DoctorNew(HumanNew):    # sub-class

    def __init__(self, name, surname, age):
        super().__init__(name, surname)   # викликаємо батьківський метод __init__
        self.age = age

    def __str__(self):
        return f"DOCTOR {self.name} {self.surname} {self.age}"


h = HumanNew('Ivan', 'Ivanov')
g = DoctorNew('Petro', 'Petrov', 25)
# print(h.name, h.surname)
# print(g.name, g.surname, g.age)
g.info()
# Parent class
# DOCTOR Petro Petrov 25
h.info()
# Parent class
# HUMAN Ivan Ivanov


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# and will have seating_capacity own method
class Vehicle:
    def __init__(self, max_speed=0, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, max_speed=0, mileage=0, seating_capacity=0):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

bus = Bus(100, 200, 300)
print(bus.max_speed, bus.mileage, bus.seating_capacity)
# OUTPUT: 100 200 300
