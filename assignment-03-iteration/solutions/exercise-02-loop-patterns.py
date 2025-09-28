"""Assignment 3 – Exercise 2: Common Loop Patterns"""

from __future__ import annotations

from typing import Iterable, List, Tuple


def accumulator(values: Iterable[float]) -> float:
    total = 0.0
    for value in values:
        total += value
    return total


def find_first_negative(values: Iterable[int]) -> int | None:
    for value in values:
        if value < 0:
            return value
    return None


def filter_long_words(words: Iterable[str], length: int) -> List[str]:
    result = []
    for word in words:
        if len(word) >= length:
            result.append(word)
    return result


def map_to_squares(values: Iterable[int]) -> List[int]:
    squares = []
    for number in values:
        squares.append(number * number)
    return squares


def min_max(values: Iterable[int]) -> Tuple[int, int]:
    iterator = iter(values)
    try:
        first = next(iterator)
    except StopIteration:
        raise ValueError("min_max requires at least one value")

    current_min = current_max = first
    for value in iterator:
        if value < current_min:
            current_min = value
        if value > current_max:
            current_max = value
    return current_min, current_max


def demo() -> None:
    print("=== ACCUMULATOR ===")
    print(accumulator([2.5, 3.1, 4.4]))

    print("\n=== FIND FIRST NEGATIVE ===")
    print(find_first_negative([5, 3, -2, -9]))

    print("\n=== FILTER LONG WORDS ===")
    print(filter_long_words(["loop", "iteration", "for", "while"], length=5))

    print("\n=== MAP TO SQUARES ===")
    print(map_to_squares(range(6)))

    print("\n=== MIN MAX ===")
    print(min_max([4, 7, 1, 3, 9, 2]))


if __name__ == "__main__":
    demo()
