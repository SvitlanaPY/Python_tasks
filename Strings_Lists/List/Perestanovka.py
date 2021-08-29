# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
# Если элементов нечетное число, то последний элемент остается на своем месте.
# a = input("Enter numbers (1 2 3 4 5): ").split()
# print(a)
# i = 0
# while i < len(a)-1:
#     a[i], a[i + 1] = a[i + 1], a[i]
#     i = i + 2
# print(' '.join(a))


# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
a = [int(i) for i in input("Enter (3 4 5 2 1): ").split()]
index_maxx = a.index(max(a))
print("index_maxx= ", index_maxx)
index_minn = a.index(min(a))
print("index_minn= ", index_minn)
a[index_maxx], a[index_minn] = a[index_minn], a[index_maxx]
print(' '.join([str(i) for i in a]))
# for i in a:
#     print(i)
