# #Zamykannya - when our inner function uses variables not defined whithin inner function
print('1. -------------------------')
def main_func():
    print('main_func')
    def inner_func():
        print('Hello my friend')
    inner_func()

main_func()
# OUTPUTS:
# main_func
# Hello my friend

# print(main_func())
# OUTPUTS:
# main_func
# Hello my friend
# None  - because our function does not return anything
#
#
print()
print('2. ---------------------------- ')
def out_func():
    print('print in out_func')
    def in_func():
        print('in_func: Hello my friend!!!')
    return in_func
b = out_func()   # тепер b є функцією in_func(), тобто b=in_func(),
# і ми можемо тепер викликати нашу внутрішню функцію in_func(), ось так: b()
# print(b)  # <function main_func2.<locals>.inner_func2 at 0x7f843c9c43a0>
b()   # Hello my friend2
#
#
print()
print('3.-------------------------------')
def main_func3():
    name = 'John'
    def inner_func3():
        print('Hello my friend #3,', name)
    return inner_func3
d = main_func3()
d()
# # Hello my friend #3, John


# print()
# print('4.-------------------------------------')
# def main_func4(value):
#     name = value
#     def inner_func4():
#         print('Hello my friend4', name)
#     return inner_func4
#
# r = main_func4('Misha')
# r()
# # Hello my friend4 Misha
# v = main_func4('Vasya')
# v()
# # Hello my friend4 Vasya
# r()
# v()
#
#
# print()
# print('5.-------------------------------')
# def adder(value):
#     def inner(a):
#         return value + a
#     return inner   # inner w/o ()
# a2 = adder(2)   # value = 2
# print(a2(5))    #  a = 5: 2+5=7
#
#
# print()
# print('6.-----------------------------------------')
# # рахуємо, ск разів викликається наша функція
# def counter():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner
#
# q = counter()
# q()
# q()
# q()
# print(q())  # 4
# r = counter()
# print(r())   # 1
#
#
print()
print('7. --------------------------------')
def average_numbers():
    numbers = []
    def inner(number):
        numbers.append(number)
        # print(numbers)
        # return sum(numbers)/len(numbers)
        return numbers
    return inner
aa = average_numbers()
aa(5)
aa(7)
aa(4)
print(aa(6))
#
#
# print()
# print('8.-------------------------------')
# def average_numbers():
#     summa = 0
#     count = 0
#     def inner(number):
#         nonlocal summa
#         nonlocal count
#         summa += number
#         count += 1
#         return summa / count
#     return inner
#
# av = average_numbers()
# print(av(20))
# print(av(10))
#
#
# print()
# print('9.---------------------------------')
# def average_numbers():
#     numbers = []
#     def inner(*args):
#         for i in args:
#             numbers.append(i)
#         print(numbers)
#         return sum(numbers)/len(numbers)
#     return inner
# f1 = average_numbers()
# print(f1(4, 5, 3, 2))
#
#
# print()
# print('10.---------------------------------')
# from datetime import datetime
# from time import perf_counter
# def timer():
#     start = perf_counter()
#     def inner():
#         return perf_counter() - start
#     return inner
#
# r = timer()
# print(r())
# print(r())
# print(r())
# print(r())
# print(r())
# print(r())
#
#
# print()
# print('11.---------------------------------')
# def add(a, b):
#     return a + b
#
# def counter(func):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"Function {func.__name__} has been called {count} times")
#         return func(*args, **kwargs)
#     return inner
# q = counter(add)
# q = counter(add)
# print(q(10, 20))
# print(q(4, 3))
# print(abs.__name__)   # abs
