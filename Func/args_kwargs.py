*a, b, c = [True, 3, 'yes', 67, 98, 1, 'hello']
print("a=", a, "  b=", b, "  c=", c)
# a= [True, 3, 'yes', 67, 98]   b= 1   c= hello


a, *b, c = [True, 3, 'yes', 67, 98, 1, 'hello']
print("a=", a, "  b=", b, "  c=", c)
# a= True   b= [3, 'yes', 67, 98, 1]   c= hello


a, b, *c = [True, 3, 'yes', 67, 98, 1, 'hello']
print("a=", a, "  b=", b, "  c=", c)
# a= True   b= 3   c= ['yes', 67, 98, 1, 'hello']

a, *b, c = [1, 2]
print("a=", a, "  b=", b, "  c=", c)
# a= 1   b= []   c= 2

*a, b, c = 'hello world'
print("a=", a, " b=", b, " c=", c)
# a= ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r']  b= l  c= d

s = [4, 10]
ss = list(range(*s))
print("ss=", ss)
# ss= [4, 5, 6, 7, 8, 9]


def f(a, b, c, d):
    print("a=", a, "  b=", b, "  c=", c, "  d=", d)
    # a= 11   b= hello   c= [1, 2, 3]   d= True
w = [11, 'hello', [1,2,3], True]   # має містити стільки елементів, скільки змінних приймає функція
f(*w)


def ff(*args):
    print(args, type(args))   # args = (1, 2, 3, 4, 5, 6), отже args - це змінна, в якій міститься кортеж із переданих у ф-ію значень
    # (1, 2, 3, 4, 5, 6) <class 'tuple'>
ff(1,2,3,4,5,6)   # можна передати у ф-ію будь-яку к-сть значень


def z(**kwargs):
    print("kwargs=", kwargs, type(kwargs))
    # kwargs= {'a': 1, 'b': 2, 'c': 3} <class 'dict'>
    for k,v in kwargs.items():
        print("key=:", k, "   val=", v)
        # key=: a    val= 1
        # key=: b    val= 2
        # key=: c    val= 3

z(a=1, b=2, c=3)


def tet(*args, **kwargs):
    print(args, kwargs)
    # (5, 4, 3, 2, 7) {'a': 5, 'name': 'Anna', 'year': 2021}

tet(5, 4, 3, 2, 7, a=5, name="Anna", year=2021)


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def tt(**kwargs, *args):   # *args має іти ПЕРЕД **kwargs
#     print(kwargs, args)
#     # SyntaxError: invalid syntax
# tt(a=5, name="Anna", year=2021, 5, 4, 3, 2, 7)


def outPrint(*args, sep="#", end="@"):     # "#" та "@" - значення по замовчуванню
    print(args, sep, end)

outPrint(1, 2, 3, 4, sep="999")   #  (1, 2, 3, 4) 999 @
outPrint(11, 22, end="!!!")       #  (11, 22) # !!!
outPrint(10, 20)    # (10, 20) # @
