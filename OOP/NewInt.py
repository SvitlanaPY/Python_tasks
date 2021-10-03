"""
Создайте класс NewInt, который унаследован от целого типа int, то есть мы будем унаследовать поведение целых чисел
и значит экземплярам нашего класса будут поддерживать те же операции, что и целые числа.

Дополнительно в классе NewInt нужно создать:

- метод repeat, который принимает одно целое положительное число n (по умолчанию равное 2),
обозначающее сколько раз нужно продублировать данное число.
Метод repeat должен возвращать новое число, продублированное n раз (см пример ниже);
- метод to_bin, который возвращает двоичное представление числа в виде числа (может пригодиться функция bin)

a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35

# Кстати, как вы думаете, что вернет данный вызов NewInt() ?
"""
import pprint


class NewInt(int):

    def repeat(self, n=2):
        self.n = n
        return int(str(self) * n)

    def to_bin(self):
        return int(bin(self)[2:])
        # return int(format(self, 'b'))   # b = binary format/двійковий формат
        # return int(bin(self).replace('0b', ''))


num = NewInt(9)
print(num.repeat())

d = NewInt(num + 5)
print(d.repeat(3))

b = NewInt(NewInt(7) * NewInt(5))
print(b.to_bin())

# =================================================
print(type(bin(35)))   # <class 'str'>
print(bin(35))   # '0b100011'

# pprint.pprint(dir(num))
