# Задача «Лесенка»
# По данному натуральному n ≤ 9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов.

# n = int(input())
# x = 0
# for i in range(1, n+1):
#     x = x * 10 + i
#     print(x)


n = int(input())
x = ''
for i in range(0, n):
    x = x + str(i + 1) + ' '
    print(x)
