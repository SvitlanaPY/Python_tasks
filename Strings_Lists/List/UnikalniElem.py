"""
Дан список чисел. 
Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""
a = [int(i) for i in input("Enter few numbers (1 2 2 3 5 3 3 4 2): ").split()]
for i in range(0, len(a)):
    is_pair = 0
    for j in range(0, len(a)):
        if i != j and a[i] == a[j]:
                is_pair = 1
    if is_pair == 0:
        print(a[i], end=' ')
