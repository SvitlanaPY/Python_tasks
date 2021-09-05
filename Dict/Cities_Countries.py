# Задача «Страны и города»
# Дан список стран и городов каждой страны. Затем даны названия городов.
# Для каждого города укажите, в какой стране он находится.
#
# Inputs1:
# 2
# Russia Moscow Petersburg Novgorod Kaluga
# Ukraine Kiev Donetsk Odessa
# 3
# Odessa
# Moscow
# Novgorod
# Outputs1:
# Ukraine
# Russia
# Russia

n = int(input())
d = {}
for i in range(n):
    cc = input().split()
    key = cc[0]
    d[key] = cc[1:]
print("Dict: ", d)   # Dict:  {'Russia': ['Moscow', 'Petersburg', 'Novgorod', 'Kaluga'], 'Ukraine': ['Kiev', 'Donetsk', 'Odessa']}
m = int(input())
for i in range(m):
    word = input()
    for key, val in d.items():
        if word in val:
            print(key)
