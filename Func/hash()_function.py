# hash() method to encode the data into unrecognisable value (for immutable objects)
int_val = 4
str_val = 'Test'
flt_val = 24.56
tuple_value = (1, 2, 3)
frozen_set = frozenset(tuple_value)
print("frozen_set: ", frozen_set)   # frozen_set:  frozenset({1, 2, 3})
bytes_value = bytes(4)
print("bytes_value: ", bytes_value)   # bytes_value:  b'\x00\x00\x00\x00'
complex_value = complex(2, -3)
print("complex_value: ", complex_value)   # complex_value:  (2-3j)


print("The integer hash value is : ", hash(int_val))
# The integer hash value is : 4
print("The string hash value is : ", hash(str_val))
# The string hash value is : -4621964286487436750
print("The float hash value is : " + str(hash(flt_val)))
# The float hash value is : 1291272085159665688
print("The tuple hash value is : ", hash(tuple_value))
# The tuple hash value is :  529344067295497451
print("The frozenset hash value is : ", hash(frozen_set))
# The frozenset hash value is :  -272375401224217160
print("The bytes hash value is : ", hash(bytes_value))
# The bytes hash value is :  8856133653819740529
print("The complex hash value is : ", hash(complex_value))
# The complex hash value is :  -3000007


# hash() method is not supported for mutable objects (unhashable types)
# TypeError: unhashable type: 'list'/'dict'/'set'
lst_value = [2, 4, 6]
dict_value = {}
set_value = {1, 2, 3, 4}

# print("The list hash value is : ", hash(lst_value))     # TypeError: unhashable type: 'list'
# print("The dict hash value is : ", hash(dict_value))    # TypeError: unhashable type: 'dict'
# print("The set hash value is : ", hash(set_value))      # TypeError: unhashable type: 'set'
