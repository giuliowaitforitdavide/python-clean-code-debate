# python-clean-code-debate

A performance comparison project demonstrating different coding approaches in Python: clean code patterns vs unreadable implementations.

## 📋 Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager

### Installing uv

If you don't have `uv` installed, you can install it using one of the following methods:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Using pip:**
```bash
pip install uv
```

## 🚀 Setup

1. **Clone the repository** (if you haven't already):
```bash
git clone https://github.com/giuliowaitforitdavide/python-clean-code-debate.git
cd python-clean-code-debate
```

2. **Create a virtual environment and install dependencies**:
```bash
uv sync
```

This command will:
- Create a virtual environment (if it doesn't exist)
- Install all project dependencies from `pyproject.toml`
- Install development dependencies (pytest, factory-boy, ruff)
- Lock dependencies in `uv.lock`

3. **Activate the virtual environment**:

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```powershell
.venv\Scripts\activate
```

## 🧪 Running Tests

### Run All Tests

To run all performance benchmarks:

```bash
pytest
```

Or using the Makefile:

```bash
make complete-benchmark
```

### Run Specific Benchmarks

The project includes three specific performance tests comparing different approaches:

**1. Polymorphism Benchmark**
```bash
make poly-benchmark
```
or
```bash
pytest -q tests/test_performance.py::test_performance_polymorphism
```

**2. Internals Benchmark**
```bash
make internals-benchmark
```
or
```bash
pytest -q tests/test_performance.py::test_performance_internals
```

**3. Simple Benchmark**
```bash
make simple-benchmark
```
or
```bash
pytest -q tests/test_performance.py::test_performance_simple
```

### Verbose Test Output

For more detailed test output, remove the `-q` flag:
```bash
pytest tests/test_performance.py -v
```

## 📂 Project Structure

```
python-clean-code-debate/
├── src/                    # Source code
│   ├── __init__.py        
│   ├── models.py          # Shape models (Circle, Rectangle, Square, Triangle)
│   ├── clean_code.py      # Clean code implementation
│   ├── polymorphism.py    # S.O.L.I.D. unreadable implementation
│   ├── internals.py       # T.D.A. unreadable implementation
│   └── simple.py          # K.I.S.S. unreadable implementation
├── factories/             # Test data factories
│   ├── __init__.py
│   └── shape_factories.py # Factory Boy factories for shapes
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── conftest.py        # Pytest fixtures
│   └── test_performance.py # Performance tests
├── Makefile               # Build and test automation
├── pyproject.toml         # Project configuration
├── uv.lock                # Locked dependencies
└── README.md              # This file
```

## 🔧 Development

### Code Formatting and Linting

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and formatting:

**Check for issues:**
```bash
ruff check .
```

**Auto-fix issues:**
```bash
ruff check --fix .
```

**Format code:**
```bash
ruff format .
```

### Adding New Dependencies

**Add a runtime dependency:**
```bash
uv add <package-name>
```

**Add a development dependency:**
```bash
uv add --dev <package-name>
```

## 📊 What This Project Tests

This project compares the performance of different coding approaches:

1. **Clean Code Approach**: Follows clean code principles with emphasis on readability
2. **Polymorphism Unreadable Implementation**: Show how using S.O.L.I.D. principles affect performance
3. **Internals Unreadable Implementation**: Show how using T.D.A. principles affect performance
4. **Simple Unreadable Implementation**: Show how using K.I.S.S. principles affect performance

Each test measures execution time to demonstrate the performance trade-offs between clean, readable code and unreadable implementations.

## 📝 License

See [LICENSE](LICENSE) file for details.
