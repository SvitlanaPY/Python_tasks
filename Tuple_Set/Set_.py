# a = set(map(int, input().split()))
# print(a, type(a))
# СТВОРЕННЯ
a = {1, 2, 3, 3, 3, 2}
print("a: ", a, type(a))
# a:  {1, 2, 3} <class 'set'>

b = {'hi', 'ho', 'he', 'hi', 'ho', 'hmm'}
print("b: ", b, type(b))
# b:  {'he', 'hi', 'ho', 'hmm'} <class 'set'>

c = set('abracadabra')
print("c: ", c, type(c))
# c:  {'b', 'c', 'a', 'r', 'd'} <class 'set'>

l = set([1, 'hello', '11', 2, False, 1, 2, 1])
print("l: ", l, type(l))
# l:  {False, 1, 2, 'hello', '11'} <class 'set'>

r = set(range(5))
print("r: ", r, type(r))
# r:  {0, 1, 2, 3, 4} <class 'set'>

f = set()
print("empty set 'f': ", f, type(f))
# empty set 'f':  set() <class 'set'>

k = set((1, 3, 2, 33, 22, 11))
print("k: ", k, type(k))
# k:  {1, 2, 3, 33, 11, 22} <class 'set'>

# видалити зі списку дублі (перетворивши list в set, а потім назад set у list
ll = list(set([1, 2, 3, 3, 2, 1, 1]))
print(ll, type(ll))
# [1, 2, 3] <class 'list'>


# додавання елементу:
m = {54, 55, 76, 2, 'hi'}
m.add((9, 8))
m.add(100)
# m.add([99, 88])   # TypeError: unhashable type: 'list'
print("added new elements in set:", m)
# added new element in set: {2, 100, 76, 'hi', (9, 8), 54, 55}
m.add('ccccccc')
print("add str in set:", m)
# add str in set: {2, 100, 76, 'ccccccc', 'hi', (9, 8), 54, 55}

# редагування/ update:
m = {2, 'hi', 100, 76, (9, 8), 54, 55, 'ccccccc'}
m.update([99, 88])
print("updated1 set:", m)
# updated1 set: {2, 99, 100, 'hi', 76, (9, 8), 54, 55, 88, 'ccccccc'}
m.update('bye')
print("updated2 set:", m)
# pdated2 set: {2, 99, 100, 'hi', 76, 'b', 'e', (9, 8), 54, 55, 88, 'y', 'ccccccc'}
m.update(range(111, 115))
print("updated3 set:", m)
# updated3 set: {2, 99, 100, 'hi', 76, 'b', 'e', 111, 112, 113, 114, (9, 8), 54, 55, 88, 'y', 'ccccccc'}
m.update({777777, 999999})
print("updated4 set:", m)
# updated4 set: {2, 'hi', 76, 'b', 'e', (9, 8), 88, 'y', 'ccccccc', 99, 100, 111, 112, 113, 114, 777777, 54, 55, 999999}


# видалення
v = {76, 65, 54, 43, 32, 21}
v.discard(4)
print(v)
# {32, 65, 43, 76, 21, 54}
v.discard(54)
print("delete 54 from set:", v)
# delete 54 from set: {32, 65, 43, 76, 21}
test = v.pop()   # викликається БЕЗ аргументів
print("delete 54 from set:", v)
print("test=", test)


# ОПЕРАЦІЇ НАД МНОЖИНОМА:
m = {2, 'b', 76, 'e', (9, 8), 'y', 88, 99, 100, 'ccccccc', 'hi', 111, 112, 113, 114, 777777, 54, 55, 999999}
print("length: ", len(m))   # 19
print(2 in m, 22 in m, 54 not in m, 54 in m)   # True False False True

# ПЕРЕСІКАННЯ
xx = {4, 3, 2, 1}
zz = {3, 4, 5, 6, 7}
print(xx & zz)   # {3, 4}
print(xx.intersection(zz))   # {3, 4}
xxzz = xx & zz
xxzz = xx.intersection(zz)
# ПЕРЕСІКАННЯ зі зміною множини
x1 = {4, 3, 2, 1}
z1 = {3, 4, 5, 6, 7}
x1.intersection_update(z1)
x1 &= z1
x1 = x1.intersection(z1)
print("xx=", xx, "   x1=", x1)
# xx= {1, 2, 3, 4}    x1= {3, 4}


# ОБ"ЄДНАННЯ (ВСІ елементи з обох множин, але дублі при цьому видаляться)
cc = {4, 3, 2, 1}
dd = {3, 4, 5, 6, 7}
print("cc+dd", cc | dd)
print("cc+dd", cc.union(dd))
ccdd = cc | dd
ccdd = cc.union(dd)
c1 = {4, 3, 2, 1}
d1 = {3, 4, 5, 6, 7}
# ОБ"ЄДНАННЯ зі зміною множини
c1 = c1.union(d1)
c1 |= d1
print("cc=", cc, "   c1=",  c1)
# cc= {1, 2, 3, 4}    c1= {1, 2, 3, 4, 5, 6, 7}

# ВІДНІМАННЯ
# з множини аа віднімемо всі елементи, які пересікаються з множиною bb - залишаться унікальні елементи (ті, яких немає в bb)
aa = {4, 3, 2, 1}
bb = {3, 4, 5, 6, 7}
aabb = aa - bb
aabb = aa.difference(bb)
print("aa-bb=", aabb)   # aa-bb= {1, 2}
# ВІДНІМАННЯ зі зміною множини
a1 = {4, 3, 2, 1}
b1 = {3, 4, 5, 6, 7}
a1 -= b1
a1 = a1.difference(b1)
a1.difference_update(b1)
print("aa=", aa, "   a1=",  a1)
# aa= {1, 2, 3, 4}    a1= {1, 2}

# СИМЕТРИЧНІ РІЗНОСТІ (результатом будуть всі елементи за виключенням тих, які входять в обидві множини)
tt = {4, 3, 2, 1}
pp = {3, 4, 5, 6, 7}
ttpp = tt ^ pp
ttpp = tt.symmetric_difference(pp)
print("tt^pp=", ttpp)   # tt^pp= {1, 2, 5, 6, 7}
# СИМЕТРИЧНІ РІЗНОСТІ зі зміною множини
t1 = {4, 3, 2, 1}
p1 = {3, 4, 5, 6, 7}
t1 ^= p1
t1 = t1.symmetric_difference(p1)
t1.symmetric_difference_update(p1)
print("tt=", tt, "   t1=",  t1)
# tt= {1, 2, 3, 4}    t1= {1, 2, 7, 6, 5}

# множини можна порівнювати
tex1 = {1, 2, 3, 4}
tex2 = {1, 2, 3, 4, 3, 4}
print("? tex1=tex2: ", tex1 == tex2)   # True
print("? tex1> tex2: ", tex1 > tex2)    # False
print("? tex1 >= tex2: ", tex1 >= tex2)  # True


tex11 = {1, 2, 3, 4}
tex22 = {1, 2, 3}
print("? tex11 > tex22: ", tex11 > tex22)   # True
print("? tex22 < tex22: ", tex22 < tex11)   # True

# Example(1.1)
# dict_ = {'Bill': set()}
# while True:
#     text = input()
#     if text == 'q':
#         break
#     name, comments = text.split(': ')
#     dict_[name].add(comments)


# Example(1.2)
# d = {}
# while True:
#     text = input()
#     if text == 'q':
#         break
#     name, comments = text.split(': ')
#     d[name] = d.get(name, set())
#     print(d)
#     print(d[name])
#     d[name].add(comments)
#     print(d)
# print(d)

