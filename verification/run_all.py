"""Run the two finite scientific checks and compare committed reference data."""
import json
import math
from pathlib import Path
import sys

import numpy
import scipy

from check_autonomous_bath import run_check as fixed_check
from check_autonomous_adaptive_times import run_check as adaptive_check


def compare(actual, expected, path="result"):
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or actual.keys() != expected.keys():
            raise ValueError(f"{path}: dictionary keys differ")
        for key in expected:
            compare(actual[key], expected[key], f"{path}.{key}")
    elif isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise ValueError(f"{path}: list lengths differ")
        for i, (a, e) in enumerate(zip(actual, expected)):
            compare(a, e, f"{path}[{i}]")
    elif isinstance(expected, (int, float)):
        if not math.isfinite(actual) or not math.isclose(
            actual, expected, rel_tol=2e-8, abs_tol=2e-10
        ):
            raise ValueError(f"{path}: {actual!r} differs from {expected!r}")
    elif actual != expected:
        raise ValueError(f"{path}: values differ")


def main():
    if sys.flags.optimize:
        raise RuntimeError("Run without -O: numerical inequality checks use assertions.")
    root = Path(__file__).resolve().parent
    cases = [
        ("fixed-time", "check_autonomous_bath_results.json", fixed_check),
        ("adaptive-time", "check_autonomous_adaptive_times_results.json", adaptive_check),
    ]
    for name, filename, check in cases:
        expected = json.loads((root / filename).read_text())
        actual = check()
        compare(actual, expected, name)
        print(f"PASS: {name}; analytic inequalities, trace and reference output checked")
    print(f"Python {sys.version.split()[0]}; NumPy {numpy.__version__}; SciPy {scipy.__version__}")
    print("Two finite examples reproduced. Universal bounds rely on the written proofs.")


if __name__ == "__main__":
    main()
