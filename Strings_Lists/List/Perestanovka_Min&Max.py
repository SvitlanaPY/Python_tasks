"""
В списке все элементы различны.
Поменяйте местами минимальный и максимальный элемент этого списка.
"""

# a = list(map(int, input("Enter (3 4 5 2 1): ").split()))
a = [int(i) for i in input("Enter (3 4 5 2 1): ").split()]
index_maxx = a.index(max(a))
print("index_maxx= ", index_maxx)
index_minn = a.index(min(a))
print("index_minn= ", index_minn)
a[index_maxx], a[index_minn] = a[index_minn], a[index_maxx]
print(' '.join([str(i) for i in a]))
# for i in a:
#     print(i)
