"""
__getitem__ - магічний метод, який викликається, коли ми намагаємось звернутись до об"єкту, як до масиву по індексу.
Масивом може бути список, словник, стрічка.
__getitem__(self, item) - приймає параметр item, що є індексом масиву.

Для зміни елементу колекції по індексу використовується магічний метод __setitem__.
__setitem__(self, key, value) - приймає два параметри (key та value):
key (є індексом масиву) та
value (нове значення, яке ми хочемо присвоїти елементу масиву по вказаному індексу)

__delitem__ - викликається, якщо ми хочемо видалити елемент масиву по індексу.
__delitem__(self, key) - приймає параметр key, що є індексом масиву.

"""

class Vector:

    def __init__(self, *args):
        self.listt = list(args)

    def __repr__(self):
        return str(self.listt)

    def __getitem__(self, item):
        if 0 <= item < len(self.listt):
            return self.listt[item]
        else:
            raise IndexError("Індекс поза межами нашої колекції")

    def __setitem__(self, key, value):
        if 0 <= key < len(self.listt):
            self.listt[key] = value
        else:
            raise IndexError("Індекс поза межами нашої колекції")

    def __delitem__(self, key):
        if 0 <= key < len(self.listt):
            del self.listt[key]
        else:
            raise IndexError("Індекс поза межами нашої колекції")


v1 = Vector(25, 11, 22, 3, 4, 55, 67)
print(v1[1])
v2 = Vector(10, 22, 44, 33, 55)
print(v2[0])
v2[0] = 100
print(v2[0])
v3 = Vector(26, 62, 85, 74, 20, 98)
print(v3, v3[3])
del v3[3]
print(v3)


class Vector_1:

    def __init__(self, *args):
        self.listt = list(args)

    def __repr__(self):
        return str(self.listt)

    def __getitem__(self, item):
        if 1 <= item <= len(self.listt):
            return self.listt[item-1]
        elif item > len(self.listt):
            diff = item - len(self.listt)
            self.listt.extend([0] * diff)
            return self.listt[item-1]
        else:
            raise IndexError("Індекс поза межами нашої колекції")

    def __setitem__(self, key, value):
        if 1 <= key <= len(self.listt):
            self.listt[key-1] = value
        elif key > len(self.listt):
            diff = key - len(self.listt)
            self.listt.extend([0]*diff)
            self.listt[key-1] = value
        else:
            raise IndexError("Індекс поза межами нашої колекції")

    def __delitem__(self, key):
        if 1 <= key <= len(self.listt):
            del self.listt[key]
        else:
            raise IndexError("Індекс поза межами нашої колекції")


vv1 = Vector_1(12, 10, 9, 7, 17)
print(vv1)
print(vv1[10])
print(vv1)
vv1[10] = 100
print(vv1[10])
