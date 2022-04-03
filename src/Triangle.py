import math
from src.base_class import Figure
from src.Square import square

Triangle = Figure()


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = 'Triangle'
        print(self.get_perimeter)
        print(self.get_area)
        print(self.name)
        self.add_area

    @property
    def get_perimeter(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return self.a + self.b + self.c
        else:
            print(None)

    @property
    def half_of_perimeter(self):
        return self.get_perimeter / 2

    @property
    def get_area(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return math.sqrt(self.half_of_perimeter * (self.half_of_perimeter - self.a) *
                             (self.half_of_perimeter - self.b) * (self.half_of_perimeter - self.c))
        else:
            print(None)


triangle = Triangle(5, 6, 4)
print(triangle.add_area(square))
