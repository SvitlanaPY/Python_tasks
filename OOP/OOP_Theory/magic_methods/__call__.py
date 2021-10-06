







"""
11. The __call__ method enables Python programmers to write classes where the instances behave like functions
and can be called like a function.
Create a new class with __call__ method and define this call to return sum.
"""

# (1)
class SumNumb:
    def __call__(self, *args):
        summa = 0
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
