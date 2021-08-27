t = IndexError()
print(isinstance(t, IndexError))   # True - means that t is object of class IndexError
print(isinstance(t, LookupError))  #  True - means that t is object of class LookupError
print(isinstance(t, TypeError))  # False - means that t is NOT an object of class TypeError
print(isinstance(t, Exception))   # True - means that t is object of base class Exception

# print('Hello1')
# print('Hello2')
# print('Hello3')
# try:
#     {}[5]
# except LookupError:   # LookupError is parent class of KeyError and that's why we can catch KeyError
#     print('KeyError exception occured')
# print('Hello4')
# print('Hello5')


# we can call exceptions by ourselve:
# print('Hello1')
# print('Hello2')
# raise ValueError('Incorrect meaning')   # ValueError: Incorrect meaning
# print('Hello3')
# print('Hello4')
#

try:
    a = int(input(ford))
except:   # if no type of exception mentioned then all types are taken into account
    raise ValueError("MOE ABTO")   #  raise ValueError("MOE ABTO")   ValueError: MOE ABTO
