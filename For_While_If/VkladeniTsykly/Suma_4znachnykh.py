"""
Знайти суму всіх 4-значних чисел, сума цифр кожного з яких рівна 20.
"""

summa = 0
for i in range(555, 10000):
    x = i
    s = 0
    while x > 0:
        last = x % 10
        s += last
        x //= 10
    print(i, s)
    if s == 20:
        summa += i
print(summa)
# 569 = 5+6+9 = 20
# 578 = 5+7+8 = 20
# 587 = 5+8+7 = 20
# .....
# summa = 569+578+587+596+659+668+677+686...


# for i in range(10, 101):
#     x = i
#     s = 0
#     while x > 0:
#         last = x % 10
#         s += last
#         x = x // 10
#     print(i, s)
