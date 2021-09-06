# create tuple
a = (1, 2, 3, 4, 5)
print(a, type(a))
# (1, 2, 3, 4, 5) <class 'tuple'>

b = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(b, type(b))
# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10) <class 'tuple'>

# кома після 100 вказує на те, що це кортеж
c = 100,
print(c, type(c))
# (100,) <class 'tuple'>

d = tuple(range(1, 6))
print(d, type(d))
# (1, 2, 3, 4, 5) <class 'tuple'>

f = tuple(['h', 'e', 'l', 'l', 'o'])
print(f, type(f))
# ('h', 'e', 'l', 'l', 'o') <class 'tuple'>


s = tuple('hello')
print(s, type(s))
# ('h', 'e', 'l', 'l', 'o') <class 'tuple'>


g = ()
print(g, type(g))
# () <class 'tuple'>

h = tuple()
print(h, type(h))
# () <class 'tuple'>


t = 10, 20, 30, 40, 50
print(type(t))  # <class 'tuple'>



print(len(t))  # 5
print(10 in t, 100 in t, 200 not in t)  # True False True
t = 10, 20, 30, 40, 50
tt = tuple((44, 55))
print("t+tt: ", t + tt)
# t+tt:  (10, 20, 30, 40, 50, 44, 55)
print("tt+t: ", tt + t)
# tt+t:  (44, 55, 10, 20, 30, 40, 50)

# ДУБЛЮВАННЯ КОРТЕЖУ
print(tt * 2)  # (44, 55, 44, 55)

print("sum=", sum(t))
# sum= 150
print("min= ", min(t), "max= ", max(t))
# min=  10 max=  50

# можемо змінити список в кортежі, але не кортеж:
l = 1, 'hello', 33, [10, 20, 30], False, 5
print(l, type(l))
# (1, 'hello', 33, [10, 20, 30], False, 5) <class 'tuple'>
l[3].append(100)
print(l)
# (1, 'hello', 33, [10, 20, 30, 100], False, 5)

tuple_ = (1, 'hello', 33, [10, 20, 30], False, 5)
print(tuple_.__sizeof__(), type(tuple_))   # 72 bytes   <class 'tuple'>
list_ = [1, 'hello', 33, [10, 20, 30], False, 5]
print(list_.__sizeof__(), type(list_))   # 88 bytes   <class 'list'>

# можемо створити словник, в якому ключами будуть кортежі:
key = (1, 2, 3)
d = {}
d[key] = 'hello'
d.setdefault((10, 20), 'hi')
print("dict: ", d)
# dict:  {(1, 2, 3): 'hello', (10, 20): 'hi'}
