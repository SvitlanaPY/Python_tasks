# reduce(func, iterable[, initial])
# reduce применяет функцию двух аргументов кумулятивно к элементам итерируемого,
# необязательно начиная с начального аргумента. Имеет следующий синтаксис:
#
# Где func это функция, к которой кумулятивно применяется каждый элемент iterable,
# а initial необязательное значение, которое помещается перед элементами итерируемого в вычислении и
# служит значением по умолчанию, когда итерируемый объект пуст.
# О reduce() должно быть отмечено следующее:
# 1. func требуется ДВА аргумента, первый из которых является первым элементом в iterable (если initial не указан)
# а второй - вторым элементом в iterable. Если initial указано, то оно становится первым аргументом функции func,
# а первый элемент в iterable становится вторым элементом.
# 2. reduce "уменьшает" iterable до одного значения.
from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers)
print(result)

# Результат, как ожидалось, равен 68.
# reduce берет первый и второй элементы в numbers и передает их соответственно в custom_sum.
# custom_sum вычисляет их сумму и возвращает ее в reduce.
# Затем reduceпринимает этот результат и применяет его в качестве первого элемента к custom_sum и
# принимает следующий элемент (третий) в numbers в качестве второго элемента для custom_sum.
# Он делает это непрерывно (накопительно), пока numbers не будет исчерпан.
#
# Посмотрим, что произойдет, когда я использую необязательное начальное значение initial.
from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers, 10)
print(result)
# Результат, равен 78 потому что reduce изначально использует 10 в качестве первого аргумента для custom_sum.


print()
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
