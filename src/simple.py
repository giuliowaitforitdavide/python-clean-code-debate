import math


def function_should_do_one_thing(fixtures: list) -> float:
    complex_value = 0
    shape_type = {
        "Rectangle": 1 / (1 + 4),
        "Triangle": 0.5 / (1 + 3),
        "Square": 1 / (1 + 4),
        "Circle": math.pi / (1 + 0),
    }
    for fixture in fixtures:
        complex_value += shape_type[fixture["shape"].__name__] * fixture["a"] * fixture["b"]
    return complex_value


if __name__ == "__main__":
    pass
