"""
Вспомним нашего приятеля с предыдущих уроков: класс Vector.

Ваша задача создать класс Vector, который хранит в себе вектор целых чисел.

У класса Vector есть:
конструктор __init__, принимающий произвольное количество аргументов.
Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка.
Причем значения должны хранится в порядке неубывания;

- переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом:
"Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по возрастанию;
"Пустой вектор", если наш вектор не хранит в себе значения.

- переопределить метод __add__ так, чтобы экземпляр класса Vector мог складываться:
---с целым числом, в результате должен получиться новый Vector,
у которого каждый элемент атрибута values увеличен на число
---с другим вектором такой же длины. В результате должен получиться новый Vector,
состоящий из суммы элементов, расположенных на одинаковых местах.
Если длины векторов различаются, выведите сообщение "Сложение векторов разной длины недопустимо";
---в случае, если вектор складывается с другим типом(не числом и не вектором),
нужнo вывести сообщение "Вектор нельзя сложить с <значением>"

-переопределить метод __mul__ так, чтобы экземпляр класса Vector мог умножаться
---на целое число. В результате должен получиться новый Vector,
у которого каждый элемент атрибута values умножен на переданное число;
---на другой вектор такой же длины. В результате должен получиться новый Vector,
состоящий из произведения элементов, расположенных на одинаковых местах.
Если длины векторов различаются, выведите сообщение "Умножение векторов разной длины недопустимо";
---в случае, если вектор умножается с другим типом(не числом и не вектором), нужны вывести сообщение "Вектор нельзя умножать с <значением>";

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
"""


class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
        self.values = sorted(self.values)

    def __add__(self, other):
        if isinstance(other, int):
            values2 = []
            for i in range(len(self.values)):
                values2.append(self.values[i] + other)
            return Vector(*values2)

        if isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return "Сложение векторов разной длины недопустимо"
            else:
                values3 = []
                for i in range(len(self.values)):
                    values3.append(self.values[i] + other.values[i])
                return Vector(*values3)

        return f"Вектор нельзя сложить с {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            values2 = []
            for i in range(len(self.values)):
                values2.append(self.values[i] * other)
            return Vector(*values2)

        if isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return "Сложение векторов разной длины недопустимо"
            else:
                values3 = []
                for i in range(len(self.values)):
                    values3.append(self.values[i] * other.values[i])
                return Vector(*values3)

        return f"Вектор нельзя умножать с {other}"

    def __str__(self):
        if self.values:     # = bool(self.values) = True
            return f"Вектор{tuple(self.values)}"   # = f"Вектор{*self.values, }"
        return "Пустой вектор"


v1 = Vector(1,2,3)
print(v1)
# "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2)
# "Вектор(3, 4, 5)"

v3 = v1 + v2
print(v3)
# "Вектор(4, 6, 8)"

v4 = v3 + 5
print(v4)
# "Вектор(9, 11, 13)"

v5 = v1 * 2
print(v5)
# "Вектор(2, 4, 6)"

print(v5 + 'hi')
# "Вектор нельзя сложить с hi"


# Ob1 = Vector(2, 2)
# # Ob2 = Vector(2, 3)
# Ob3 = Ob1 + 2
# print("Ob3", Ob3)
# print(Ob1 + 'hi')

# v1 = Vector(1, 2, 3)
# print("v1: ", v1)
# # "Вектор(1, 2, 3)"
#
# v2 = Vector(3, 4, 5)
# print("v2: ", v2)
# # "Вектор(3, 4, 5)"
#
# v03 = v1 + 5
# print("v03: ", v03)
# # "Вектор(6, 7, 8)"
#
# # v1 + 'hi'
# print(v1 + 'hi')
#
# v3 = v1 + v2
# print("v3: ", v3)
# # "Вектор(4, 6, 8)"
# #
# v4 = v3 + 5
# print("v4: ", v4)
# # "Вектор(9, 11, 13)"
#
# v7 = Vector(1, 2, 3, 4)
# v = v1 + v7
# print("v: ", v)
#
# v5 = v1 * 2
# print(v5)
# # "Вектор(2, 4, 6)"
#
# print(v5 + 'hi')
# # "Вектор нельзя сложить с hi"
