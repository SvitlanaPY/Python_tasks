"""
Конструкція try-except дозволяє нам:
1. вибрати типи помилок, які вважаємо некритичними,
2. якось їх обробити і
3. продовжити виконання коду.
Якщо є кілька except-блоків, то будь-яке виключення буде оброблятись одним із них - першим, під яке підійде наше виключення.
Решта except-блоків не буде виконуватись.
"""
# try:
#     15 / 0
#     # e
# except ZeroDivisionError:  # isinstance(e, ZeroDivisionError) == True
#     print("ZeroDivisionErrorZeroDivisionErrorZeroDivisionError")

print(ZeroDivisionError.mro())
# [<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]


print("(1)")
try:
    x = [1, 2, "hello", 7]
    x.sort()
    print(x)
except TypeError:
    print("TypeError happened :( ")

print("Code execution not stopped. I CAN CATCH")


# print("(2)")
# def f(x, y):
#     try:
#         return x / y
#     except TypeError:
#         print("TypeError happens!!!")
# f(5, [])
# # OUTPUT:
# # TypeError happens!!!
# f(5, 0)
# # OUTPUT:
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Module2_TryExceptElseFinally.py", line 36, in <module>
# #     f(5, 0)
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Module2_TryExceptElseFinally.py", line 32, in f
# #     return x / y
# # ZeroDivisionError: division by zero


"""
Якщо є кілька except-блоків, то будь-яке виключення буде оброблятись одним із них - першим, під яке підійде наше виключення.
Решта except-блоків не буде виконуватись.
"""
print("(3)")
def f(x, y):
    try:
        return x / y
    except TypeError:
        print("TypeError happens")
    except ZeroDivisionError:
        print("ZeroDivision!!! Please, correct!")
print(f(5, 0))
# error happens but was handled it and function does not return any value, so we receives None
# OUTPUTS:
# ZeroDivision!!! Please, correct!
# None


"""
Виключення можемо обробляти і в інший спосіб - 
Можемо відловлювати виключення при запуску функції.
"""
# print("(4)")
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


"""
Одним except-блоком можемо спіймати кілька виключень - 
для цього потрібно передавати кортеж із типом всіх виключень, які потрібно відловити.
"""
# print("(5)")
# def func(x, y):
#     try:
#         return x / y
#     except (TypeError, ZeroDivisionError):
#         print("ERROR")
#
# print(func(5, 0))
# print(func(5, []))
# # OUTPUTS:
# # ERROR
# # None
# # ERROR
# # None


"""
Можемо також обробляти і сам об"єкт помилки. 
Для цього потрібно вказати тип помилки і конструкцію as та ім"я того об"єкту, який ми хочемо відловити.
Кожна помилка має атрибут args.
"""
# print("(6)")
# def funct(x, y):
#     try:
#         return x / y
#     except (TypeError, ZeroDivisionError) as e:
#         print("type(e): ", type(e))   # <class 'ZeroDivisionError'>
#         print("e: ", e)   # division by zero
#         print("e.args: ", e.args)   # ('division by zero',)
# print(funct(5, 0))   # None
#
# # OUTPUT:
# # <class 'ZeroDivisionError'>     # type of error and it is class
# # division by zero     # description of error
# # ('division by zero',)     # parameters of our object of the class
# # None
#
# print(funct(5, []))
# # OUTPUT:
# # <class 'TypeError'>
# # unsupported operand type(s) for /: 'int' and 'list'
# # ("unsupported operand type(s) for /: 'int' and 'list'",)
# # None


"""
Часто ми не знаємо, який тип помилки може виникнути, 
в такому випадку ми можемо написати try-except блок але не вказувати типу помилок, які потрібно вдловлювати.
Для цього можемо використати порожній except
"""
# print("(7)")
# def ff(x, y):
#     try:
#         return x / y
#     except:
#         print("Any Error")
#
# print(ff(5, 0))
# # OUTPUT:
# # Any Error
# # None
# print(ff(5, []))
# # OUTPUT:
# # Any Error
# # None


# print("(8)")
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("Division Error")
#     else:
#         print("result is:", result)
#     finally:
#         print("Finally")
#
#
# divide(2, 1)
# # result is: 2.0
# # Finally
#
# divide(2, 0)
# # Division Error
# # Finally
#
# # divide(2, [])
# # Finally
# # Traceback (most recent call last): .... TypeError: unsupported operand type(s) for /: 'int' and 'list'
#

"""
"""
# try:
#     15 / 0
# except ZeroDivisionError:
#     print("Division by zero")

