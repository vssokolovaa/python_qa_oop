from src.Triangle import Triangle
from src.Rectangle import Rectangle
import pytest


class Test():
    def __init__(self, a, b):
        self.a = a
        self.b = b


@pytest.mark.positive
def test_create_triangle_perimeter():
    triangle = Triangle(13, 14, 19)
    assert triangle.get_perimeter == 46


@pytest.mark.positive
def test_create_triangle_area():
    triangle = Triangle(5, 29, 30)
    assert triangle.get_area == 72


@pytest.mark.positive
def test_create_triangle_add_area():
    triangle = Triangle(5, 29, 30)
    rectangle = Rectangle(3, 4)
    r = triangle.add_area(rectangle)
    assert r == 84


@pytest.mark.negative
def test_create_negative_triangle_perimeter():
    triangle = Triangle(1, 2, 9)
    assert triangle.get_perimeter == None


@pytest.mark.negative
def test_create_negative_triangle_area():
    triangle = Triangle(1, 2, 9)
    assert triangle.get_area == None


@pytest.mark.negative
def test_create_negative_null_triangle_perimeter():
    triangle = Triangle(0, 0, 0)
    assert triangle.get_perimeter == None


@pytest.mark.negative
def test_create_negative_null_triangle_area():
    triangle = Triangle(0, 0, 0)
    assert triangle.get_area == None


@pytest.mark.negative
def test_create_triangle_add_negative_area():
    with pytest.raises(ValueError):
        triangle = Triangle(5, 29, 30)
        rectangle = Test(3, 4)
        r = triangle.add_area(rectangle)
        assert (str(r.value)) == 'ValueError Incorrect class'
