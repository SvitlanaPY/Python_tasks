"""
Класи є callable, а результатом виклику класу - є екземпляр класу,
самі ж екземпляри класу НЕ підтримують операції виклику (не є callable),
але ми можемо за допомогою магічного методу __call__ додати їм цію поведінку.

11. The __call__ method enables Python programmers to write classes where the instances behave like functions
and can be called like a function.
Create a new class with __call__ method and define this call to return sum.

За допомогою цього магічного методу ми можемо позбутьсь замикання

"""

# (1)
class SumNumb:
    def __call__(self, *args):
        # summa = 0
        summa = sum(args)
        return summa
s = SumNumb()
print(s(1, 2, 3, 4, 5, 5))
# OUTPUT: 20


# (2)
class SumNumb:
    def __call__(self, *args):
        summa = 0
        for i in args:
            summa += i
        return summa

s = SumNumb()
print(s(1, 2, 3))
print(s(1, 2, 3))
# OUTPUT: 6 6


class Counter1:
    def __init__(self):
        print('init object, self')

    def __call__(self, *args, **kwargs):
        print('instance called, self')

b = Counter1()
print(b)   # <__main__.Counter object at 0x7fc46db42f70>
b()      # <__main__.Counter object at 0x7fc46db42f70>
# адреси в памяті співпадають !!!!!!!!!!!!!!!!!


class Counter:
    def __init__(self):
        self.counter = 0
        print('init object, self')

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f'Our instance called {self.counter} times')

c = Counter()
c()
c()
c()
# Our object called 1 times
# Our object called 2 times
# Our object called 3 times
# Якщо створити новий екземпляр, то counter буде відраховуватись з нуля


class Avg:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object, self')

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Our instance called {self.counter} times')

    def average(self):
        return self.summa / self.length


q = Avg()
print(q.counter)   # 0
print(q.summa)   # 0
q(3, 4, 5)
print(q.summa)    # 12
print(q.length)   # 3
q(1, 2)
print(q.summa)       # 15 (12 + 3)
print(q.length)      # 5 (3 + 2)

r = Avg()
r(1, 2, 3, 4, 5, 6)
print(r.average())   # 3.5
