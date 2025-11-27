import math


def get_area_polymorphism(fixtures: list) -> float:
    area = 0
    for fixture in fixtures:
        if fixture["shape_type"].__name__ in ("Rectangle", "Square"):
            area += fixture["a"] * fixture["b"]
        elif fixture["shape_type"].__name__ == "Triangle":
            area += 0.5 * fixture["a"] * fixture["b"]
        elif fixture["shape_type"].__name__ == "Circle":
            area += math.pi * fixture["a"] * fixture["b"]
        else:
            raise ValueError(f"Unexpected shape type: {fixture['shape_type']}")
    return area


if __name__ == "__main__":
    pass
