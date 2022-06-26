"""
Метод підрахунку для сортування

Скільки разів будь-яке значення зустрічалось в нашому списку
"""

# s = 'abczjhdf aaajgkfYGg 543 *(!@$&*((__|} asdwe'
# letters = [0] * 26
# for i in s.lower():
#     if i.isalpha():   # if 'a' <= i <= 'z':
#         nomer = ord(i) - 97
#         letters[nomer] += 1
# print(letters)
# # [5, 1, 1, 2, 1, 2, 3, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1]
#
# for i in range(26):
#     if letters[i] > 0:
#         print(chr(i + 97) * letters[i], end='')
# # aaaaabcddeffggghjjkswyz


a = []
from random import randint
for i in range(10):
    a.append(randint(-10, 10))
    # -10 до 10: -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # всього у проміжку від -10 до 10 є 21 можливих числа
print(a)
count = [0] * 21
for i in a:
    nomer = i + 10
    count[nomer] += 1

for i in range(21):
    if count[i] > 0:
        print(i - 10, count[i])
        # print((str(i - 10) + ' ') * count[i], end='')

# aa = [1, 2, 5, 4, 3, 2, 0, 6, 1, 5, 1]
# count = [0] * (max(aa) + 1)
# for i in aa:
#     count[i] += 1
# print(count)
# for i in range(max(aa)+1):
#     if count[i] > 0:
#         print(i, count[i])
