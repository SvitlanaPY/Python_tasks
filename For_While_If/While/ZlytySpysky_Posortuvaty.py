"""
"Слияние списков"
В вашем распоряжении имеется два отсортированных списка по неубыванию элементов, состоящих из n и m элементов
Ваша задача слить их в один отсортированный список размером  n + m

Входные данные
Программа получает на вход два числа n и m - количество элементов первого списка и второго списков
Затем с новой строки поступают элементы первого отсортированного списка, а со следующей строки - второго списка
Выходные данные
Слить два списка в один в порядке неубывания и вывести элементы полученного списка
P.S: пользоваться встроенной сортировкой запрещено

Sample Input 1:
2 3
3 9
2 3 6
Sample Output 1:
2 3 3 6 9

Sample Input 2:
3 5
2 8 8
3 4 5 5 10
Sample Output 2:
2 3 4 5 5 8 8 10

Sample Input 3:
2 5
3 7
1 1 3 6 8
Sample Output 3:
1 1 3 3 6 7 8
"""

a, b = map(int, input().split())
n = list(map(int, input().split()))
m = list(map(int, input().split()))
s = n + m
while len(s) != 0:
    minn = s.index(min(s))
    print(s.pop(minn), end=' ')


# n, m = map(int, input().split())
# lst_1 = list(map(int, input().split()))
# lst_2 = list(map(int, input().split()))
# lst_1_2 = lst_1 + lst_2
# lst_new = []
# while len(lst_1_2) != 0:
#     min_item = min(lst_1_2)
#     lst_new.append(min_item)
#     lst_1_2.remove(min_item)
# print(*lst_new)


# a, b = map(int, input().split())
# n = list(map(int, input().split()))
# m = list(map(int, input().split()))
# s = n + m
# ss = []
# while len(s) != 0:
#     ss.append(min(s))
#     index_minn = s.index(min(s))
#     s.pop(index_minn)
# print(*ss)
