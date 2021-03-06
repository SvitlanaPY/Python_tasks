#Задача «Числа Фибоначчи»
# Последовательность Фибоначчи определяется так:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
# По данному числу/номеру n определите n-е число Фибоначчи φn.
# Эту задачу можно решать и циклом for.

# кожне наступне число дорівнює сумі двох попередніх:
# res:     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ...
# elem_№:  0  1  2  3  4  5  6  7   8   9   10  11  12   13   14   15 ...

n = int(input())   # номер фібоначі (вивести число фібоначі, що відповідає введеному номеру)
i = 2       # для збереження номеру числа Фібоначі
pp = 0      # element before previous; нулевое число Фибоначи
p = 1       # previous element; первое число Фибоначи
res = 1    # current element; n-е число Фибоначчи φn
while i <= n:
    res = p + pp
    pp = p
    p = res
    i += 1
if n == 0:
    res = 0
if n == 1:
    res = 1
print(res)
