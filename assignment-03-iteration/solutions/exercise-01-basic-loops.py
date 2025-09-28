"""Assignment 3 – Exercise 1: Basic Loop Practice"""

from __future__ import annotations

from typing import Iterable, List


def count_odds(numbers: Iterable[int]) -> int:
    count = 0
    for number in numbers:
        if number % 2 == 1:
            count += 1
    return count


def factorial(n: int) -> int:
    result = 1
    for value in range(2, n + 1):
        result *= value
    return result


def collect_until_stop(prompt: str = "Enter value (blank to finish): ") -> List[str]:
    values: List[str] = []
    while True:
        text = input(prompt).strip()
        if text == "":
            break
        values.append(text)
    return values


def sum_first_n(n: int) -> int:
    total = 0
    current = 1
    while current <= n:
        total += current
        current += 1
    return total


def demo() -> None:
    print("=== COUNT ODDS ===")
    sample = [1, 4, 7, 10, 13]
    print(sample, "->", count_odds(sample))

    print("\n=== FACTORIALS ===")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")

    print("\n=== TRIANGULAR NUMBERS ===")
    for n in range(1, 6):
        print(f"Sum of first {n} numbers = {sum_first_n(n)}")


if __name__ == "__main__":
    demo()
