print("function   s()")
def s():
    # local
    a = 11
    b = 22
    c = 33
    print('local:', a, b, c)   # 11, 22, 33

# global
a = 100
b = 200
c = 300

s()
print('global:', a, b, c)   # 100, 200, 300
print()


print("\nfunction   f()")
def f():
    # local
    aa = 11
    bb = 22
    print('local:', aa, bb, cc)   # 11, 22, 300 (c is global variable)

# global
aa = 100
bb = 200
cc = 300

f()
print('global:', aa, bb, cc)   # 100, 200, 300


print("\nfunction   ss()")
def ss(aa, bb, cc):
    # local
    print('local:', aa, bb, cc)

# global
aa = 100
bb = 200
cc = 300

ss(aa, bb, cc)   # параметри, що передаються у ф-ію, автоматично стають локальними змінними всередині ф-ії
print('global:', aa, bb, cc)



print("\nfunction   sss()")
def sss(aa, bb, cc):
    # local
    print(id(aa))   # aa - is global
    aa = 20
    print(id(aa))   # aa - is local now
    print('local:', aa, bb, cc)   # local: 20 200 300

# global
aa = 100
bb = 200
cc = 300

sss(aa, bb, cc)   # параметри, що передаються у ф-ію, автоматично стають локальними змінними всередині ф-ії
print('global:', aa, bb, cc)   # global: 100 200 300
print(id(aa))
