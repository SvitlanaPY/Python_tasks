import logging
################
# number = float(input("Enter a positive number:"))
# assert (number > 0), "Only positive numbers are allowed!"
# OUTPUT: AssertionError: Only positive numbers are allowed!

# name = 'hauser'
# assert(name=='Quaid'), f"name is {name}, it should be Quaid"
# print(f"my name is {name}")
# AssertionError: name is hauser, it should be Quaid

# def hyp(a, b):
#     hypotenuza = (a ** 2 + b ** 2)   # hypotenuza = (a ** 2 + b ** 2) ** 0.5
#     return hypotenuza
#
# assert hyp(3, 4) == 5   # AssertionError


################
# def hyp(a, b):
#     hyp = (a ** 2 + b ** 2) ** 0.5
#     return hyp
#
# try:
#     assert hyp(3, 4) == 5
# except AssertionError:
#     logging.warning("test failed")


############################
# logging.basicConfig(filename="Assertion_logs.log", level=logging.INFO, filemode='a')
#
# def avg(ranks):
#     try:
#         assert len(ranks) != 0, "No values"
#         logging.info("test passed")
#         return round(sum(ranks) / len(ranks), 2)
#     except AssertionError:
#         logging.warning("test failed")
#         print("AssertionError error happens")
#
# logging.basicConfig(filename="Assertion_logs.log", level=logging.INFO, filemode='a')
# ranks = [12, 22, 34]
# print("Среднее значение:", avg(ranks))
#
#
#
# ########################
# def avg(ranks):
#     try:
#         assert len(ranks) != 0, "No values"
#         logging.info("test passed")
#         return round(sum(ranks) / len(ranks), 2)
#     except AssertionError:
#         logging.warning("test failed")
#         print("AssertionError error happens")
#
# logging.basicConfig(filename="Assertion_logs.log", level=logging.INFO, filemode='a')
# ranks = []
# print("Среднее значение:", avg(ranks))

################
# def avg(ranks):
#     assert len(ranks) != 0, "No values"
#     return round(sum(ranks)/len(ranks), 2)
#
# ranks = [62, 65, 75]
# print("Среднее значение:", avg(ranks))


################
# def avg(ranks):
#     assert len(ranks) != 0
#     return round(sum(ranks)/len(ranks), 2)
#
# ranks = []
# print("Среднее значение:", avg(ranks))


################
# def divide(val1, val2):
#     assert val2 != 0, "Divisor is zero!"
#     return val1/val2
#
# print(divide(10, 0))


###################
# def divide(val1, val2):
#     assert val2 != 0 , 'Нельзя делить на 0'
#     return round(val1/val2, 2)
#
# z = divide(21,3)
# print(z)
#
# a = divide(21,0)
# print(a)


########################
# def divide(val1, val2):
#     try:
#         assert val2 != 0 , 'Нельзя делить на 0'
#         logging.info("test passed")
#         return round(val1/val2, 2)
#     except AssertionError:
#         logging.warning("test failed")
#         print("AssertionError happens. Divisor is zero!")
#
# logging.basicConfig(filename="Assertion_Divv_logs.log", level=logging.INFO, filemode='a')
#
# z = divide(21,3)
# print(z)
#
# a = divide(21,0)
# print(a)


################
# def dilennya(val1, val2):
#     try:
#         divv = val1 / val2
#     except ZeroDivisionError:
#         return "Division by zero!"
#     else:
#         return divv
#
# assert dilennya(5, 0) == "Division by zero!"

#
# def root(val1, val2):
#     assert val1 >= 0, "Impossible to find a root from negative number!"
#     return val1 ** (1 / val2)
#
# r = root(25, 2)
# print(r)
#
# rr = root(-25, 2)
# print(r)


def root2(val1, val2):
    assert val1 >= 0, "Root from negative number!"
    return val1 ** (1 / val2)

s = 'root'
if s == 'root':
    try:
        rrr = root2(-25, 2)   # rrr = root2(25, 2)
        print(rrr)
    except AssertionError:
        print("Impossible to find the root from negative number!!!")


