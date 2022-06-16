# Дана строка. Разрежьте ее на две равные части (если длина строки — четная, а если длина строки нечетная,
# то длина первой части должна быть на один символ больше).
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

from math import *
# s = input()
s = 'asdfghjzxc'
length = len(s)
# print(length)
length1 = ceil(length / 2)  # length of the first part
# print(length1)
s_new = s[length1:] + s[:length1]
print(s_new)   # hjzxcasdfg
