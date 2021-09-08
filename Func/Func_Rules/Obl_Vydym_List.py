# !!!!!!!!!!!!!!!!!!!!
# оскільки список є змінюваним обєктом, то ми всередині ф-ії можемо звернутись до конкретного елемента списку
# і змінити його значення,
# причому значення цього конкретного елемента зміниться як в локальній, так і в глобальній області видимості
def ff(aaa, bbb, ccc):
    # local
    print("aaa= ", aaa)   # aaa=  [1, 2, 3]
    aaa[0] = 111
    print('local:', aaa, bbb, ccc)   # local: [111, 2, 3] 200 300

# global
aaa = [1, 2, 3]
bbb = 200
ccc = 300

ff(aaa, bbb, ccc)
print('global:', aaa, bbb, ccc)   # global: [111, 2, 3] 200 300


print()
# щоб уникнути зміну списку всередині функції, потрібно під час передачі змінних при виклику ф-ії передавати копію списку
# тобто ff(aaa[:], bbb, ccc);   aaa[:] - повний зріз
def f(a,b):
    print(a, b, '- local')   # [1, 20, 333] 90 - local
    a.append(555)
    a[1] = 777
    b = 99
    print(a, b, '- local after')   # [1, 777, 333, 555] 99 - local after

c = [1, 20, 333]
d = 90

print("'c' is a copy and global 'c' has been NOT changed")
f(c[:], d)   # c[:]  -- копія с
print(c, d, ' - global')

print("'c' is not a copy and global 'c' has been changed")
f(c, d)   # [1, 777, 333, 555] 90  - global
print(c, d, ' - global')   # [1, 20, 333], 90
