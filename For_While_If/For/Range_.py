print(list(range(11)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(range(10, 0, -1)))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(sum(range(1, 101)))
# 5050

print(len(range(5, 16, 5)))
# 3

a, b, c = range(5, 8)
print("a=", a, "b=", b, "c=", c)

r = list(range(10, 21))
print("r: ", r)
# r:  [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(list(range(-10, -21, -2)))
# [-10, -12, -14, -16, -18, -20]

rr = range(20, 31)
print("rr: ", rr)
# rr:  range(20, 31)
print(len(rr))
# 11
print("rr[2]: ", rr[2])
# rr[2]:  22

print(type(range(10)))
# <class 'range'>
# range() - є ітерабельним об"єктом, тобто це об"єкт, який дозволяє обходити всі свої елементи по черзі;
# З ітерабельного об"єкту можна отримати ітератор, застосувавши до нього ф-ію до ітерабельного об"єкту ф-ію iter().
# Ітератор - запам"ятовує/зберігає інформацію, який елемент буде братись наступним.
# Ітератор - це колекція, елементи якої можна обійти.
# При кожному виклику/застосуванні в ітератора ф-ії next(), ми будемо по черзі переходити до наступного елементу,
# і коли всі елементи ми обійдемо, то отримаємо іксепшин StopIteration.
# Ф-ію next() в ітератора можна викликати двома способами:
# v.__next__() або next(v)

# ITERABLE OBJECTS:
# range(), list, tuple, string, dict, bytes, bytearray

v = iter(range(5))
print(v)   # - v - є ітератором
# <range_iterator object at 0x7f3f0c70ff00>
print(v.__next__())   # 0
print(next(v))   # 1
print(v.__next__())   # 2
print(next(v))   # 3
print(v.__next__())   # 4
# print(next(v))    # StopIteration

n = iter([43, True, 'hello', 7])
print(next(n))    # 43
print(next(n))    # True
print(next(n))    # hello
print(next(n))    # 7

# Строки є теж ітерабельними об"єктами
m = iter('hello')
print(next(m))   # h
print(next(m))   # e
print(next(m))   # l
print(next(m))   # l
print(next(m))   # o
