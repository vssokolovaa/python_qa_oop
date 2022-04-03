import math

from src.base_class import Figure
from src.Rectangle import rectangle


class Circle(Figure):
    def __init__(self, r):
        self.r = r
        self.name = 'Circle'
        self.get_perimeter
        self.get_area

    @property
    def get_perimeter(self):
        return 2 * self.r * math.pi

    @property
    def get_area(self):
        return self.r * self.r * math.pi


circle = Circle(5)
print(circle.get_perimeter)
print(circle.get_area)
print(circle.add_area(rectangle))
