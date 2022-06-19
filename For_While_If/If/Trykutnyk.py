"""
Даны три натуральных числа a, b, c записанные в отдельных строках.
Ваша задача определить, существует ли треугольник с такими сторонами.

Для этого вспоминаем теорему о существовании треугольника.
Она утверждает, что треугольник существует, если сумма любых двух сторон больше оставшейся третьей.

Выведите строку YES, если условие теоремы выполняется, иначе выведите строку NO.

Sample Input 1:
3
4
5
Sample Output 1:
YES

Sample Input 2:
2
7
2
Sample Output 2:
NO
"""


A, B, C = int(input()), int(input()), int(input())
if A + B > C and A + C > B and B + C > A:
    print('YES')
else:
    print('NO')
    