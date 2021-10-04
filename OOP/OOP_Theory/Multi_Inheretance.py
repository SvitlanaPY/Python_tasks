"""
МНОЖИННЕ НАССЛІДУВАННЯ - така ситуація, при якій ваш клас наслідується і має кілька батьківських класів
Порядок пошуку методів залежить від порядку, в якому вказані батьківські класи
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

class Person1(Doctor1, Builder1):   # клас Person візьме поведінку з класу Doctor і з класу Builder

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

class Person2(Doctor2, Builder2):   # клас Person візьме поведінку спершу з класу Doctor, а потім з класу Builder
    pass
    # def can_build(self):
    #     print("I am human, I can build")

pp = Person2()
pp.can_build()

"""
Порядок пошуку методів залежить від порядку, в якому вказані батьківські класи, 
і називається MRO = method resolution order
його можна подивитись наступним чином:
<child class>.__mro__  /(print(Person.__mro__))
або
<child class>.mro()   /(print(Person.mro()))

"""
print(Person.__mro__)
# (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>)
print(Person.mro())
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
