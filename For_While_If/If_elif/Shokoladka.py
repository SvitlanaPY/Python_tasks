"""
Задача «Шоколадка»
Шоколадка имеет вид прямоугольника, разделенного на n*m долек.
Шоколадку можно один раз разломить по прямой на две части.
Определите, можно ли таким образом отломить от шоколадки k-долек.
Программа получает на вход три числа: n, m, k и должна вывести YES или NO.

INPUT1:
4
2
6
OUTPUT1: YES

INPUT2:
2
10
7
OUTPUT2:
NO

INPUT3:
5
7
1
OUTPUT3:
NO

INPUT4:
7
4
21
OUTPUT4:
YES

INPUT5:
5
12
100
OUTPUT5:
NO
"""


m = int(input())
n = int(input())
k = int(input())
if (k % m == 0 or k % n == 0) and k <= n * m:
    print('YES')
else:
    print('NO')
