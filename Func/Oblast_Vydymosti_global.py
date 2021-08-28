
def ss():
    # local
    a, b, c = 1,2,3
    w = 'HELLO'
    print(id(w))   # 140285847392880
    print(a, b, c, w)   # 1 2 3 HELLO

# global
w = 'hello'

ss()
print(id(w))   # 140285847392944
print(w)   # hello
