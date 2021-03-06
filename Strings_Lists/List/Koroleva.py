"""
Задача «Ферзи»/"королева"
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей.
Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
НЕ б"ють якщо: x1 != x2; y1 != y2; |x2 - x1| != |y2 - y1|

# INPUTS:
# 1 7
# 2 4
# 3 2
# 4 8
# 5 6
# 6 1
# 7 3
# 8 5
"""


n = 8
x = []   # x = [0] * 8
y = []   # y = [0] * 8
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)
flag = 0
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            flag = 1
if flag == 1:
    print('YES')   # так, б"ють
else:
    print('NO')

