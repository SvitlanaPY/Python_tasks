"""
Annotation - це такий інструмент, що дозволяє зробити наш код більш інформативним і
позбутись деяких проблем, пов"язаних із динамічною типізацією.

Аннотація змінних:
first: int = 100

Аннотація функцій:
def add_numbers(a: int, b: int) -> int:
    return a + b

Можна також задати значення по замовчуванню всередині ф-ії (вони проставляються після визначення типу змінної):
def add_numbers(a: int, b: int = 111) -> int:
    return a + b
(b: int = 111, значення по замовчуванню)

"""


def add_numbers(a: int, b: int = 111) -> int:
    return a + b


zero: int = 200
first: int = 100
print("add_numbers: ", add_numbers(zero, first))   # add_numbers:  300
print("add_numbers with default 'b': ", add_numbers(zero))   # add_numbers with default 'b':  311
print(first)
first = 'hello'  # Expected type 'int', got 'str' instead
print(first)
second: int = [1, 2, 3]

print("add_strs: ", add_numbers('zero', 'first'))
print("add_lsts: ", add_numbers([1, 2, 3], [4, 5, 6]))

print(add_numbers.__annotations__)
# {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
