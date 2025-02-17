import pytest

from src.figures.circle import Circle
from src.figures.square import Square


# func area
@pytest.mark.parametrize(
    ("radius", "area"), [(10, 314), (11.2, 394)], ids=["integer", "float"]
)
def test_circle_area_positive(radius, area):
    c = Circle(radius)
    assert c.area == area, f"Circle area with radius {radius} must be {c.area}"


@pytest.mark.parametrize(
    "radius",
    [0, -100, "", Circle],
    ids=["zero value", "negative value", "string type", "Class"],
)
def test_circle_area_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


# func perimeter
@pytest.mark.parametrize(
    ("radius", "perimeter"), [(10, 62), (11.2, 70)], ids=["integer", "float"]
)
def test_circle_perimeter_positive(radius, perimeter):
    c = Circle(radius)
    assert (
        c.perimeter == perimeter
    ), f"Circle perimeter with radius {radius} must be {c.perimeter}"


@pytest.mark.parametrize(
    "radius",
    [0, -100, "", Square],
    ids=["zero value", "negative value", "string type", "Class"],
)
def test_circle_perimeter_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


# func add_area
@pytest.mark.parametrize(("expected_area", "radius"), [(414, 10)], ids=["integer"])
def test_circle_add_area_positive(expected_area, radius):
    s = Square(side_a=10)
    c = Circle(radius)
    total_sum = c.add_area(s)
    assert total_sum == expected_area, f"Circle and square areas must be {total_sum}"


@pytest.mark.parametrize(
    "other_class", ["", 0, -100], ids=["string", "zero value", "negative value"]
)
def test_circle_add_area_negative(other_class):
    c = Circle(10)
    with pytest.raises(ValueError):
        c.add_area(other_class)
