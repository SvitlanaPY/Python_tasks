from Polymorphism_ex2 import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

square1 = Square(5)
square2 = Square(7)

circle1 = Circle(3)
circle2 = Circle(2)


figures = [rect1, rect2, square1, square2, circle1, circle2]
for figure in figures:
    print(figure, figure.get_area())
