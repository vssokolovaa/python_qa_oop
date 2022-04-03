import math

from src.Circle import Circle
from src.Triangle import Triangle
import pytest


class Test():
    def __init__(self, a, b):
        self.a = a
        self.b = b


@pytest.mark.positive
def test_create_circle_perimeter():
    circle = Circle(4)
    assert circle.get_perimeter == math.pi * 4 * 2


@pytest.mark.positive
def test_circle_rectangle_area():
    circle = Circle(4)
    assert circle.get_area == math.pi * 4 * 4


@pytest.mark.positive
def test_create_circle_add_area():
    circle = Circle(4)
    triangle = Triangle(5, 29, 30)
    r = circle.add_area(triangle)
    assert r == math.pi * 4 * 4 + 72


@pytest.mark.negative
def test_create_circle_add_negative_area():
    with pytest.raises(ValueError):
        circle = Circle(2)
        triangle = Test(3, 4)
        r = circle.add_area(triangle)
        assert (str(r.value)) == 'ValueError Incorrect class'
