class Vector:

    def __init__(self, *args):
        self.values = [val for val in args if isinstance(val, int)]

    def __str__(self):
        if self.values:
            return f'Вектор({", ".join(sorted(map(str, self.values)))})'
        else:
            return 'Пустой вектор'


v1 = Vector(5,1,2,3)
print(v1)
# "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)
# "Пустой вектор"
