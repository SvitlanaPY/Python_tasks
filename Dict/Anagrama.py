# "Анаграмма"
# Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
# Программа получает на вход две строки S1 и S2.
# Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO
#
# Sample Input 1:
# abc
# cba
# Sample Output 1:
# YES
#
# Sample Input 2:
# abracadabra
# cadabraabra
# Sample Output 2:
# YES
#
# Sample Input 3:
# abb
# bbc
# Sample Output 3:
# NO


s1 = input().lower()
d1 = {}
for elem in s1:
    d1[elem] = d1.get(elem, 0) + 1

s2 = input().lower()
d2 = {}
for elem in s2:
    d2[elem] = d2.get(elem, 0) + 1

if d1 == d2:
    print('YES')
else:
    print('NO')
