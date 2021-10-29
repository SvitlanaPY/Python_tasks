
def first():
    print('start first')
    print('finish first')

print('hello')
first()

#
# def first1():
#     print('start first')
#     1 / 0
#     print('finish first')
#
# print('hello1')
# first1()
# we will see two error messages:
# the first - about error in our main code where the function is called: line 15, in <module> first();
# the second error - about the line with error: line 11, in first 1 / 0


# def first2():
#     print('start one')
#     print('finish one')
#
# def second2():
#     print("start two")
#     second2()
#     print('finish two')
#
# print('-----------------------')
# print('hello2')
# first2()

"""
Коли Пайтон зустрічає виключення, то запускається механізм запуску виключень, який перевіряє, чи відбулось виключення в блоці try...except
Блоку немає, тому відбувається виключення. 
В останній стрічці покажеться рядок, де відбулось виключення, а вище всі рядки, де викликалась функція: 
цепочка/стек викликів ф-ії.

"""

"""here is an example of THREE error messages in Traceback"""
# def first3():
#     print('start one')
#     second3()
#     print('finish one')
#
# def second3():
#     print("start two")
#     1/0
#     print('finish two')
#
# print('-----------------------')
# print('hello3')
# first3()
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Exceptions_Egoroff2.py", line 53, in <module>
# #     first3()
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Exceptions_Egoroff2.py", line 43, in first3
# #     second3()
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Exceptions_Egoroff2.py", line 48, in second3
# #     1/0
# # ZeroDivisionError: division by zero
# #
# # Process finished with exit code 1


"""here is an example of FOUR error messages in Traceback"""
# def third4():
#     print('start third')
#     1/0
#     print('finish third')
#
# def second4():
#     print("start two")
#     third4()
#     print('finish two')
#
# def first4():
#     print('start one')
#     second4()
#     print('finish one')
#
# print('-----------------------')
# print('hello4')
# first4()
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Exceptions_Egoroff2.py", line 84, in <module>
# #     first4()
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Exceptions_Egoroff2.py", line 79, in first4
# #     second4()
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Exceptions_Egoroff2.py", line 74, in second4
# #     third4()
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Exceptions_Egoroff2.py", line 69, in third4
# #     1/0
# # ZeroDivisionError: division by zero
# #
# # Process finished with exit code 1


"""ОБРОБКА ВИКЛЮЧЕНЬ"""
# def third5():
#     print('start third')
#     try:
#         1/0
#     except ZeroDivisionError:
#         print("HANDLING ERROR")
#     print('finish third')
#
# def second5():
#     print("start two")
#     third5()
#     print('finish two')
#
# def first5():
#     print('start one')
#     second5()
#     print('finish one')
#
# print('-----------------------')
# print('hello5')
# first5()


"""
ВКЛАДЕНІСТЬ
"""
def third6():
    print('start third')
    1/0
    print('finish third')

def second6():
    print("start two")
    third6()
    print('finish two')

def first6():
    print('start one')
    try:
        second6()
    except ZeroDivisionError:
        print('HANDLING ERROR IN FIRST()')
    print('finish one')

print('-----------------------')
print('hello6')
first6()
# hello6
# start one
# start two
# start third
# HANDLING ERROR IN FIRST()
# finish one
