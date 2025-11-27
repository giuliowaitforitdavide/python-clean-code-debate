from typing import Generator, Optional

import pytest
from tabulate import tabulate

from src.models import Shape
from tests.factories import ShapeFactory


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item) -> Generator[None, None, Optional[None]]:
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and hasattr(item, "performance_data"):
        results = item.performance_data
        if (clean_execution_time := results.get("clean_execution_time")) and (
            unreadable_execution_time := results.get("unreadable_execution_time")
        ):
            table = [
                [
                    "Execution time (clean code)",
                    "Execution time (unreadable code)",
                    "Performance improvement",
                ],
                [
                    round(clean_execution_time, 2),
                    round(unreadable_execution_time, 2),
                    f"{round(100 * (clean_execution_time - unreadable_execution_time) / clean_execution_time, 2)} %",
                ],
            ]

            if report.passed or report.failed:
                tw: pytest.TerminalReporter = item.config.get_terminal_writer()
                tw.line()
                tw.line("Performance Results:", bold=True, black=True)
                tw.line(tabulate(table, headers="firstrow", tablefmt="fancy_grid"))


@pytest.fixture
def performance_results(request: pytest.FixtureRequest) -> Generator[dict, None, None]:
    """Fixture to store performance results for test reporting."""
    results = {}
    request.node.performance_data = results
    yield results


@pytest.fixture
def shapes() -> list[Shape]:
    return [ShapeFactory.build() for _ in range(50_000)]


@pytest.fixture
def executions() -> int:
    return 1000
