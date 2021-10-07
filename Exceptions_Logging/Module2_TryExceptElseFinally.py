# try:
#     15 / 0
#     # e
# except ZeroDivisionError: # isinstance(e, ZeroDivisionError) == True
#     print("ZeroDivisionErrorZeroDivisionErrorZeroDivisionError")
# print(ZeroDivisionError.mro())  # <class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]


# (1)
# try:
#     x = [1, 2, "hello", 7]
#     x.sort()
#     print(x)
# except TypeError:
#     print("TypeError happened")
#
# print("Code execution not stopped. I CAT CATCH")

# (2)
# def f(x, y):
#     try:
#         return x / y
#     except TypeError:
#         print("TypeError happens")
# f(5, 0)

# (3)
# def f(x, y):
#     try:
#         return x / y
#     except TypeError:
#         print("TypeError happens")
#     except ZeroDivisionError:
#         print("ZeroDivision!!! Please, correct!")
# print(f(5, 0))   # error happens but was handled and function does not return any value, so we receives None


# (4)
# def f(x, y):
#     try:
#         return x / y
#     except TypeError:  # incorrect type error and this except is not called, but the below except ZeroDivisionError: is called
#         print("TypeError happens")
# try:
#     print(f(5, 0))
# except ZeroDivisionError:
#     print("Devision by zero! Please, correct!")
# OUTPUT: Devision by zero! Please, correct!


# (5)
# def func(x, y):
#     try:
#         return x / y
#     except (TypeError, ZeroDivisionError):
#         print("ERROR")
#
# print(func(5, 0))
# print(func(5, []))
# OUTPUTS:
# ERROR
# None
# ERROR
# None

# (6)
# def funct(x, y):
#     try:
#         return x / y
#     except (TypeError, ZeroDivisionError) as e:
#         print(type(e))
#         print(e)
#         print(e.args)
# print(funct(5, 0))
# OUTPUT:
# <class 'ZeroDivisionError'>    # type of error and it is class
# division by zero   # description of error
# ('division by zero',)   # parameters of our object of the class
# None
# print(funct(5, []))
# OUTPUT:
# <class 'TypeError'>
# unsupported operand type(s) for /: 'int' and 'list'
# ("unsupported operand type(s) for /: 'int' and 'list'",)
# None


# (7)
# def ff(x, y):
#     try:
#         return x / y
#     except:
#         print("Any Error")
#
# print(ff(5, 0))
# OUTPUT:
# Any Error
# None
# print(ff(5, []))
# OUTPUT:
# Any Error
# None


# (8)
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division Error")
    else:
        print("result is:", result)
    finally:
        print("Finally")


divide(2, 1)
# result is: 2.0
# Finally

divide(2, 0)
# Division Error
# Finally

# divide(2, [])
# Finally
# Traceback (most recent call last): .... TypeError: unsupported operand type(s) for /: 'int' and 'list'

