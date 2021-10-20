"""
magic methods = dunder methods (Double UNDERscore) -
це спеціальні методи, які починаються і закінчуються на два нижніх підкреслення.
Ці методи мають певний функціонал і викликаються всередині класу у певний момент.

об"єкти/екземпляри класу НЕ підтримують математичних бінарних операцій (+, *, /, -) !
When we multiply two objects with binary ‘*’ operator - it throws an error,
because compiler don’t know how to multiply two objects.

The same error happens when we multiply other types with class object.

У всіх бінарних операціях з об"єктами - у першого об"єкту (лівого) викликається відповідний магічний метод,
і в цей мегічний метод у якості параметру підставляється інший об"єкт.
a1 * a2 = a1.__mul__(a2)
"""

"""
Перевизначимо метод __add__, щоб можна було додавати  об"єкт + інт/float
а також  об"єкт + об"єкт
"""


class BankAccount1:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __mul__(self, other):
        print('__mul__ called')

        # щоб можна було перемножати об"єкт на об"єкт
        if isinstance(other, BankAccount1):
            return self.balance * other.balance

        # щоб можна було перемножати об"єкт на інт/float
        if isinstance(other, (int, float)):
            return self.balance * other

        if isinstance(other, str):
            return self.name + other

        raise NotImplemented


bb = BankAccount1('Mike', 20)
print("balance: ", bb * 10)  # 78 * 12
# __add__ called
# balance:  90
tt = BankAccount1('Tanya', 2)
print("перемножаємо ДВА ОБЄКТИ: ", bb * tt)
print(bb * "еееееккк")
