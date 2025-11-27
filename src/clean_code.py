from .models import Shape


def get_area_clean_code(fixtures: list) -> float:
    area = 0
    for fixture in fixtures:
        shape: Shape = fixture["shape_type"](fixture["a"], fixture["b"])
        area += shape.get_area()
    return area


def get_complex_things_clean_code(fixtures: list) -> float:
    complex_things = 0
    for fixture in fixtures:
        shape: Shape = fixture["shape_type"](fixture["a"], fixture["b"])
        complex_things += shape.get_complex_things()
    return complex_things
