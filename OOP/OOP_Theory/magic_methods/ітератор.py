a = [1, 2, 3, 4, 5]
b = iter(a)
print(b)   # <list_iterator object at 0x7f1ad0f7b2e0>
print(next(b))   # 1
print(next(b))   # 2
print(next(b))   # 3
print(next(b))   # 4
print(next(b))   # 5
# print(next(b))   # StopIteration
с = a.__iter__()
print(с)   # <list_iterator object at 0x7f1900f77d00>
print(с.__next__())   # 1
print(с.__next__())   # 2
print(с.__next__())   # 3
print(с.__next__())   # 4


