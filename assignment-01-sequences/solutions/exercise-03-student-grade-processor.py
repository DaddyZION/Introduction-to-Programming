"""Assignment 1 – Exercise 3: Student Grade Processor

Collects data for three students, calculates averages, and renders a formatted
report highlighting the highest and lowest scores.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import List, Tuple


SCORES_PER_STUDENT = 4
NUMBER_OF_STUDENTS = 3


@dataclass
class StudentRecord:
    name: str
    scores: List[float]

    @property
    def average(self) -> float:
        return mean(self.scores)


def ask_for_float(prompt: str, *, min_value: float = 0.0, max_value: float = 100.0) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a numerical score.")
            continue

        if not (min_value <= value <= max_value):
            print(f"Score must be between {min_value} and {max_value}.")
            continue

        return value


def collect_student() -> StudentRecord:
    name = input("Enter student name: ").strip() or "Unknown Student"
    scores = [
        ask_for_float(f"  Score {index + 1}: ")
        for index in range(SCORES_PER_STUDENT)
    ]
    return StudentRecord(name=name, scores=scores)


def collect_students() -> List[StudentRecord]:
    print("Enter details for three students (four test scores each).")
    print()
    return [collect_student() for _ in range(NUMBER_OF_STUDENTS)]


def find_high_low(records: List[StudentRecord]) -> Tuple[Tuple[str, float], Tuple[str, float]]:
    all_scores: List[Tuple[str, float]] = []
    for record in records:
        for score in record.scores:
            all_scores.append((record.name, score))

    highest = max(all_scores, key=lambda item: item[1])
    lowest = min(all_scores, key=lambda item: item[1])
    return highest, lowest


def print_report(records: List[StudentRecord]) -> None:
    highest, lowest = find_high_low(records)

    print("\n=== STUDENT GRADE REPORT ===")
    print(f"Highest Score: {highest[1]:.1f} ({highest[0]})")
    print(f"Lowest Score:  {lowest[1]:.1f} ({lowest[0]})")
    print()

    header = f"{'Name':<20}{'Scores':<35}{'Average':>10}"
    print(header)
    print("-" * len(header))

    for record in records:
        scores_list = ", ".join(f"{score:.1f}" for score in record.scores)
        print(f"{record.name:<20}{scores_list:<35}{record.average:>10.2f}")


def main() -> None:
    records = collect_students()
    print_report(records)


if __name__ == "__main__":
    main()
