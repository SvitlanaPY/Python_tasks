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


print("# " * 15)


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def get_full_name(self):
        return f'{self.name} {self.surname}'


human1 = Human("Анна", "Тех")
print(human1.get_full_name)
# Анна Тех

human2 = Human("Olha", "Smith")
print(human2.get_full_name)
# Olha Smith
human2.name = 'Taya'
print(human2.get_full_name)
# Taya Smith
