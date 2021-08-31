# ЛІНІЙНИЙ алгоритм пошуку дільників числа
# лінійний, бо час виконання лінійний - к-сть циклів виконання залежить від змінної n
# (якщо n = 20, то цикл буде виконуватись 20 раз)
# n = int(input())
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i, end=' ')
#     i += 1


# це теж лінійний алгоритм, але чуть ефективнійший (пошук скорочено вдвічі)
# n = int(input())
# i = 1
# while i <= n // 2:
#     if n % i == 0:
#         print(i, end=' ')
#     i += 1
# print(n)



n = int(input())
a = 1
lst_ = []
while a <= n ** 0.5:   # або a ** 2 <= n;  або a * a <= n
    if n % a == 0:
        if a == n // a:
            lst_.append(a)
            # print(a)
        else:
            lst_.append(a)
            lst_.append(n // a)
            # print(a, n // a)
    a += 1
lst_.sort()
print(lst_)
