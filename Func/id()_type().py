print('\n"id() function"')
# The id() function returns a unique id for the specified object.
# - All objects in Python has its own unique id.
# - The id is assigned to the object when it is created.
# - The id is the object's memory address, and will be different for each time you run the program.
# (except for some object that has a constant unique id, like integers from -5 to 256)


# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(int_a), id(str_b), id(set_c), id(lst_d), id(dict_e))
# OUTPUT: 9790336 139929085498032 139929085495104 139929086388544 139929086345984

# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.append(4)
lst_d.append(5)
print(id(lst_d))
# OUTPUT: 139929086388544 (it differs with every new program run)


print('\n"type() function"')
# type() method returns class type of the argument(object) passed as parameter.
# type() function is mostly used for debugging purposes.

# Syntax:  type(object)
lst = [1, 2, 3]
tpl = (1, 2, 3)
dct = {1: 'one', 2: 'two', 3: 'three'}
st = {1, 2, 3}

print(type(lst) is list)
# # True
print(type(tpl) is tuple)
# # True
print(type(dct) is dict)
# # True
print(type(st) is set)
# # True
print(type(lst) is tuple)
# # False


# 3. Define the type of each object from step 1.
print(type(int_a), type(str_b), type(set_c), type(lst_d), type(dict_e))
# OUTPUT: <class 'int'> <class 'str'> <class 'set'> <class 'list'> <class 'dict'>
