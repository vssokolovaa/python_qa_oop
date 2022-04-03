from src.Square import Square
from src.Triangle import Triangle
import pytest


class Test():
    def __init__(self, a, b):
        self.a = a
        self.b = b


@pytest.mark.positive
def test_create_square_perimeter():
    square = Square(6)
    assert square.get_perimeter == 24


@pytest.mark.positive
def test_create_square_area():
    square = Square(6)
    assert square.get_area == 36


@pytest.mark.positive
def test_create_square_add_area():
    square = Square(6)
    triangle = Triangle(5, 29, 30)
    r = square.add_area(triangle)
    assert r == 108


@pytest.mark.negative
def test_create_square_add_negative_area():
    with pytest.raises(ValueError):
        square = Square(6)
        rectangle = Test(3, 4)
        r = square.add_area(rectangle)
        assert (str(r.value)) == 'ValueError Incorrect class'
