d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
rez = d1
for key, val in d2.items():
    rez.setdefault(key, val)
print(rez)
