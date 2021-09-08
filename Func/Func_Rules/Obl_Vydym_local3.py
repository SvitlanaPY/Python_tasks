def ss():
    print(w)   # hello
    # local
    a, b, c = 1, 2, 3
    print(a, b, c, w)   # 1 2 3 hello, w - is global variable

# global
w = 'hello'

ss()
print(w)   # hello
