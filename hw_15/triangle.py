from figure import Figure
import math

class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__()
        super().add_dot(a)
        super().add_dot(b)
        super().add_dot(c)
        self.sides = self.get_sides()
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_sides(self):
        return [self.dots[0].distance(self.dots[1]),
                self.dots[1].distance(self.dots[2]),
                self.dots[2].distance(self.dots[0])]

    def get_perimeter(self):
        perimeter = 0
        for side in self.sides:
            perimeter += side
        return perimeter

    def get_area(self):
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter
                         * (semi_perimeter - self.sides[0])
                         * (semi_perimeter - self.sides[1])
                         * (semi_perimeter - self.sides[2]))
