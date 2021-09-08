def s():
    # local
    print(w)   # UnboundLocalError: local variable 'w' referenced before assignment
    a, b, c = 1, 2, 3
    w = 'HELLO'
    print(id(w))
    print(a, b, c, w)

# global
w = 'hello'

s()
print(w)   # hello
print(id(w))   # 139695845004784
