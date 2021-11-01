# (1)
# class MyException(Exception):
#     """this is my first exception"""
# raise MyException('hello')


# (2)
# class MyException2(Exception):
#     """this is my Exception"""
# obj = MyException2('hello', 1, 2, 3)
# try:
#     raise obj
# except MyException2:
#     print('DONE')
#


# (3)
# class MyException3(Exception):
#     """this is my Exception"""
# try:
#     raise MyException3('hello', 1, 2, 3)
# except:   # or except Exception:
#     print('DONE - Exception3 caught')


# (4)
# class MyException4(ArithmeticError):
#     """this is my Exception"""
# try:
#     raise MyException4('hello', 1, 2, 3)
# except ArithmeticError:   # or except Exception:
#     print('DONE - Exception4 caught')


# (5)
class MyException5(ArithmeticError):
    """this is my Exception"""

    def __init__(self, *args):
        if args:
            self.message = args[0:2]
        else:
            self.message = None

    def __str__(self):
        print('str is called')
        if self.message:
            return f"MyException5 ({self.message})"
        else:
            return "MyException5 is empty"

raise MyException5('hello', 1, 2, 3)

# OUTPUT: raise MyException5('hello', 1, 2, 3)
# __main__.MyException5: MyException5 (('hello', 1))
# raise MyException5()
# OUTPUT:     raise MyException5()
# __main__.MyException5: MyException5 is empty


# ------------------------------------------------ #
# class SnakeExceptionBase(Exception):
#     """Main class of exceptions in Snake game"""
#
# class SnakeBorderException(SnakeExceptionBase):
#     """Exception when the snake touches the wall/border"""
#
# class SnakeTailException(SnakeBorderException):
#     """Exception when the snake touches own tail"""
