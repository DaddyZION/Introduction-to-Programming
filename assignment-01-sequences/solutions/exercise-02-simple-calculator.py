"""Assignment 1 – Exercise 2: Simple Calculator

A command-line calculator that performs several arithmetic operations on two
numbers. Division-based operations fail gracefully if division by zero is
attempted.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Tuple


@dataclass
class OperationResult:
    label: str
    value: str


def safe_division(numerator: float, denominator: float, *, operation: str) -> str:
    """Perform a division-style operation, handling division by zero."""

    if denominator == 0:
        return "undefined (division by zero)"

    if operation == "division":
        return f"{numerator / denominator:.2f}"
    if operation == "floor":
        return str(int(numerator // denominator))
    if operation == "modulus":
        return str(numerator % denominator)

    raise ValueError(f"Unsupported division operation: {operation}")


def build_results(a: float, b: float) -> Tuple[OperationResult, ...]:
    """Return a tuple of formatted operation results."""

    operations: Dict[str, Callable[[float, float], str]] = {
        "Addition": lambda x, y: f"{x + y:.2f}",
        "Subtraction": lambda x, y: f"{x - y:.2f}",
        "Multiplication": lambda x, y: f"{x * y:.2f}",
        "Division": lambda x, y: safe_division(x, y, operation="division"),
        "Floor Division": lambda x, y: safe_division(x, y, operation="floor"),
        "Modulus": lambda x, y: safe_division(x, y, operation="modulus"),
        "Exponentiation": lambda x, y: f"{x ** y:.2f}",
    }

    return tuple(OperationResult(label=label, value=function(a, b)) for label, function in operations.items())


def ask_for_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("That wasn't a valid number. Please try again.")


def main() -> None:
    print("=== SIMPLE CALCULATOR ===")
    first = ask_for_float("Enter the first number: ")
    second = ask_for_float("Enter the second number: ")
    print()

    results = build_results(first, second)
    width = max(len(result.label) for result in results)

    print("Operation".ljust(width), "| Result")
    print("-" * width, "+", "-" * 12, sep="")

    for result in results:
        print(result.label.ljust(width), "|", result.value)


if __name__ == "__main__":
    main()
