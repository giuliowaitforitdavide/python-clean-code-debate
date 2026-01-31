import math


def prefer_polymorphism(fixtures: list) -> float:
    area = 0
    for fixture in fixtures:
        if fixture["shape"].__name__ in ("Rectangle", "Square"):
            area += fixture["a"] * fixture["b"]
        elif fixture["shape"].__name__ == "Triangle":
            area += 0.5 * fixture["a"] * fixture["b"]
        elif fixture["shape"].__name__ == "Circle":
            area += math.pi * fixture["a"] * fixture["b"]
    return area


if __name__ == "__main__":
    pass
