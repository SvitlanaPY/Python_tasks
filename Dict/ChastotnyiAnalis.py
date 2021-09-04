# Задача «Частотный анализ»
# Дан текст: в первой строке записано количество строк в тексте, а затем сами строки.
# Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке.
#
# Указание. После того, как вы создадите словарь всех слов,
# вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов:
# частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
# Тогда стандартная сортировка будет сортировать список кортежей,
# при этом кортежи сравниваются по первому элементу, а если они равны — то по второму.
# Это почти то, что требуется в задаче.

# Inputs1:
# 9
# hi
# hi
# what is your name
# my name is bond
# james bond
# my name is damme
# van damme
# claude van damme
# jean claude van damme
# Outputs1:
# damme
# is
# name
# van
# bond
# claude
# hi
# my
# james
# jean
# what
# your

# Inputs2:
# 2
# iovjxotfvt h h iovjxotfvt h iovjxotfvt iovjxotfvt h
# h iovjxotfvt
# Outputs2:
# h
# iovjxotfvt

n = int(input())
d = {}
for i in range(n):
    text = input().split()
    for word in text:
        d[word] = d.get(word, 0) + 1
# print(d)
lst = []
# lst1= []
for key, val in d.items():
    lst.append([-val, key])   # или lst.append((-val, key))
#     lst1.append([val, key])
# print(sorted(lst))
# print(sorted(lst1, reverse = True))
lst_new = sorted(lst)   # или lst.sort()
#print(lst_new)
for i in lst_new:    # или for i in lst:
    print(i[1])
