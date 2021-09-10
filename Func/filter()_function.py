# filter(function or None, iterable) ---> filter object
# Ф-ія filter() приймає ф-ію, а потім ітерабельну послідовність (списки, кортежі, словники, ф-ія range, строки...):
# і повертає filter-object, який є ітератором,
# і в нього увійдуть лише ті елементи нашої ітерабельної колекції, для яких ф-ія поверне значення True
# отже наша ф-ія, яка передається у filter має повертати True або False
# filter() відфільтрує елементи нашої колекції і залишить лише ті, значення яких буде True
a = [14, 0, 5, 79, 645, 7952, 18, 8, 192, 471]
def f(x):
    return x > 10
b = list(filter(f, a))
print("#1: ", b)
# #1:  [14, 79, 645, 7952, 18, 192, 471]


b = list(filter(lambda x: x>9 and x<100, a))
print("#2: ", b)
# #2:  [14, 79, 18]


b = list(filter(lambda x: x>0 and x<10, range(1, 20)))
print("#3: ", b)
# #3:  [1, 2, 3, 4, 5, 6, 7, 8, 9]


b = list(filter(bool, [14, 0, 5, '', 0, 7952, 0, 8, 192, [], 471]))
print("#4: ", b)
# #4:  [14, 5, 79, 7952, 8, 192, 471]

b = list(filter(lambda x: len(x) > 5, ['hello', 'hi', 'bye', 'potato', 'carrot', 'world']))
print("#5: ", b)
# #5:  ['potato', 'carrot']

c = 'qweRTY567788TNMssdj'
b = list(filter(str.isalpha, c))
print("#6: ", b)
# #6:  ['q', 'w', 'e', 'R', 'T', 'Y', 'T', 'N', 'M', 's', 's', 'd', 'j']
b = list(filter(str.isdigit, c))
print("#7: ", b)
# #7:  ['5', '6', '7', '7', '8', '8']


dict_ = {
    'moscow': 800,
    'boston': 750,
    'LA': 400,
    'SF': 900,
    'Chicago': 650,
    'SP': 600
}
b = list(filter(lambda x: dict_[x] > 700, dict_))   # x = key
print("#8: ", b)
# #8:  ['moscow', 'boston', 'SF']


print()
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
print(list(filter(lambda elem: elem % 2 == 1, lst_to_sort)))
# OUTPUT: [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
print(list(filter(lambda y: y < 0, range(-10, 10))))
# OUTPUT: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
common = list(filter(lambda p: p in list_2, list_1))
print(common)
# OUTPUT: [2, 3, 5, 7]