from src.base_class import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.name = 'Rectangle'
        self.get_perimeter
        self.get_area

    @property
    def get_perimeter(self):
        return (self.a + self.b) * 2

    @property
    def get_area(self):
        return self.a * self.b


rectangle = Rectangle(5, 4)
print(rectangle.get_perimeter)
print(rectangle.get_area)
