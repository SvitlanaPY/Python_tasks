# Дано трехзначное число. Найдите сумму его цифр.
# x = int(input())
x = 179
a = x % 10          # знаходимо одиниці
# print(a)
x2 = x // 10
# print(x2)
b = x2 % 10
# print(b)
c = x2 // 10
# print(c)
summ = a + b + c
print(summ)
