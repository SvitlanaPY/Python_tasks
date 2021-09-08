def s():
    # local
    a, b, c = 1, 2, 3
    w = 'HELLO'
    print(id(w))   # 139695845004720
    print(a, b, c, w)   # 1 2 3 HELLO

# global
w = 'hello'
y = 100

s()
print(w, id(w))   # hello   139695845004784
# print(a)   # NameError: name 'a' is not defined

# Після того, як ф-ія s() відпрацює, то її локальні змінні видаляться