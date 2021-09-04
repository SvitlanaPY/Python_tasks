# створення ПОРОЖНЬОГО словника:
empty1 = {}
print(empty1, type(empty1))
# {} <class 'dict'>

# створення ПОРОЖНЬОГО словника:
empty2 = dict()
print(empty2, type(empty2))
# {} <class 'dict'>


Capitals = {'Spain': 'Madrid', 'Ukraine': 'Kiev', 'USA': 'Washington'}
print("Capitals =  ", Capitals)
# Capitals =   {'Spain': 'Madrid', 'Ukraine': 'Kiev', 'USA': 'Washington'}


# ключі передаються як іменовані параметри ф-ії; ключем є тільки строки!
d = dict(Spain = 'Madrid', Ukraine = 'Kiev', USA = 'Washington', Lviv = 380322)
print("d =  ", d)
# d =   {'Spain': 'Madrid', 'Ukraine': 'Kiev', 'USA': 'Washington', 'Lviv': 380322}


# для створення великих словників;
dd = dict([('Spain', 'Madrid'), ("Ukraine", "Kiev"), ("USA", "Washington")])
print("dd =  ", dd)
# dd =   {'Spain': 'Madrid', 'Ukraine': 'Kiev', 'USA': 'Washington'}

# для створення великих словників; у ф-ію zip передається два списки однакової довжини:
# список слючів та список значень
ddd = dict(zip(['Spain', 'Ukraine', 'USA'], ['Madrid', 'Kiev', 'Washington']))
print("ddd =  ", ddd)
# ddd =   {'Spain': 'Madrid', 'Ukraine': 'Kiev', 'USA': 'Washington'}
A = dict(zip('abcdef', range(6)))
print("A=  ", A)
# A=   {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}


# метод fromkeys перетворює в ключ кожен елемент нашого списку, і автоматично присвоює значення ключа в None
# цей метод використовується тоді, коли потрібно ключам списку присвоїти ОДНАКОВЕ значення
q = dict.fromkeys(['a', 'b', 'c'])
print("q = ", q)
# q =  {'a': None, 'b': None, 'c': None}


qq = dict.fromkeys(['a', 'b', 'c'], 100)
print("qq = ", qq)
# qq =  {'a': 100, 'b': 100, 'c': 100}


# До значень словника звернення відбувається по ключу - A[key]
s = {1: 'one', 2: 'two', 3: 'three', 'Lviv': 380322}
print(s[2])   # two
print(s['Lviv'])   # 380322
# Если элемента с заданным ключом нет в словаре, то возникает исключение KeyError.


# Щоб створити нову пару словника - неіснючому ключу присвоюється значення: ss[4] = 'four'
ss = {1: 'one', 2: 'two', 3: 'three'}
ss[4] = 'four'
print("ss=  ", ss)
# ss=   {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
# якщо ключ вже існує, то значення перезапишеться на нове
