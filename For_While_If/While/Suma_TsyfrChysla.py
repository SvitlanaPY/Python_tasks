"""
Програма приймає на вхід одне натуральне число і виводить на екран суму цифр даного числа.

"""
x = int(input())
summ = 0
while x > 0:
    last_num = x % 10
    summ += last_num
    x = x // 10
print(summ)
