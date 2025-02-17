import pytest

from src.figures.triangle import Triangle
from src.figures.circle import Circle


# func area
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [(10, 12, 15, 59), (11.2, 13.44, 10.1, 55)],
    ids=["integer", "float"],
)
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert (
        t.area == area
    ), f"Triangle area with sides {side_a} and {side_b} and {side_c} must be {t.area}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (0, 0, 0),
        (-100, -12, -13),
        ("", "", ""),
        (Circle, Triangle, Circle),
        (10, 10, 20),
    ],
    ids=[
        "zero value",
        "negative value",
        "string type",
        "Class",
        "triangle doesn't exist",
    ],
)
def test_triangle_area_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


# func perimeter
@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimeter"),
    [(10, 12, 14, 36), (11.2, 7.2, 16.2, 34)],
    ids=["integer", "float"],
)
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert (
        r.perimeter == perimeter
    ), f"Triangle perimeter with sides {side_a} and {side_b} and {side_c} must be {r.perimeter}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (0, 0, 0),
        (-100, -90, -12),
        ("", "", ""),
        (Circle, Triangle, Circle),
        (10, 10, 20),
    ],
    ids=[
        "zero value",
        "negative value",
        "string type",
        "Class",
        "triangle doesn't exist",
    ],
)
def test_triangle_perimeter_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


# func add_area
@pytest.mark.parametrize(
    ("expected_area", "side_a", "side_b", "side_c"),
    [(348, 12, 10, 21)],
    ids=["integer"],
)
def test_triangle_add_area_positive(expected_area, side_a, side_b, side_c):
    c = Circle(radius=10)
    t = Triangle(side_a, side_b, side_c)
    total_sum = t.add_area(c)
    assert total_sum == expected_area, f"Triangle and circle areas must be {total_sum}"


@pytest.mark.parametrize(
    "other_class", ["", 0, -100], ids=["string", "zero value", "negative value"]
)
def test_triangle_add_area_negative(other_class):
    r = Triangle(10, 10, 10)
    with pytest.raises(ValueError):
        r.add_area(other_class)
