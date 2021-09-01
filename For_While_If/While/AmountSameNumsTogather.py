# Задача «Максимальное число идущих подряд равных элементов»
# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу.

n = int(input())
previous_n = n
maxx_amount = 1
amount = 1

while n != 0:
    n = int(input())
    if n == previous_n:
        amount = amount + 1
    else:   # виконується тоді, коли ми переходимо з одної пачки на іншу: n != previous_n
        if amount > maxx_amount:
            maxx_amount = amount
        amount = 1
    previous_n = n
print(maxx_amount)
