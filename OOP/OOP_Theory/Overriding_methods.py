"""
ЯК перевизначати бітьківські методи:
Щоб перевизначити метод батьківського класу, потрібно в дочірньому класі створити метод з такою ж назвою і
всередині нього визначити зовсім іншу поведінку.
"""

class Person:   # parent class

    def breathe(self):
        print("Person can breathe")

    def walk(self):
        print('Person can walk')


class Doctor(Person):    # sub-class
    pass


p = Person()
d = Doctor()

p.breathe()   # оскільки об"єкт р належить до класу Person, то він буде шукати метод breathe() в своєму класі Person,
# знайде його і відпрацює:
# Person can breathe
d.breathe()   # метод d належить класу Doctor і він буде шукати всередині себе метод breathe(),
# всередині себе НЕ знаходить такого методу breathe(), але знаходить його в батьківському класі і відпрацьовує:
# Person can breathe


"""
Але ми можемо перевизначити метод breathe() всередині дочірнього класу Doctor:
створивши метод з такою ж назвою, але із зовсім іншою поведінкою в методі
"""
class Human:   # parent class

    def breathe(self):
        print("Human can breathe")

    def walk(self):
        print('Human can walk')


class Doc(Human):    # sub-class
    def breathe(self):
        print("Doctor can also breathe")


pp = Human()
dd = Doc()

pp.breathe()   # оскільки об"єкт рр належить до класу Human, то він буде шукати метод breathe() в своєму класі Human,
# знайде його і відпрацює:
# Human can breathe
dd.breathe()   # об"єкт dd належить до класу Doc, то він буде шукати спершу всередині себе метод breathe(), і якщо є - то  відпрацює його
# Doctor can also breathe

