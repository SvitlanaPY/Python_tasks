# LAMBDA:
# (1)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (2)
# foo = lambda x, y, z: z if y < x and x > z else y

# 18. Convert (1) to lambda function
foo = lambda x, y: x if x < y else y
print(foo(5, 3))
# OUTPUT: 3

# 19*. Convert (2) to regular function
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(5, 3, 1))
# OUTPUT: 1

