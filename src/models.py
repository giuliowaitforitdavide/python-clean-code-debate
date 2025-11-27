import math


class Shape:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def _get_complex_things(self) -> float:
        return self.get_area() / (1 + self.get_sides())

    def get_area(self) -> float:
        raise NotImplementedError()

    def get_sides(self) -> int:
        raise NotImplementedError()

    def get_complex_things(self) -> float:
        raise NotImplementedError()


class Rectangle(Shape):
    def get_area(self) -> float:
        return self.a * self.b

    def get_sides(self) -> float:
        return 4

    def get_complex_things(self) -> float:
        return super()._get_complex_things()


class Square(Shape):
    def get_area(self) -> float:
        return self.a * self.b

    def get_sides(self) -> float:
        return 4

    def get_complex_things(self) -> float:
        return super()._get_complex_things()


class Triangle(Shape):
    def get_area(self) -> float:
        return 0.5 * self.a * self.b

    def get_sides(self) -> float:
        return 3

    def get_complex_things(self) -> float:
        return super()._get_complex_things()


class Circle(Shape):
    def get_area(self) -> float:
        return math.pi * self.a * self.b

    def get_sides(self) -> float:
        return 0

    def get_complex_things(self) -> float:
        return super()._get_complex_things()


if __name__ == "__main__":
    print(Circle(1, 1).get_complex_things())
