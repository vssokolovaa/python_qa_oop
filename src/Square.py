from src.base_class import Figure
from src.Rectangle import rectangle


class Square(Figure):
    def __init__(self, a):
        self.a = a
        self.name = 'Square'
        self.get_perimeter
        self.get_area

    @property
    def get_perimeter(self):
        return self.a * 4

    @property
    def get_area(self):
        return self.a * self.a


square = Square(5)
print(square.get_perimeter)
print(square.get_area)
print(square.add_area(rectangle))
