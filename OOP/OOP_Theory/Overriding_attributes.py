"""
ЯК перевизначати батьківські атрибути:
Щоб перевизначити атрибут(и) батьківського класу, потрібно в дочірньому класі створити атрибут(и) з такою ж назвою і
дати атрибуту(ам) інше значення.
"""


class Person:   # parent class

    name = 'Adam'

    def breathe(self):
        print("Person can breathe")

    def walk(self):
        print('Person can walk')


class Doctor(Person):    # sub-class

    def breathe(self):
        print("Doctor can also breathe")


p = Person()
d = Doctor()

print(p.name, d.name)
# Adam Adam
# Python намагається знайти всередині класу Doctor атрибут з іменем name, він його НЕ знаходить і іде в батьківський клас
# де є цей атрибут і отже виводить значення цього атрибуту


"""
Але ми можемо перевизначити атрибут name всередині дочірнього класу Doc:
створивши атрибут з такою ж назвою, але із зовсім іншоим значенням
"""

class Human:  # parent class

    name = 'Adam'

    def breathe(self):
        print("Human can breathe")

    def walk(self):
        print('Human can walk')


class Doc(Human):  # sub-class

    name = 'Jep'

    def breathe(self):
        print("Doc can also breathe")


pp = Human()
dd = Doc()

print(pp.name, dd.name)
# Adam Jep
