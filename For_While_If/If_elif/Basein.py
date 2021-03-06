"""
Задача «Яша плавает в бассейне»

Яша плавал в бассейне размером N × M метров и устал.
В этот момент он обнаружил, что находится на расстоянии x метров от одного из длинных бортиков
(не обязательно от ближайшего) и y метров от одного из коротких бортиков.
Какое минимальное расстояние должен проплыть Яша, чтобы выбраться из бассейна на бортик?

Программа получает на вход числа N, M, x, y.

Программа должна вывести число метров, которое нужно проплыть Яше до бортика.

INPUT1: 23 52 8 43
OUTPUT1: 8

INPUT2: 71 26 21 42
OUTPUT2: 5
"""


n = int(input())
m = int(input())
x = int(input())    # відстань до довгого бортіка
y = int(input())    # відстань до короткого бортіка
if n > m:
    n, m = m, n         # змінні m та n міняються значеннями
    # t = n   n = m   m = t
d = n - x
s = m - y
if x < d:
    min1 = x
else:
    min1 = d
if y < s:
    min2 = y
else:
    min2 = s
if min1 < min2:
    print(min1)
else:
    print(min2)
