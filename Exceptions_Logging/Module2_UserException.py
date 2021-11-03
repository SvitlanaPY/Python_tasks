class BadName(Exception):
    pass

def greeting(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(f'{name} -- is inappropriate name')

print(greeting("Anton"))
# Hello, Anton
print(greeting("anton"))
# Traceback (most recent call last):
#   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Module2_UserException.py", line 11, in <module>
#     print(greeting("anton"))
#   File "/home/svitlana/Projects/Python_Tasks/Exceptions_Logging/Module2_UserException.py", line 8, in greeting
#     raise BadName(f'{name} -- is inappropriate name')
# __main__.BadName: anton -- is inappropriate name
