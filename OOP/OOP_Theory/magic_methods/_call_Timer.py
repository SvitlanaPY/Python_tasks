from time import perf_counter


class Timer:

    def __init__(self, func):
        self.fn = func
        print(f'{self.fn}')   # <function factoriall at 0x7f1c027039d0>


    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Function {self.fn.__name__} called')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Function worked {finish - start}')
        return result

# @Timer
def factoriall(n):
    pr = 1
    for i in range(1, n+1):
        pr *= i
    return pr

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

factoriall = Timer(factoriall)
print(factoriall(7))
# ми викликаємо наш клас Timer і в якості параметру передаємо йому функцію factoriall() і в нього запуститься метод __init__,
# який збереже нам функцію factoriall(), яку ми передаємо в атрибут self.fn і при цьому створиться об"єкт factoriall класу Timer
# і тепер у def factoriall(n) в нас уже зберігається НЕ функція, а об"єкт класу Timer
print(factoriall)   # <__main__.Timer object at 0x7fd46cac7640>
print(factoriall(7))
# Function factoriall called
# Function worked 1.9408995285630226e-05
# 5040
