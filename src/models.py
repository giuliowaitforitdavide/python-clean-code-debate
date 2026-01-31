import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def sides(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float, *args: object, **kwargs: object) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def sides(self) -> int:
        return 4


class Square(Shape):
    def __init__(self, side: float, *args: object, **kwargs: object) -> None:
        self.side = side

    def area(self) -> float:
        return self.side**2

    def sides(self) -> int:
        return 4


class Triangle(Shape):
    def __init__(self, base: float, height: float, *args: object, **kwargs: object) -> None:
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def sides(self) -> int:
        return 3


class Circle(Shape):
    def __init__(self, radius: float, *args: object, **kwargs: object) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

    def sides(self) -> int:
        return 0


class ShapeMetrics:
    @staticmethod
    def complex_value(shape: Shape) -> float:
        return shape.area() / (1 + shape.sides())


ShapeMetrics.complex_value(Circle(5))
ShapeMetrics.complex_value(Square(4))
