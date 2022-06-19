"""
Программа принимает на вход два слова s и t. 
Если слово t является словом s, записанным наоборот, выведите YES, иначе выведите NO.

Слова состоят из маленьких латинских букв.
Входные данные не содержат лишних пробелов.
Слова непустые, и их длины не превосходят 100 символов.

Sample Input 1:
avtor
rotva
Sample Output 1:
YES

Sample Input 2:
aba
abb
Sample Output 2:
NO
"""

s, t = input(), input()
if s[::-1] in t:
    print('YES')
else:
    print('NO')


# s, t = input(), input()
# if s[::-1] == t[:]:
#     print('YES')
# else:
#     print('NO')


# s = list(map(str, input())
# t = list(map(str, input())
# t.reverse()
# if s == t:
#     print("YES")
# else:
#     print('NO')
