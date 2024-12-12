from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: int | float, side_b: int | float):
        # Проверка на тип аргументов
        args = [side_a, side_b]
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("Should be a number")

        if side_a <= 0 or side_b <= 0:
            raise ValueError("Rectangle sides can't be less than 0")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self) -> int:
        return int(self.side_a * self.side_b)

    @property
    def perimeter(self) -> int:
        return int((self.side_a + self.side_b) * 2)
