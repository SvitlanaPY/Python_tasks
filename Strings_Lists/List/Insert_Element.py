'''
Задача «Вставить элемент»
Дан список целых чисел, число k и значение C.
Необходимо вставить в список на позицию с индексом k элемент, равный C, сдвинув все элементы,
имевшие индекс не менее k, вправо.
Поскольку при этом количество элементов в списке увеличивается,
после считывания списка в его конец нужно будет добавить новый элемент, используя метод append.
Вставку необходимо осуществлять уже в считанном списке,
не делая этого при выводе и не создавая дополнительного списка.
'''

lst = [int(i) for i in input("Enter numbers (7 6 5 4 3 2 1): ").split()]
print(lst)
K, C = [int(i) for i in input("Enter numbers (2 0): ").split()]
print("index=", K, "elem=", C)
lst.append(C)
print("updated lst:", lst)
print("Length of updated lst: ", len(lst))
for i in range(len(lst)-1, K, -1):
    lst[i] = lst[i-1]
print("shifted lst: ", lst)
lst[K] = C
# lst[KC[0]] = KC[1]
print(' '.join([str(i) for i in lst]))
