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
        self.lines = ['Полоска белая', 'Полоска черная']
        self.state = 0

    def which_stripe(self):
        if self.state == 0:
            self.state = 1
            print(self.lines[0])
        else:
            self.state = 0
            print(self.lines[1])


z1 = Zebra()
z1.which_stripe()  # печатает "Полоска белая"
z1.which_stripe()  # печатает "Полоска черная"
z1.which_stripe()  # печатает "Полоска белая"

z2 = Zebra()
z2.which_stripe()  # печатает "Полоска белая"
