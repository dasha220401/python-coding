from figure import Figure
from point import Point
from square import Square
from triangle import Triangle
from rectangle import Rectangle

a = Point(0, 0)
b = Point(1, 0)
c = Point(1, 1)
d = Point(0, 1)
e = Point(1, 2)
f = Point(0, 2)
square = Square(a, b, c, d)
triangle = Triangle(a, b, e)
rectangle = Rectangle(a, b, e, f)
print("Square")
square.print()
print("perimeter = ", str(square.perimeter))
print("area = ", str(square.area))
print("Triangle")
square.print()
print("perimeter = ", str(triangle.perimeter))
print("area = ", str(triangle.area))
print("Rectangle")
square.print()
print("perimeter = ", str(rectangle.perimeter))
print("area = ", str(rectangle.area))
