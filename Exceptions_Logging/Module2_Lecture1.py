# Syntax Error - code is NOT executed at all
print("This line is executed ")
class EventLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EventLengthMixin)
    pass


ml = MyList([1, 2, 3, 4])
ml.sort()
print(ml)

# OUTPUT: SyntaxError: invalid syntax