print("\n#1")
*a, b, c = [True, 3, 'yes', 67, 98, 1, 'hello']
print("a=", a, "  b=", b, "  c=", c)
# a= [True, 3, 'yes', 67, 98]   b= 1   c= hello


print("\n#2")
a, *b, c = [True, 3, 'yes', 67, 98, 1, 'hello']
print("a=", a, "  b=", b, "  c=", c)
# a= True   b= [3, 'yes', 67, 98, 1]   c= hello


print("\n#3")
a, b, *c = [True, 3, 'yes', 67, 98, 1, 'hello']
print("a=", a, "  b=", b, "  c=", c)
# a= True   b= 3   c= ['yes', 67, 98, 1, 'hello']


print("\n#4")
a, *b, c = [1, 2]
print("a=", a, "  b=", b, "  c=", c)
# a= 1   b= []   c= 2


print("\n#5")
*a, b, c = 'hello world'
print("a=", a, " b=", b, " c=", c)
# a= ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r']  b= l  c= d


print("\n#6")
s = [4, 10]
ss = list(range(*s))
print("ss=", ss)
# ss= [4, 5, 6, 7, 8, 9]


print("\n#7")
a, b, *c = range(5)    # range(5): [0, 1, 2, 3, 4]
print("a=", a, " b=", b, " c=", c)
# a= 0  b= 1  c= [2, 3, 4]


print("\n#8")
def f(a, b, c, d):
    print("a=", a, "  b=", b, "  c=", c, "  d=", d)
    # a= 11   b= hello   c= [1, 2, 3]   d= True
w = [11, 'hello', [1,2,3], True]   # має містити стільки елементів, скільки змінних приймає функція
f(*w)


print("\n#9")
def ff(*args):
    print(args, type(args))   # args = (1, 2, 3, 4, 5, 6), отже args - це змінна, в якій міститься кортеж із переданих у ф-ію значень
    # (1, 2, 3, 4, 5, 6) <class 'tuple'>
ff(1,2,3,4,5,6)   # можна передати у ф-ію будь-яку к-сть значень


print("\n#10")
def z(**kwargs):
    print("kwargs=", kwargs, type(kwargs))
    # kwargs= {'a': 1, 'b': 2, 'c': 3} <class 'dict'>
    for k,v in kwargs.items():
        print("key=:", k, "   val=", v)
        # key=: a    val= 1
        # key=: b    val= 2
        # key=: c    val= 3

z(a=1, b=2, c=3)


print("\n#11")
def tet(*args, **kwargs):
    print(args, kwargs)
    # (5, 4, 3, 2, 7) {'a': 5, 'name': 'Anna', 'year': 2021}

tet(5, 4, 3, 2, 7, a=5, name="Anna", year=2021)


# print("\n#12")
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def tt(**kwargs, *args):   # *args має іти ПЕРЕД **kwargs
#     print(kwargs, args)
#     # SyntaxError: invalid syntax
# tt(a=5, name="Anna", year=2021, 5, 4, 3, 2, 7)


print("\n#13")
def outPrint(*args, sep="#", end="@"):     # "#" та "@" - значення по замовчуванню
    print(args, sep, end)

outPrint(1, 2, 3, 4, sep="999")   # (1, 2, 3, 4) 999 @
outPrint(11, 22, end="!!!")       # (11, 22) # !!!
outPrint(10, 20)                  # (10, 20) # @


print("\n#14")
a = [2, 22, 3, 33, 4, 55]
print(*a)   # 2 22 3 33 4 55
print(a)    # [2, 22, 3, 33, 4, 55]
print(*[2, 22, 3, 33, 4, 55])   # = print(*a) --> 2 22 3 33 4 55

# print(*a) == print(2, 22, 3, 33, 4, 55)
