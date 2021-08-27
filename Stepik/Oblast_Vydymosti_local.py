def s():
    # local
    a, b, c = 1,2,3
    w = 'HELLO'
    print(a, b, c, w)   # 1 2 3 HELLO

# global
w = 'hello'
y = 100

s()
print(a)   # NameError: name 'a' is not defined

