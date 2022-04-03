from src.Rectangle import Rectangle
from src.Triangle import Triangle
import pytest


class Test():
    def __init__(self, a, b):
        self.a = a
        self.b = b


@pytest.mark.positive
def test_create_rectangle_perimeter():
    rectangle = Rectangle(6, 3)
    assert rectangle.get_perimeter == 18


@pytest.mark.positive
def test_rectangle_rectangle_area():
    rectangle = Rectangle(6, 3)
    assert rectangle.get_area == 18


@pytest.mark.positive
def test_create_rectangle_add_area():
    rectangle = Rectangle(6, 3)
    triangle = Triangle(5, 29, 30)
    r = rectangle.add_area(triangle)
    assert r == 90


@pytest.mark.negative
def test_create_rectangle_add_negative_area():
    with pytest.raises(ValueError):
        rectangle = Rectangle(6, 3)
        circle = Test(3, 4)
        r = rectangle.add_area(circle)
        assert (str(r.value)) == 'ValueError Incorrect class'
