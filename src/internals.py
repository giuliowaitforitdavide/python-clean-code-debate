import math


def avoid_exposing_internals(fixtures: list) -> float:
    area = 0
    shape_type = {
        "Rectangle": 1,
        "Triangle": 0.5,
        "Square": 1,
        "Circle": math.pi,
    }

    for fixture in fixtures:
        area += shape_type[fixture["shape"].__name__] * fixture["a"] * fixture["b"]
    return area


if __name__ == "__main__":
    pass
