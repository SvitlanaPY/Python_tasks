from Polymorphism_ex1 import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)
print(rect1.get_rect_area(), rect2.get_rect_area())

square1 = Square(5)
square2 = Square(7)
print(square1.get_square_area(), square2.get_square_area())

circle1 = Circle(3)
circle2 = Circle(2)
print(circle1.get_circle_area(), circle2.get_circle_area())


figures = [rect1, rect2, square1, square2, circle1, circle2]
for figure in figures:
    if isinstance(figure, Rectangle):   # якщо figure належить до класу Rectangle
        print(figure.get_rect_area())
    elif isinstance(figure, Circle):
        print(figure.get_circle_area())
    else:
        print(figure.get_square_area())
