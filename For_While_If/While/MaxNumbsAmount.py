# Задача «Количество элементов, равных максимуму»
# Последовательность состоит из натуральных чисел и завершается числом 0.
# Определите, сколько элементов этой последовательности равны ее наибольшему элементу.

n = -1   # n = -1, щоб зайти в цикл
maxx = 0
amount_of_maxx = 1
while n != 0:
    n = int(input())
    if n > maxx:
        maxx = n
        amount_of_maxx = 1
    elif n == maxx:
        amount_of_maxx = amount_of_maxx + 1
print(amount_of_maxx)
