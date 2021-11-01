"""
Exception є батьківським класом усіх виключень (окрім системних виключень: SystemExit, GeneratorExit, KeyboardInterrupt)
і всі свої власні виключення краще наслідувати від класу Exception,
а не від BaseException, для того щоб виключити ці три системні класи.
Щоб створити своє власне виключення,
потрібно створити свій клас, дати йому ім"я, і який буде наслідуватись від класу Exception.
Ми можемо викликати створений клас виключення або об"єкт від створеного класу виключення
"""
print("(1)")
# # створюємо свій клас викллючення і викликаємо цей створений клас виключення:
# class MyException(Exception):
#     """this is my first exception"""
#
# raise MyException('hello', 1, 2)   #  викликаємо цей створений клас виключення передаючи атрибути
#
# # OUTPUT:
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/User_Exceptions_Egoroff4.py", line 11, in <module>
# #     raise MyException('hello', 1, 2)
# # __main__.MyException: ('hello', 1, 2)


print("(2)")
# class MyException2(Exception):
#     """this is my Exception"""
#
# try:
#     raise MyException2('hello', 1, 2, 3)
# except:   # or except Exception:
#     print('DONE - Exception2 caught')
#
# # OUTPUT:
# # DONE - Exception2 caught


print("(3)")
# class MyException3(Exception):
#     """this is my Exception"""
#
# obj = MyException3('hello', 1, 2, 3)
# #  екземпляр створеного класу виключення MyException2
#
# try:
#     raise obj   # викликаємо екземпляр створеного класу виключення MyException3
# except MyException3:
#     print('DONE')
#
# # OUTPUT:
# # DONE


print("(4.1)")
# class MyException4(ArithmeticError):
#     """this is my Exception"""
#
# try:
#     raise MyException4('hello', 1, 2, 3)
# except ArithmeticError:
#     print('DONE - Exception4 caught')
#
# # OUTPUT:
# # DONE - Exception4 caught


print("(4.2)")
# class MyException4(ArithmeticError):
#     """this is my Exception"""
#
# try:
#     raise MyException4('hello', 1, 2, 3)
# except Exception
#     print('DONE - Exception4 caught')
#
# # OUTPUT:
# # DONE - Exception4 caught


"""
Оскільки наш створений клас виключення MyException4 типу ArithmeticError не наслідується від класу ZeroDivisionError,
тобто він стає на рівні з класом ZeroDivisionError в ієрархії виключень, 
то кинуте виключення MyException4 типу ArithmeticError не зможе обробитись блоком "except ZeroDivisionError:", 
бо ми знаходимось не в тій гілці ієрархії.
Виходить, що ми кидаємо виключення типу ArithmeticError, а обробляємо виключення ZeroDivisionError нижчого рівня.

Якщо буде навпаки (кидаємо виключення типу ZeroDivisionError, а обробляємо виключення ArithmeticError),
то кинуте виключення ZeroDivisionError обробиться.
"""
print("(4.3)")
# class MyException4(ArithmeticError):
#     """this is my Exception"""
#
# try:
#     raise MyException4('hello', 1, 2, 3)
# except ZeroDivisionError:
#     print('DONE - Exception caught')
#
# # OUTPUT:
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/User_Exceptions_Egoroff4.py", line 63, in <module>
# #     raise MyException4('hello', 1, 2, 3)
# # __main__.MyException4: ('hello', 1, 2, 3)


"""
Класи виключень, які ми пишемо самі, ми можемо перевизначати.
"""
print("(5.1)")
# class MyException5(ArithmeticError):
#     """this is my Exception"""
#
#     def __init__(self, *args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None
#
#     def __str__(self):
#         print('str is called')
#         if self.message:
#             return f"MyException5 ({self.message})"
#         else:
#             return "MyException5 is empty"
#
# raise MyException5('hello', 1, 2, 3)
#
# # OUTPUT:
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/User_Exceptions_Egoroff4.py", line 115, in <module>
# #     raise MyException5('hello', 1, 2, 3)
# # __main__.MyException5: MyException5 (hello)
# # str is called


print("(5.2)")
# class MyException5(ArithmeticError):
#     """this is my Exception"""
#
#     def __init__(self, *args):
#         if args:
#             self.message = args[0]
#         else:
#             self.message = None
#
#     def __str__(self):
#         print('str is called')
#         if self.message:
#             return f"MyException5 ({self.message})"
#         else:
#             return "MyException5 is empty"
#
# raise MyException5()
#
# # # OUTPUT:
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/User_Exceptions_Egoroff4.py", line 151, in <module>
# #     raise MyException5()
# # __main__.MyException5: MyException5 is empty
# # str is called


print("# - #"*10)
"""
Зі своїх власних виключень можемо вибудовувати свою ієрархію виключень
"""
class SnakeExceptionBase(Exception):
    """Основний клас помилок в грі Snake"""

class SnakeBorderException(SnakeExceptionBase):
    """Помилка, коли змійка торкається країв поля"""

class SnakeTailException(SnakeBorderException):
    """Помилка, коли змійка торкається свого хвоста"""
