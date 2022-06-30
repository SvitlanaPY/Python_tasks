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


for i in range(10, 101):
    x = i
    s = 0
    while x > 0:
        last = x % 10
        s += last
        x = x // 10
    print(i, s)
