"""
Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит сообщение о том,
являются ли эти клетки одного цвета. Столбцы на шахматной доске обозначаются английскими строчными буквами.

Программа должна выводить YES, когда клетки одного цвета, NO - разного.
Гарантируется, что значение колонок это латинские буквы abcdefgh, а строки это символы цифр от 1-8

Sample Input 1:
a1
b2
Sample Output 1:
YES

Sample Input 2:
f5
c3
Sample Output 2:
NO
"""

s = 'abcdefgh'
a = input()
b = input()
a1 = (s.index(a[0]) + int(a[1])) % 2
b1 = (s.index(b[0]) + int(b[1])) % 2

if a1 == b1:
    print("YES")
else:
    print("NO")

#
# str_ = '_abcdefgh'
# coord_1 = input()     # 'a3'
# letter = coord_1[0]   # a
# column_1 = str_.find(letter)   # 1
# row_1 = int(coord_1[1])   # 3
# print(row_1, column_1)    # 3 1
# coord_2 = input()     # 'f4'
# letter2 = coord_2[0]   # 4
# column_2 = str_.find(letter2)   # 6
# row_2 = int(coord_2[1])   # 4
# print(row_2, column_2)    # 4 6
#
# if ((row_1 + column_1) % 2 == 0 and (row_2 + column_2) % 2 == 0) or ((row_1 + column_1) % 2 == 1 and (row_2 + column_2) % 2 == 1):
#     print("YES")
# else:
#     print("NO")
#
# if (row_1 + column_1) % 2 == (row_2 + column_2) % 2:
#     print("YES")
# else:
#     print("NO")

# if ((column_1 % 2 == 0 and row_1 % 2 == 0) and (column_2 % 2 == 0 and row_2 % 2 == 0)) \
#         or ((column_1 % 2 == 0 and row_1 % 2 == 0) and (column_2 % 2 == 1 and row_2 % 2 == 1)) \
#         or ((column_1 % 2 == 1 and row_1 % 2 == 1) and (column_2 % 2 == 1 and row_2 % 2 == 1)) \
#         or ((column_1 % 2 == 1 and row_1 % 2 == 1) and (column_2 % 2 == 0 and row_2 % 2 == 0)):
#     print("YES")
# else:
#     print("NO")
