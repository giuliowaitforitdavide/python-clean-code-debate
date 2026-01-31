from .models import Shape, ShapeMetrics


def area_clean(fixtures: list) -> float:
    area = 0
    for fixture in fixtures:
        shape: Shape = fixture["shape"](fixture["a"], fixture["b"])
        area += shape.area()
    return area


def complex_value_clean(fixtures: list) -> float:
    complex_value = 0
    for fixture in fixtures:
        shape: Shape = fixture["shape"](fixture["a"], fixture["b"])
        complex_value += ShapeMetrics.complex_value(shape)
    return complex_value
