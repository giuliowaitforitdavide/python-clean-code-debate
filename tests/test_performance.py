import timeit

from src.clean_code import area_clean, complex_value_clean
from src.internals import avoid_exposing_internals
from src.models import Shape
from src.polymorphism import prefer_polymorphism
from src.simple import function_should_do_one_thing


def test_performance_polymorphism(
    shapes: list[Shape], performance_results: dict, executions: int
) -> None:
    clean_execution_time = timeit.timeit(lambda: area_clean(shapes), number=executions)
    unreadable_execution_time = timeit.timeit(
        lambda: prefer_polymorphism(shapes), number=executions
    )

    performance_results["clean_execution_time"] = clean_execution_time
    performance_results["unreadable_execution_time"] = unreadable_execution_time

    assert unreadable_execution_time < clean_execution_time


def test_performance_internals(
    shapes: list[Shape], performance_results: dict, executions: int
) -> None:
    clean_execution_time = timeit.timeit(lambda: area_clean(shapes), number=executions)
    unreadable_execution_time = timeit.timeit(
        lambda: avoid_exposing_internals(shapes), number=executions
    )

    performance_results["clean_execution_time"] = clean_execution_time
    performance_results["unreadable_execution_time"] = unreadable_execution_time

    assert unreadable_execution_time < clean_execution_time


def test_performance_simple(
    shapes: list[Shape], performance_results: dict, executions: int
) -> None:
    clean_execution_time = timeit.timeit(lambda: complex_value_clean(shapes), number=executions)
    unreadable_execution_time = timeit.timeit(
        lambda: function_should_do_one_thing(shapes), number=executions
    )

    performance_results["clean_execution_time"] = clean_execution_time
    performance_results["unreadable_execution_time"] = unreadable_execution_time

    assert unreadable_execution_time < clean_execution_time
