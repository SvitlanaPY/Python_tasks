def s():
    # local
    a = 11
    b = 22
    # c = 33
    print('local:', a, b, c)

# global
a = 100
b = 200
c = 300

s()
print('global:', a, b, c)
print()


def ss(aa, bb, cc):
    # local
    aa = 10
    print('local:', aa, bb, cc)

# global
aa = [1, 2, 3]
bb = 200
cc = 300

ss(aa, bb, cc)
print('global:', aa, bb, cc)
print()


# !!!!!!!!!!!!!!!!!!!!
# оскільки список є змінним обєктом, то ми всередині ф-ії можемо звернутись до конкретного елемента списку
# і змінити його значення,
# причому значення цього конкретного елемента зміниться як в локальній, так і в глобальній області видимості
def f(aaa, bbb, ccc):
    # local
    aaa[0] = 111
    print('local:', aaa, bbb, ccc)

# global
aaa = [1, 2, 3]
bbb = 200
ccc = 300

f(aaa, bbb, ccc)
print('global:', aaa, bbb, ccc)