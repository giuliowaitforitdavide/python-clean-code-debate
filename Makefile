poly-benchmark:
	pytest -q tests/test_performance.py::test_performance_polymorphism

internals-benchmark:
	pytest -q tests/test_performance.py::test_performance_internals

simple-benchmark:
	pytest -q tests/test_performance.py::test_performance_simple

complete-benchmark:
	pytest -q