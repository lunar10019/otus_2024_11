from src.figures.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a: int | float):
        if side_a <= 0:
            raise ValueError("Square sides can't be less than 0")
        super().__init__(side_a, side_a)
