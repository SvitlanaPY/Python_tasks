# def func():
#     print("Hello world!")
#
# func()   # Hello world!
# func.__call__()   # Hello world!


# Функція є не лише процедурою, але і екземпляром якогось певного класу,
# тобто в неї є свої методи, атрибути, до яких ми можемо звертатись.
# Функція в Пайтоні є функтором;
# Функтор - це екземпляр класу, який веде себе як функція;
# Отже нашу ф-ію func() можемо змусити працювати, викликавши в неї метод __call__():
# func.__call__(), а не лише func()
# Оск. ф-ія є екземпляром класу, то ми можемо:
# 1. присвоювати ф-ію у якусь змінну і звертаючись до змінною - викликати ф-ію:
# def f():
#     print("Hello")
#
# var_ = f
# var_()
#
# 2. передавати ф-ію як аргумент в іншу ф-ію
# def f_1():
#     print("BYE")
#
# def f_2(f_1):
#     f_1()
#
# f_2(f_1)
#
# 3. можемо повернути ф-ію як значення, яке повертає ф-ія:
# def func_1():
#     print("GOOD BYE")
#
# def func_3():
#     return func_1
#
# a = func_3()
# a()   # відпрацює як функція func_1()
# або
# func_3()()



# class Repeater:
#     def __init__(self, num_):
#         self.num_ = num_
#
#     def __call__(self, foo_):
#         def inner(*args, **kwargs):
#             for i in range(self.num_):
#                 foo_(*args, **kwargs)
#         return inner
#
# @Repeater(3)
# def foo():
#     print("HELLO!")
#
# foo()


class RepeaterNew:
    def __init__(self, num_, func):
        self.fn = func
        self.num_ = num_

    def __call__(self, *args, **kwargs):
        def inner(*args, **kwargs):
            for i in range(self.num_):
                foo_(*args, **kwargs)
            return inner()


@RepeaterNew(3)
def foo():
    print("HELLO!")

foo()
