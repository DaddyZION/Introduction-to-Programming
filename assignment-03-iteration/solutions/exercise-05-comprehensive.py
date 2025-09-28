"""Assignment 3 – Exercise 5: Comprehensive Loop Practice

Implements a classroom analytics dashboard combining accumulation, nested loops,
search, filter, and reporting.
"""

from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Dict, List


@dataclass
class Assessment:
    name: str
    score: float
    weight: float


@dataclass
class Student:
    name: str
    assessments: List[Assessment]

    @property
    def weighted_average(self) -> float:
        total_weight = sum(assessment.weight for assessment in self.assessments)
        if total_weight == 0:
            return 0.0
        weighted_sum = sum(assessment.score * assessment.weight for assessment in self.assessments)
        return weighted_sum / total_weight


def build_sample_classroom() -> List[Student]:
    return [
        Student(
            name="Alice",
            assessments=[
                Assessment("Quiz 1", 85, 0.1),
                Assessment("Project", 92, 0.4),
                Assessment("Final", 88, 0.5),
            ],
        ),
        Student(
            name="Ben",
            assessments=[
                Assessment("Quiz 1", 78, 0.1),
                Assessment("Project", 81, 0.4),
                Assessment("Final", 73, 0.5),
            ],
        ),
        Student(
            name="Chloe",
            assessments=[
                Assessment("Quiz 1", 95, 0.1),
                Assessment("Project", 89, 0.4),
                Assessment("Final", 94, 0.5),
            ],
        ),
    ]


def class_statistics(students: List[Student]) -> Dict[str, float]:
    averages = [student.weighted_average for student in students]
    highest = max(averages)
    lowest = min(averages)
    return {
        "class_average": mean(averages),
        "highest": highest,
        "lowest": lowest,
    }


def list_students_at_risk(students: List[Student], threshold: float = 70.0) -> List[str]:
    results: List[str] = []
    for student in students:
        if student.weighted_average < threshold:
            results.append(student.name)
    return results


def build_grade_distribution(students: List[Student]) -> Dict[str, int]:
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for student in students:
        average = student.weighted_average
        if average >= 90:
            distribution["A"] += 1
        elif average >= 80:
            distribution["B"] += 1
        elif average >= 70:
            distribution["C"] += 1
        elif average >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1
    return distribution


def print_report(students: List[Student]) -> None:
    print("=== CLASSROOM ANALYTICS REPORT ===")
    for student in students:
        print(f"\n{student.name} -> {student.weighted_average:.2f}")
        for assessment in student.assessments:
            print(f"  {assessment.name:<12} {assessment.score:>5.1f} (weight {assessment.weight:.2f})")

    stats = class_statistics(students)
    print("\nClass Average:", stats["class_average"])
    print("Highest Average:", stats["highest"])
    print("Lowest Average:", stats["lowest"])

    print("\nStudents at Risk (<70):")
    for name in list_students_at_risk(students):
        print(" -", name)

    print("\nGrade Distribution:")
    distribution = build_grade_distribution(students)
    for grade, count in distribution.items():
        print(f"{grade}: {count}")


def main() -> None:
    classroom = build_sample_classroom()
    print_report(classroom)


if __name__ == "__main__":
    main()
