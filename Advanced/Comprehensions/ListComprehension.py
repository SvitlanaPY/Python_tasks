# [<що покласти> for <елемент/індекс> in <діапазон>]
# [<що покласти> for <елемент/індекс> in <діапазон> if <умова>]
# [<що покласти> if <умова> else <покласти ін значення> for <елемент/індекс> in <діапазон>]

# ДВОХВИМІРНІ МАСИВИ
# r = [[0]*m for i in range(n)]     # де m = 4 (стовпці), n = 5 (рядки)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# s = [(i,j) for i in "abc" for j in [1,2,3]]
# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]


st = 'Create a list of the first letters of every word in this string'
st = st.split(' ')
print(st)
a = []
for i in st:
    a.append(i[0])
print(a)


stt = 'Create a list of the first letters of every word in this string'
aa = [i[0] for i in stt.split(' ')]
print(aa)


w = [
    ('Sidorov', 1995),
    ('Lukov', 2002),
    ('Petrov', 1991),
    ('Shevchenko', 1985),
    ('Gorbachov', 1984),
    ('Kostin', 2000),
    ('Isaev', 2005),
    ('Eliseev', 1999),
    ('Kozlov', 2004),
    ('Bukov', 1995),
    ('Gavrilov', 1980),
    ('Efremov', 2006)
]
ww = [elem[0] for elem in w]
print(ww)
# ['Sidorov', 'Lukov', 'Petrov', 'Shevchenko', 'Gorbachov', 'Kostin', 'Isaev', 'Eliseev', 'Kozlov', 'Bukov', 'Gavrilov', 'Efremov']

ww = [elem[1] for elem in w]
print(ww)
# [1995, 2002, 1991, 1985, 1984, 2000, 2005, 1999, 2004, 1995, 1980, 2006]

ww = [elem[0] for elem in w if elem[0].startswith('G')]
print(ww)
# ['Gorbachov', 'Gavrilov']

ww = [elem[1] for elem in w if elem[1] > 2000]
print(ww)
# [2002, 2005, 2004, 2006]

ww = [elem[0][0] for elem in w if elem[1] > 2000]
print(ww)
# ['L', 'I', 'K', 'E']
