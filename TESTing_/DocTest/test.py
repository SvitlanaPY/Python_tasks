# def sum(a, b):
#     return a + b
#
# print(sum(0.5, 5.0))

# val1 = float(input("Enter val1: "))
# val2 = float(input("Enter val1: "))
# summa = val1 / val2
# print(summa)

# def div(a, b):
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         if b != 0:
#             return round((a / b), 2)
#         else:
#             return ZeroDivisionError("Divisor is zero!")
#     else:
#         return ValueError('It must be a number')
#
# divv = div(10, 7)
# print(divv)

from math import sqrt


def sum(a):
    return sqrt(a)
    #     else:
    #         return ZeroDivisionError("Divisor is zero!")
    # else:
    #     return TypeError('Invalid input, enter some number')

print(sum("4.0"))