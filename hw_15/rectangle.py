from figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b, c, d):
        super().__init__()
        super().add_dot(a)
        super().add_dot(b)
        super().add_dot(c)
        super().add_dot(d)
        self.sides = self.get_sides()
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_sides(self):
        return [self.dots[0].distance(self.dots[1]),
                self.dots[1].distance(self.dots[2])]

    def get_perimeter(self):
        return (self.sides[0] + self.sides[1]) * 2

    def get_area(self):
        return self.sides[0] * self.sides[1]