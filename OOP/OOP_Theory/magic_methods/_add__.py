




""" 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value
which is greater than 10. And perform this add (+) of two instances.
"""

class Dodavannya:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):   # self = a1, other = a2
        if other.value > 10 or self.value > 10:    # other.value = a2.value (attribute of the second object a2); self.value = a1.value
            return other.value * self.value
        else:
            return other.value + self.value


a1 = Dodavannya(11)
a2 = Dodavannya(7)
print(a1 + a2)
# OUTPUT: 77
b1 = Dodavannya(5)
b2 = Dodavannya(3)
print(b1 + b2)
# OUTPUT: 8
