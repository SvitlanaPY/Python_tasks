# [<що покласти> for <елемент/індекс> in <діапазон>]
# [<що покласти> for <елемент/індекс> in <діапазон> if <умова>]
# [<що покласти> if <умова> else <покласти ін значення> for <елемент/індекс> in <діапазон>]

# ДВОХВИМІРНІ МАСИВИ
n = 5   # рядки
m = 4   # стовпці
r = [[0]*m for i in range(n)]
print("r: ", r)
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


s = [(i, j) for i in "abc" for j in [1, 2, 3]]
print("s: ", s)
# [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]


st = 'Create a list of the first letters of every word in this string'
st = st.split(' ')
print("st: ", st)
# st:  ['Create', 'a', 'list', 'of', 'the', 'first', 'letters', 'of', 'every', 'word', 'in', 'this', 'string']
a = []
for i in st:
    a.append(i[0])
print("a: ", a)


stt = 'Create a list of the first letters of every word in this string'
aa = [i[0] for i in stt.split(' ')]
print("aa: ", aa)


mm = [
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
ww = [elem[0] for elem in mm]
print("names: ", ww)
# ['Sidorov', 'Lukov', 'Petrov', 'Shevchenko', 'Gorbachov', 'Kostin', 'Isaev', 'Eliseev', 'Kozlov', 'Bukov', 'Gavrilov', 'Efremov']

ww = [elem[1] for elem in mm]
print("years: ", ww)
# [1995, 2002, 1991, 1985, 1984, 2000, 2005, 1999, 2004, 1995, 1980, 2006]

ww = [elem[0] for elem in mm if elem[0].startswith('G')]
print("names start with G: ", ww)
# ['Gorbachov', 'Gavrilov']


ww = [elem[1] for elem in mm if elem[1] > 2000]
print("birth > 2000: ", ww)
# [2002, 2005, 2004, 2006]

ww = [elem[0][0] for elem in mm if elem[1] > 2000]
print(ww)
# ['L', 'I', 'K', 'E']


w = {
    'Sidorov': {
        'age': 1995,
        'hobby': 'soccer',
        'car': 'BMW'
    },
    'Lukov': {
        'age': 2002,
        'hobby': 'basketball',
        'car': 'Opel'
    },
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Shevchenko': {'age': 1984, 'hobby': 'tennis', 'car': 'Audi'},
    'Gorbachov': {'age': 2000, 'hobby': 'swimming', 'car': 'BMW'},
    'Kostin': {'age': 2005, 'hobby': 'music', 'car': 'Reno'},
    'Isaev': {'age': 1995, 'hobby': 'dances', 'car': 'Open'},
    'Eliseev': {'age': 2004, 'hobby': 'music', 'car': 'BMW'},
    'Kozlov': {'age': 1999, 'hobby': 'yoga', 'car': 'Jeep'},
    'Bukov': {'age': 2001, 'hobby': 'soccer', 'car': 'Audi'},
    'Gavrilov': {'age': 1998, 'hobby': 'dances', 'car': 'Opel'},
    'Efremov': {'age': 1986, 'hobby': 'yoga', 'car': 'BMW'}
    }

# у словниках по замовчуванню ОБХІД відбувається по КЛЮЧАХ
names = [elem for elem in w]
print("names: ", names)
# names:  ['Sidorov', 'Lukov', 'Petrov', 'Shevchenko', 'Gorbachov', 'Kostin', 'Isaev', 'Eliseev', 'Kozlov', 'Bukov', 'Gavrilov', 'Efremov']

nested_dicts = [w[elem] for elem in w]
print("nested_dicts: ", nested_dicts)
# nested_dicts:  [{'age': 1995, 'hobby': 'soccer', 'car': 'BMW'}, {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'}, {'age': 1991, 'hobby': 'chess', 'car': 'BMW'}, {'age': 1984, 'hobby': 'tennis', 'car': 'Audi'}, {'age': 2000, 'hobby': 'swimming', 'car': 'BMW'}, {'age': 2005, 'hobby': 'music', 'car': 'Reno'}, {'age': 1995, 'hobby': 'football', 'car': 'Open'}, {'age': 2004, 'hobby': 'gymnastic', 'car': 'BMW'}, {'age': 1999, 'hobby': 'badminton', 'car': 'Jeep'}, {'age': 2001, 'hobby': 'soccer', 'car': 'Audi'}, {'age': 1998, 'hobby': 'dances', 'car': 'Opel'}, {'age': 1986, 'hobby': 'yoga', 'car': 'BMW'}]

cars_ = [w[elem]['car'] for elem in w]     # elem - це ключ
print("cars: ", cars_)
# cars:  ['BMW', 'Opel', 'BMW', 'Audi', 'BMW', 'Reno', 'Open', 'BMW', 'Jeep', 'Audi', 'Opel', 'BMW']

age_ = [(key, w[key]['age']) for key in w if w[key]['age'] < 2000]
print("age < 2000: ", age_)
# age < 2000:  [('Sidorov', 1995), ('Petrov', 1991), ('Shevchenko', 1984), ('Isaev', 1995), ('Kozlov', 1999), ('Gavrilov', 1998), ('Efremov', 1986)]


hobby_ = [(key, w[key]['hobby']) for key in w if w[key]['hobby'] in ('soccer', 'yoga')]
print("hobby is soccer_yoga: ", hobby_)
# hobby is soccer_yoga:  [('Sidorov', 'soccer'), ('Kozlov', 'yoga'), ('Bukov', 'soccer'), ('Efremov', 'yoga')]



str_ = 'sfkTYRSJfjasa6567254jhjkFw6789JHHiusdf'
strr_ = [int(symbol) for symbol in str_ if symbol.isdigit()]
print("digits: ", strr_)
# [6, 5, 6, 7, 2, 5, 4, 6, 7, 8, 9]


n = 5    # рядки
m = 3    # стовпці
zz = [[0] * m for i in range(n)]
print(zz)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

import random
n = 5
m = 3
xx = [[random.randint(1, 10)] * m for i in range(n)]
print("xx: ", xx)
# xx:  [[6, 6, 6], [2, 2, 2], [9, 9, 9], [4, 4, 4], [1, 1, 1]]


# для кожної змінної і (і=0, і=1, і=2) буде формуватись генератор, який повторюється 5 раз
xxx = [[random.randint(1, 10) for j in range(5)] for i in range(3)]
print("xxx: ", xxx)
# xxx:  [[1, 1, 3, 1, 7], [4, 1, 10, 3, 7], [7, 8, 1, 9, 7]]


"""
Tablytsya mnozhennya
"""
n = 5    # рядки
m = 10    # стовпці
# кожне і множимо на всі числа в проміжку (1, m+1)
q = [[i*j for j in range(1, m+1)] for i in range(1, n+1)]
print("tablytsya mnozhennya: ", q)
# tablytsya mnozhennya:  [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]]
for i in q:
    print(i)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

"""
В вашем распоряжении есть двумерный список vector. 
Ваша задача при помощи генератора-списка сделать на основании vector линейный(одномерный ) список и вывести его.
"""
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
v = [j for i in vector for j in i]
print(v)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


"""
При помощи генератора-списков создайте список, состоящий из слов,  начинающихся с буквы 't' или 'T'. 
Слова возьмите из переменной phrase, также не забывайте про метод split()

В качестве ответа выведите полученный список, слова в нем должны стоять в том же порядке, 
в котором они стояли в изначальной фразе.
"""
phrase = 'Take only the words that start with t in this sentence'
letter = 'tT'
print([i for i in phrase.split() if i[0] in letter])
# OR
print([i for i in phrase.split() if i.startswith(('T', 't'))])
