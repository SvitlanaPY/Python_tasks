# def greeting(name):
#     if name[0].isupper():
#         return "Hello, " + name
#     else:
#         raise ValueError(f'{name} -- is inappropriate name')
#
# print(greeting("Anton"))
# print(greeting("anton"))


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
