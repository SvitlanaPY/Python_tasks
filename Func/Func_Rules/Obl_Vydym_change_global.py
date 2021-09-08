def s():
    # local
    global a
    a = 30

# global
a = [1,2,3,4,5,6]
print("before changing global a: ", a)   # before changing global a:  [1, 2, 3, 4, 5, 6]

s()
print('global:', a)   # global: 30
