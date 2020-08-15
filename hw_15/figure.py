class Figure:
    def __init__(self):
        self.dots = []

    def add_dot(self, point):
        self.dots.append(point)

    def print(self):
        for dot in self.dots:
            dot.print()
