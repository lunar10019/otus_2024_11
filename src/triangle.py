import math

from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float, side_c: int | float):
        # Проверка на тип аргументов
        args = [side_a, side_b, side_c]
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Should be a number")

        # Проверка что стороны треугольника не могут быть меньше 0
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Triangle sides can't be less than 0")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self) -> int:
        # Проверка на возможность существования треугольника
        if (
            self.side_a + self.side_b <= self.side_c
            or self.side_a + self.side_c <= self.side_b
            or self.side_b + self.side_c <= self.side_a
        ):
            raise ValueError("A triangle with these sides does not exist")

        # Полупериметр
        s = (self.side_a + self.side_b + self.side_c) / 2

        # Площадь по формуле Герона
        area = math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        return int(area)

    @property
    def perimeter(self) -> int:
        return int(self.side_a + self.side_b + self.side_c)
