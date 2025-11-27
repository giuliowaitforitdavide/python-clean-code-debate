import math

shape_type = {
    "Rectangle": 1 / (1 + 4),
    "Triangle": 0.5 / (1 + 3),
    "Square": 1 / (1 + 4),
    "Circle": math.pi / (1 + 0),
}


def get_complex_things_unreadable(fixtures: list) -> float:
    complex_things = 0
    for fixture in fixtures:
        complex_things += shape_type[fixture["shape_type"].__name__] * fixture["a"] * fixture["b"]
    return complex_things


if __name__ == "__main__":
    pass
