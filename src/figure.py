from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def area(self) -> int | float:
        pass

    @abstractmethod
    def perimeter(self) -> int | float:
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Should be a Figure")
        return self.area + other_figure.area
