class Calc:

    @staticmethod
    def add_nums(*args):
        return sum(args)

addnums = Calc()
print(addnums.add_nums(1, 2, 3, 5))
# OUTPUT: 6

print(Calc.add_nums(1, 2, 3, 5))
# OUTPUT: 6