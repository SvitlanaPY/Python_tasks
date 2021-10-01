"""
Создайте класс Zebra, внутри которого есть метод which_stripe ,
который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"

Пример работы с классом Zebra:
z1 = Zebra()
z1.which_stripe() # печатает "Полоска белая"
z1.which_stripe() # печатает "Полоска черная"
z1.which_stripe() # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe() # печатает "Полоска белая"
"""

class Zebra:
    def __init__(self):
        self.counter = 0

    def which_stripe(self):
        if self.counter % 2 == 0:
            print("Полоска белая")
        else:
            print("Полоска черная")
        self.counter += 1


z1 = Zebra()
z1.which_stripe()  # печатает "Полоска белая"
z1.which_stripe()  # печатает "Полоска черная"
z1.which_stripe()  # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()  # печатает "Полоска белая"