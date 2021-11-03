"""

"""

# def greeting(name):
#     if name[0].isupper():
#         return "Hello, " + name
#     else:
#         raise ValueError(f'{name} -- is inappropriate name')
#
# print(greeting("Anton"))
# # Hello, Anton
# print(greeting("anton"))
# # Traceback (most recent call last):
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Module2_Raise.py", line 12, in <module>
# #     print(greeting("anton"))
# #   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Module2_Raise.py", line 9, in greeting
# #     raise ValueError(f'{name} -- is inappropriate name')
# # ValueError: anton -- is inappropriate name


def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError

while True:
    try:
        name = input("Please, enter your name: ")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Try again")
    else:
        print("ELSE: GOOD")
        break
