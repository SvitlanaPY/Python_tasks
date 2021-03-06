# Система регистрации
# В скором времени в Берляндии откроется новая почтовая служба "Берляндеск".
# Администрация сайта хочет запустить свой проект как можно быстрее, поэтому они попросили Вас о помощи.
# Вам предлагается реализовать прототип системы регистрации сайта.
#
# Система должна работать по следующему принципу.
# Каждый раз, когда новый пользователь хочет зарегистрироваться, он посылает системе запрос name со своим именем.
# Если данное имя не содержится в базе данных системы, то оно заносится туда и пользователю возвращается ответ OK,
# подтверждающий успешную регистрацию.
# Если же на сайте уже присутствует пользователь с именем name,
# то система формирует новое имя и выдает его пользователю в качестве подсказки,
# при этом подсказка также добавляется в базу данных.
# Новое имя формируется по следующему правилу.
# К name последовательно приписываются числа, начиная с единицы (name1, name2, ...),
# и среди них находят такое наименьшее i, что namei не содержится в базе данных сайта.
#
# Входные данные
# В первой строке входных данных задано число n (1≤n≤105).
# Следующие n строк содержат запросы к системе.
# Каждый запрос представляет собой непустую строку длиной не более 32 символов,
# состоящую только из строчных букв латинского алфавита.
#
# Выходные данные
# В выходных данных должно содержаться n строк — ответы системы на запросы:
# OK в случае успешной регистрации, или подсказку с новым именем, если запрашиваемое уже занято.

# Sample Input 1:
# 4
# abc
# abcd
# abc
# acab
# Sample Output 1:
# OK
# OK
# abc1
# OK

# Sample Input 2:
# 3
# b
# b
# b
# Sample Output 2:
# OK
# b1
# b2

# Sample Input 3:
# 4
# abacaba
# acaba
# abacaba
# acab
# Sample Output 3:
# OK
# OK
# abacaba1
# OK

# Sample Input 4:
# 6
# first
# first
# second
# second
# third
# third
# Sample Output 4:
# OK
# first1
# OK
# second1
# OK
# third1

n = int(input())
d = {}
i = 1
for i in range(1, n + 1):
    number = 1
    name = input()
    if name not in d.values():
        d.setdefault(i, name)
        print('OK')
    else:
        name_new = name + str(number)
        while name_new in d.values():
            number += 1
            name_new = name + str(number)
        d.setdefault(i, name_new)
        print(name_new)
    # i += 1


# (2):
# n = int(input())
# d = {}
# for i in range(n):
#     x = input()
#     d.setdefault(x, 0)
#     if d[x] == 0:
#         print('OK')
#     else:
#         print(x, str(d[x]), sep='')
#     d[x] += 1

# (3):
# logins = {}
# n = int(input())
# for i in range(n):
#     login = input()
#     if login in logins:
#         print(f"{login}{logins[login]}")
#         logins[login] += 1
#     else:
#         print("OK")
#         logins[login] = 1
