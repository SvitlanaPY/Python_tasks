# global
a = [1,2,3,4,5,6]
print('global:', a)

def s():
    # local
    global a
    a = 30

s()
print('global:', a)
