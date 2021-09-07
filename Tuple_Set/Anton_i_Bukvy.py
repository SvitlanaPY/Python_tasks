# "Антон и буквы"
# Недавно у Антона появилось множество, состоящие из маленьких латинских букв.
# Он аккуратно выписал все буквы, которые в него входят в одну строку через запятую.
# Для красоты он так же добавил в начало этой строки открывающуюся фигурную скобку, а в конец — закрывающуюся.
#
# К сожалению, Антон иногда забывал, что уже записал некоторую букву, и выписывал ее снова.
# Он просит вас посчитать общее число различных букв в его множестве.
#
# Входные данные
# В первой и единственной строке задано описание множества букв.
# Длина строки не превышает 1000.
# Гарантируется, что строка начинается с открывающейся фигурной скобки, а заканчивается закрывающейся.
# Между ними через запятую перечислены маленькие латинские буквы. После каждой запятой следует пробел.
# Выходные данные
# Выведите единственное число — количество различных букв в множестве Антона.
#
# Sample Input 1:
# {a, b, c}
# Sample Output 1:
# 3
#
# Sample Input 2:
# {b, a, b, a}
# Sample Output 2:
# 2
#
# Sample Input 3:
# {}
# Sample Output 3:
# 0

s = input()
# print(s, type(s))
set_ = set()
for i in s:
    if i.isalpha():
        set_.add(i)
print(len(set_))