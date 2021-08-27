# пріоритет операцій:
# 1.(), 2.**, 3.(*, /, //, %), 4.(+, -)

# ()
# val1 = 2 % 7
# print("2 % 7 = ", val1)   # 0*7+2

# ()
# val2 = 19 % 7
# print("19 % 7 = ", val2)   # 2*7+5

# ()
# num1 = int(input())
# num2 = int(input())
# summ1 = num1 + num2
# print("SUM1=", summ1)
#
# ()
# print(pow(3, 2))   # =9
#
# ()
# print("round(3.5)=", (round(3.5)), "round(3.4)=", (round(3.4)))   # round(3.5)= 4 round(3.4)= 3
# print("round(3.456)=", (round(3.456, 2)))   # round(3.456)= 3.46
# print("round(456)=", (round(456, -1)))   # 456 ближче до 450 чи до 460?  =460
# print("round(453)=", (round(453, -1)))   # 453 ближче до 450 чи до 440?  =450
# print("round(456)=", (round(456, -2)))   # 456 ближче до 400 чи до 500?  =500
print(9**(1/2))   # =3.0: квадратний корінь з 9
print(round(729**(1/3)))   # =9: кубічний корінь з 729
# ()
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
# ()
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
# ()
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
# ()
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
# ()
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
# ()
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
# ()
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
# ()
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
# ()
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
# stroka1, stroka2 = input(), input()
# res = stroka1 != stroka2
# print("stroka1 НЕ рівна stroka2? ", res)
