"""
Задача «Вставить элемент»
Дан список целых чисел, число k и значение C.
Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы,
имевшие индекс не менее k, вправо.
Поскольку при этом количество элементов в списке увеличивается,
после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.
Вставку необходимо осуществлять уже в считанном списке,
не делая этого при выводе и не создавая дополнительного списка.

INPUT1:
7 6 5 4 3 2 1
2 0
OUTPUT1:
7 6 0 5 4 3 2 1

INPUT2:
4 6 2 4 3 5 12 24 3 5
4 22
OUTPUT2:
4 6 2 4 22 3 5 12 24 3 5
"""

a = [int(i) for i in input().split()]
kc = [int(i) for i in input().split()]
a.append(kc[1])
for i in range(len(a)-1, kc[0], -1):
    a[i] = a[i-1]
a[kc[0]] = kc[1]
print(' '.join([str(i) for i in a]))


# lst = list(map(int, input("Enter (3 4 5 2 1): ").split()))
# lst = [int(i) for i in input("Enter numbers (7 6 5 4 3 2 1): ").split()]
# print(lst)
# K, C = [int(i) for i in input("Enter numbers (2 0): ").split()]
# print("index=", K, "elem=", C)
# lst.append(C)
# print("updated lst:", lst)
# print("Length of updated lst: ", len(lst))
# for i in range(len(lst)-1, K, -1):
#     lst[i] = lst[i-1]
# print("shifted lst: ", lst)
# lst[K] = C
# # lst[KC[0]] = KC[1]
# print(' '.join([str(i) for i in lst]))
