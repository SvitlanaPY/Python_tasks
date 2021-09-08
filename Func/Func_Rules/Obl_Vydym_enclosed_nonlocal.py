# правило пошуку імен в python-i:
# LEGB:   L=local, E=enclosing, G=global, B=builtins

def s():   # s()-function is enclosing function
    abs = 200  # abs = 'hello' from q()-function is NOT available for s()-function
    cc = 111
    def q():   # q()-function is local function in relation to s()-function
        nonlocal cc  # це означає, що ми беремо значення для cc-змінної з s()-функції і змінюємо її на сс=222
        cc = 222
        abs = 'hello'
        print('def q(): ', 'cc=', cc, '  abs=', abs)  # def q(): cc= 222 abs= hello
    q()
    print('def s(): ', 'cc=', cc, '  abs=', abs)  # def s(): cc= 222 abs= 200

abs = [1,2,3,4,5]   # global
cc = [10, 20]
s()
print('global: ', 'abs=', abs)   # global: abs= [1, 2, 3, 4, 5]
print('global: ', 'cc=', cc)
