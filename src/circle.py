import math

from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius: int | float):
        # Проверка на тип аргумента
        if not isinstance(radius, (int, float)):
            raise ValueError("Should be a number")

        # Проверка что радиус не меньше 0
        if radius <= 0:
            raise ValueError("Circle radius can't be less than 0")
        self.radius = radius

    @property
    def area(self) -> int:
        return int(math.pi * (self.radius**2))

    @property
    def perimeter(self) -> int:
        return int(2 * math.pi * self.radius)
