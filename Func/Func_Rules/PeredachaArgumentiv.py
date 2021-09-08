# з самого початку виконання нашої ф-ії наші глобальні і локальні змінні посилаються на одні і ті ж об"єкти в пам"яті
def f(a, b):
    print(id(a), id(b), ' - local')    # 9789216 9790176
    a = 100
    b = 200
    print(id(a), id(b), ' - local after')
    print(a, b, ' - local')

c = 20
d = 50
print(id(c), id(d), " - global")    # 9789216 9790176
f(c, d)
print(c, d, ' - global')

