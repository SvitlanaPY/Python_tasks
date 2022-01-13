# lambda argument1, argument2, ... : expression
# lambda-operator may have an arbitrary number of arguments, but only one expression.
# Syntax - lambda arguments : expression

add = lambda x, y: x + y
print(add(2, 3))
# 5


# 18. Convert def foo(x, y) to lambda function:
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

foo = lambda x, y: x if x < y else y
print(foo(5, 3))
# OUTPUT: 3


# 19*. Convert  lambda function to regular function: foo = lambda x, y, z: z if y < x and x > z else y
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(5, 3, 1))
# OUTPUT: 1


a_ = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
a_.sort()
print("a_: ", a_)
# a_:  [8, 23, 41, 56, 65, 78, 95, 2354, 5000, 54512]


# sort the list a by the last number of each element:
a = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
def f(x):
    return x % 10

a.sort(key=f)   # key - це іменований аргумент, який приймає функцію
print("a: ", a)
# a:  [5000, 41, 54512, 23, 2354, 65, 95, 56, 78, 8]

# використовуючи lambda:
aa = [78, 56, 23, 8, 54512, 65, 95, 2354, 41, 5000]
aa.sort(key = lambda x: x % 10)
print("aa: ", aa)
# aa:  [5000, 41, 54512, 23, 2354, 65, 95, 56, 78, 8]


# y = kx + b --- лдінійне рівняння, де k та b є коефіцієнтами
def linear(k, b):
    return lambda x: x * k + b
graph1 = linear(2, 5)   # k = 2, b = 5
print(graph1(3))   # x = 3
# y = 2 * 3 + 5


listt = []

for i in range(20):
    listt.append(lambda x: x + i)
    r = listt[0](3)
    print("r: ", r)

# print("listt: ", listt)
# print("listt len: ", len(listt))
# print(listt[12], listt[2])

r = listt[0](3)
print(r)
# 22
