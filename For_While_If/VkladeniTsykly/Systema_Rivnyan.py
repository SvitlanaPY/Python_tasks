"""
Система уравнений

Фурик очень любит уроки математики, поэтому, в отличие от Рубика, он их не посещает.
Но теперь Фурик хочет получить хорошую оценку по математике.
Для этого Лариса Ивановна, учительница математики, дала ему новое задание.
Фурик сразу же решил эту задачу, а вы сможете?

Задана система уравнений:
а**2 + b = n
b**2 + a = m
Нужно посчитать количество пар целых чисел (a,b) (0≤a,b), которые удовлетворяют системе.

Входные данные
В единственной строке заданы два целых числа n,m (1≤n,m≤1000) — параметры системы.
Числа в строке разделены пробелом.
Выходные данные
В единственную строку выведите ответ на задачу.
Решение youtube patreon boosty
Sample Input 1:
9 3
Sample Output 1:
1
Sample Input 2:
14 28
Sample Output 2:
1
Sample Input 3:
4 20
Sample Output 3:
0
"""

n, m = map(int, input().split())
print(n, m)
k = 0
for a in range(n + 1):   # n**0.5+1
    for b in range(m + 1):   # m**0.5+1
        if a ** 2 + b == n and a + b ** 2 == m:
            k += 1
print(k)
