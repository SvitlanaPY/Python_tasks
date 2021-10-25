"""
МНОЖИННЕ НАССЛІДУВАННЯ - така ситуація, при якій ваш клас наслідується і має кілька батьківських класів.
Порядок пошуку методів залежить від порядку, в якому вказані батьківські класи.

З наслідуванням використовуються два вбудовані методи:
isinstance() - перевіряє, чи наш об"єкт відноситься до якогось конкретного класу
та
issubclass() - дозволяє перевірити саме наслідування, чи один клас наслідується від іншого класу

Порядок пошуку методів залежить від порядку, в якому вказані батьківські класи,
і називається MRO = method resolution order
MRO - це така логіка всередині пайтона, яка дозволяє нам визначити порядок,
в якому пайтон буде шукати методи в ієрархії цих класів.

MRO можна подивитись наступним чином:
<child class>.__mro__  /(print(Person.__mro__))
або
<child class>.mro()   /(print(Person.mro()))
"""


class Doctor:
    def can_cure(self):
        print("I am a doctor, I can cure")

class Builder:
    def can_build(self):
        print("I am a builder, I can build")

class Person(Doctor, Builder):   # клас Person візьме поведінку з класу Doctor і з класу Builder
    pass

p = Person()
p.can_cure()
# I am a doctor, I can cure
p.can_build()
# I am a builder, I can build


print()
class Doctor1:
    def can_cure(self):
        print("I am a doctor, I can cure")

class Builder1:
    def can_build(self):
        print("I am a builder, I can build")

class Person1(Doctor1, Builder1):   # клас Person візьме поведінку з класу Doctor1 і з класу Builder1

    def can_build(self):
        print("I am human, I can build")

p_ = Person1()
p_.can_build()
# I am human, I can build


print()
class Doctor2:
    def can_cure(self):
        print("I am a doctor, I can cure")

    def can_build(self):
        print("I am a doctor, but I can build")


class Builder2:
    def can_build(self):
        print("I am a builder, I can build")

class Person2(Doctor2, Builder2):   # клас Person візьме поведінку спершу з класу Doctor2, а потім з класу Builder2
    pass
    # def can_build(self):
    #     print("I am human, I can build")

pp = Person2()
pp.can_build()

"""
Порядок пошуку методів залежить від порядку, в якому вказані батьківські класи, 
і називається MRO = method resolution order
MRO можна подивитись наступним чином:
<child class>.__mro__  /(print(Person2.__mro__))
або
<child class>.mro()   /(print(Person2.mro()))

"""
print(Person2.__mro__)
# (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>)
print(Person2.mro())
# [<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>]


print()
class Doctor3:
    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print("CONGRATS! I have doctor phd.")

    def can_build(self):
        print("I am a doctor, but I can build")


class Builder3:
    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print("CONGRATS! I have architect phd.")

    def can_build(self):
        print("I am a builder, I can build")

class Person3(Doctor3, Builder3):   # клас Person візьме поведінку спершу з класу Doctor3, а потім з класу Builder3
    def __init__(self, rank, degree):
        # self.rank = rank
        # self.degree = degree
        # дві попередні стрічки коду можна записати:
        Doctor3.__init__(self, degree)
        Builder3.__init__(self, rank)

    def __str__(self):
        return f"Person3 has:  {self.rank}, {self.degree}"

pp_ = Person3('rank 5', 'degree spec')
print(pp_)
# Person3 has:  rank 5, degree spec


"""6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus
# and will have its own - bus_school_color"""


class Vehicle:

    def __init__(self, max_speed=0, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage


class School:

    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


class Bus(Vehicle):

    def __init__(self, max_speed=0, mileage=0, seating_capacity=0):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


class SchoolBus(School, Bus):
    def __init__(self, color , get_school_id, number_of_students, max_speed=0, mileage=0, seating_capacity=0):
        super().__init__(get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = color
