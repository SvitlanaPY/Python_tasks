"""
Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки.
Формат ввода
Несколько натуральных чисел на одной строке.
Формат вывода
Несколько чисел на одной строке.

Sample Input:
3 7 1 10 8
Sample Output:
***
*******
*
**********
********
"""


listt = list(map(int, input().split()))
for i in listt:
    for j in range(i):
        print('*', end='')
    print()
