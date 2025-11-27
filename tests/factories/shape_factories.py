import factory

from src.models import Circle, Rectangle, Square, Triangle


class ShapeFactory(factory.Factory):
    class Meta:
        model = dict

    a = factory.Faker("pyfloat", min_value=1, max_value=100)
    b = factory.Faker("pyfloat", min_value=1, max_value=100)
    shape_type = factory.Faker("random_element", elements=[Rectangle, Square, Triangle, Circle])
