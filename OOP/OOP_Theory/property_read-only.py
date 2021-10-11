class Person:

    def __init__(self):
        self._name = None

    def name(self):
        print('name function called')
        return self._name

    # for read-only attribute
    n = property(fget=name, fset=None)

p = Person()
print(p.n)
# name function called
# None

setattr(p, 'n', 'rajav')
# AttributeError: can't set attribute
