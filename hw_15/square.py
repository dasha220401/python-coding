from figure import Figure

class Square(Figure):
    def __init__(self, a, b, c, d):
        super().__init__()
        super().add_dot(a)
        super().add_dot(b)
        super().add_dot(c)
        super().add_dot(d)
        self.side = self.get_side()
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_side(self):
        return self.dots[0].distance(self.dots[1])

    def get_perimeter(self):
        return self.side * 4

    def get_area(self):
        return self.side ** 2