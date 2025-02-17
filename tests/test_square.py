import pytest

from src.figures.square import Square
from src.figures.circle import Circle


# func area
@pytest.mark.parametrize(
    ("side_a", "area"), [(10, 100), (11.2, 125)], ids=["integer", "float"]
)
def test_square_area_positive(side_a, area):
    s = Square(side_a)
    assert s.area == area, f"Square area with sides {side_a} must be {s.area}"


@pytest.mark.parametrize(
    "side_a",
    [-100, 0],
    ids=["negative value", "zero value"],
)
def test_square_area_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


# func perimeter
@pytest.mark.parametrize(
    ("side_a", "perimeter"), [(10, 40), (11.2, 44)], ids=["integer", "float"]
)
def test_square_perimeter_positive(side_a, perimeter):
    s = Square(side_a)
    assert (
        s.perimeter == perimeter
    ), f"Square perimeter with sides {side_a} must be {s.perimeter}"


@pytest.mark.parametrize(
    "side_a",
    [
        0,
        -100,
    ],
    ids=[
        "zero value",
        "negative value",
    ],
)
def test_square_perimeter_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


# func add_area
@pytest.mark.parametrize(("expected_area", "side_a"), [(414, 10)], ids=["integer"])
def test_square_add_area_positive(expected_area, side_a):
    c = Circle(radius=10)
    s = Square(side_a)
    total_sum = s.add_area(c)
    assert total_sum == expected_area, f"Square and circle areas must be {total_sum}"


@pytest.mark.parametrize("other_class", [0, -100], ids=["zero value", "negative value"])
def test_square_add_area_negative(other_class):
    s = Square(10)
    with pytest.raises(ValueError):
        s.add_area(other_class)
