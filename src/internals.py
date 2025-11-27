import math

shape_type = {"Rectangle": 1, "Triangle": 0.5, "Square": 1, "Circle": math.pi}


def get_area_internals(fixtures: list) -> float:
    area = 0
    for fixture in fixtures:
        area += shape_type[fixture["shape_type"].__name__] * fixture["a"] * fixture["b"]
    return area


if __name__ == "__main__":
    pass
