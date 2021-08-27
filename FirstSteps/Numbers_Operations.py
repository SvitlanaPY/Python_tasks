# (1)
# num1 = int(input())
# num2 = int(input())
# summ1 = num1 + num2
# print("SUM1=", summ1)
#
# (2)
"""
Sample Input 2:
3.6
80
Sample Output 2:
288.0
"""
# num1 = float(input())
# num2 = float(input())
# S = num1 * num2
# print(S)
#
# (3)
"""Напишите программу, переводящую введенное количество сантиметров в метры.
Sample Input:
845
Sample Output:
8.45
"""
# sm = float(input())
# metr = sm / 100
# print(metr)
#
# (4)
"""
Допустим, перед вами встала задача вычислить кинетическую энергию тела, зная его массу и скорость по формуле:
E = (m*(v**2))/2
Sample Input:
10
3
Sample Output:
45.0
"""
# m = float(input())
# v = float(input())
# E = (m*(v**2))/2
# print(E)
#
# (5)
"""
Возможно, вам интересно, сколько секунд содержится в одном году или, 
например, в жизни человека (взяв среднюю продолжительность жизни в 70 лет).
Формат ввода: целое число — количество лет. Считайте, что в году 365 дней, т. е. год не високосный.
Формат вывода: целое число — количество секунд.
Sample Input:
12
Sample Output:
378432000"""
# age = int(input())
# life_sec = age * (365 * 24 * 60 * 60)
# print(life_sec)
#
# (6)
"""
С клавиатуры вводится натуральное число. Вам необходимо вывести последнюю цифру этого числа.
Sample Input:
125471479
Sample Output:
9
"""
# n = int(input())
# last_number = n % 10
# print(last_number)
#
# (7)
"""
С клавиатуры вводится целое число — количество минут, прошедшее с начала суток. 
Выведите на экран привычное представление времени (часы и минуты через пробел).
Sample Input:
320
Sample Output:
5 20
"""
# n = int(input())
# h = n // 60
# minutes = n % 60
# print(h, minutes)
#
# (8)
"""С клавиатуры вводится натуральное число, затем на другой строке число n <= длины числа. 
Выведите на экран последние n цифр числа.
Sample Input:
1728
3
Sample Output:
728
"""
# input_ = int(input())
# n = int(input())
# output_ = input_ % (10 ** n)
# print(output_)
#
# (9)
"""
Вводится трехзначное число n. Выведите на экран сумму кубов его цифр.
Sample Input:
692
Sample Output:
953
"""
# n = input()
# summ = 0
# for i in range(len(n)):
#     x = int(n[i]) ** 3
#     summ = summ + x
# print(summ)
#
# (10)
"""
Операторы сравнения часто применяются в связке с условными конструкциями, 
однако уже сейчас вы можете практиковаться в их использовании. На вход программе подаются две строки. 
Выведите True, если они НЕ равны и False в обратном случае.
Sample Input:
Lorem ipsum dolor sit amet, consectetur adipiscing elit
Lorem ipsum dolor sit amet, consectetur id felis bibendum fringilla
Sample Output:
True
"""
stroka1, stroka2 = input(), input()
res = stroka1 != stroka2
print("stroka1 НЕ рівна stroka2? ", res)
