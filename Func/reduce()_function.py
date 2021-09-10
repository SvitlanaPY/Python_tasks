lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
from functools import reduce
def summ_elements(x1, x2):
    return x1 + x2
print(reduce(summ_elements, lst_to_sort))
# OUTPUT: 164

# (2):
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
sum = functools.reduce(lambda x, y: x + y, lst_to_sort)
print(sum)