"""
Создайте класс Point. У этого класса должны быть

метод set_coordinates, который принимает координаты по x и по y,
и сохраняет их в экземпляр класса соответственно в атрибуты x и y
метод get_distance, который обязательно принимает экземпляр класса Point
и возвращает расстояние между двумя точками по теореме Пифагора.
В случае, если в данный метод передается не экземпляр класса Point необходимо вывести сообщение "Передана не точка"
Пример работы с классом Point

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2) # вернёт 5.0
p1.get_distance(10) # Распечатает "Передана не точка"
"""


class Point:
    def set_coordinates(self, coord_x, coord_y):
        self.x = coord_x
        self.y = coord_y

    def get_distance(self, arg):
        if isinstance(arg, Point):
            return ((self.x - arg.x) ** 2 + (self.y - arg.y) ** 2) ** 0.5
        else:
            print(f"Передана НЕ точка")


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
d = p1.get_distance(p2)  # вернёт 5.0
print("d=", d)
dd = p1.get_distance(10)
print("dd=", dd)  # Распечатает "Передана не точка"
