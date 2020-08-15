import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print(self):
        print("x = ", str(self.x), "y = ", str(self.y))

    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)