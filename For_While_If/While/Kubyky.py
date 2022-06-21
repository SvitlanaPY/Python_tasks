"""
"Ваня и кубики"
Ване на день рождения подарили n кубиков. Он с друзьями решил построить из них пирамиду.
Ваня хочет построить пирамиду следующим образом: на верхушке пирамиды должен находиться 1 кубик,
на втором уровне — 1+2=3 кубика, на третьем — 1+2+3=6 кубиков, и так далее.
Таким образом, на i-м уровне пирамиды должно располагаться 1+2+...+(i-1)+i кубиков.
Ваня хочет узнать, пирамиду какой максимальной высоты он может создать с использованием имеющихся кубиков.

Входные данные
В первой строке записано целое число n (1≤n≤104) — количество кубиков, подаренных Ване.
Выходные данные
Выведите единственной строкой максимально возможную высоту пирамиды.

Sample Input 1:
1
Sample Output 1:
1

Sample Input 2:
25
Sample Output 2:
4

Sample Input 3:
4
Sample Output 3:
2

Sample Input 4:
3
Sample Output 4:
1
"""


n = int(input())
kub_level = 0
level = 0
summ = 0
while summ <= n:
    level = level + 1
    kub_level = kub_level + level
    summ = summ + kub_level
    print(level, kub_level)
print(level - 1)


# n = int(input())
# level = 1
# cubs_for_level = 0
# total_cubs = 0
# while total_cubs <= n:
#     cubs_for_level += level
#     total_cubs += cubs_for_level
#     level += 1
#
# print(level - 2)
