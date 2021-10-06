class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)

    def __str__(self):
        if any(self.values):
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return f'Пустой вектор'


v1 = Vector(5,1,2,3)
print(v1)
# "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)
# "Пустой вектор"
