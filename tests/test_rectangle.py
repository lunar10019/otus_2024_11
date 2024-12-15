import pytest

from src.rectangle import Rectangle
from src.circle import Circle


# func area
@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [(10, 12, 120), (11.2, 13.44, 150)],
    ids=["integer", "float"],
)
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert (
        r.area == area
    ), f"Rectangle area with sides {side_a} and {side_b} must be {r.area}"


@pytest.mark.parametrize(
    "side_a, side_b",
    [(0, 0), (-100, -12), ("", ""), (Circle, Rectangle)],
    ids=["zero value", "negative value", "string type", "Class"],
)
def test_rectangle_area_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


# func perimeter
@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"),
    [(10, 62, 144), (11.2, 70.2, 162)],
    ids=["integer", "float"],
)
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert (
        r.perimeter == perimeter
    ), f"Rectangle perimeter with sides {side_a} and {side_b} must be {r.perimeter}"


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [(0, 0), (-100, -90), ("", ""), (Circle, Rectangle)],
    ids=["zero value", "negative value", "string type", "Class"],
)
def test_rectangle_perimeter_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


# func add_area
circle = Circle(radius=10)


@pytest.mark.parametrize(
    ("other_class", "add_area", "side_a", "side_b"),
    [(circle, 1538, 12, 102)],
    ids=["other class"],
)
def test_rectangle_add_area_positive(other_class, add_area, side_a, side_b):
    r = Rectangle(side_a, side_b)
    total_sum = r.add_area(other_class)
    assert total_sum == add_area, f"Rectangle and circle areas must be {total_sum}"


@pytest.mark.parametrize(
    "other_class", ["", 0, -100], ids=["string", "zero value", "negative value"]
)
def test_rectangle_add_area_negative(other_class):
    r = Rectangle(10, 10)
    with pytest.raises(ValueError):
        r.add_area(other_class)
