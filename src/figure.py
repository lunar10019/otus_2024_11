from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self) -> int | float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> int | float:
        pass

    def add_area(self, other_figure) -> int:
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        return int(self.area + other_figure.area)
