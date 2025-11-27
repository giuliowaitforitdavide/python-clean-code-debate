import timeit

from src.clean_code import get_area_clean_code, get_complex_things_clean_code
from src.internals import get_area_internals
from src.models import Shape
from src.polymorphism import get_area_polymorphism
from src.simple import get_complex_things_unreadable


def test_performance_polymorphism(
    shapes: list[Shape], performance_results: dict, executions: int
) -> None:
    clean_execution_time = timeit.timeit(lambda: get_area_clean_code(shapes), number=executions)
    unreadable_execution_time = timeit.timeit(
        lambda: get_area_polymorphism(shapes), number=executions
    )

    performance_results["clean_execution_time"] = clean_execution_time
    performance_results["unreadable_execution_time"] = unreadable_execution_time

    assert unreadable_execution_time < clean_execution_time


def test_performance_internals(
    shapes: list[Shape], performance_results: dict, executions: int
) -> None:
    clean_execution_time = timeit.timeit(lambda: get_area_clean_code(shapes), number=executions)
    unreadable_execution_time = timeit.timeit(lambda: get_area_internals(shapes), number=executions)

    performance_results["clean_execution_time"] = clean_execution_time
    performance_results["unreadable_execution_time"] = unreadable_execution_time

    assert unreadable_execution_time < clean_execution_time


def test_performance_simple(
    shapes: list[Shape], performance_results: dict, executions: int
) -> None:
    clean_execution_time = timeit.timeit(
        lambda: get_complex_things_clean_code(shapes), number=executions
    )
    unreadable_execution_time = timeit.timeit(
        lambda: get_complex_things_unreadable(shapes), number=executions
    )

    performance_results["clean_execution_time"] = clean_execution_time
    performance_results["unreadable_execution_time"] = unreadable_execution_time

    assert unreadable_execution_time < clean_execution_time
