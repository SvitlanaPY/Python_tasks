# EXCEPTIONS - code is executed partly (untill error happens)
print("This line is executed ")

class EventLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EventLengthMixin):
    pass


ml = MyList([1, "aaa", 3, 4])
ml.sort()
print(ml)

#OUTPUT:     This line is executed
# ml.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'