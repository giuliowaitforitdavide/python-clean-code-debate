import factory

from src.models import Circle, Rectangle, Square, Triangle


class ShapeFactory(factory.Factory):
    class Meta:
        model = dict

    a = factory.Faker("pyfloat", min_value=1, max_value=100)
    b = factory.Faker("pyfloat", min_value=1, max_value=100)
    shape = factory.Faker(
        "random_element",
        elements=[
            Rectangle,
            Square,
            Triangle,
            Circle,
        ],
    )

    @factory.post_generation
    def adjust_parameters(self, create, extracted, **kwargs):
        if self["shape"] in (Square, Circle):
            self["b"] = self["a"]
