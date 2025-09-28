"""Assignment 3 – Exercise 4: Interactive Menu Systems"""

from __future__ import annotations

import sys
from typing import Callable, Dict, List


def show_menu() -> None:
    print("\n=== STUDENT MENU ===")
    print("1. Add student")
    print("2. List students")
    print("3. Average score")
    print("4. Remove student")
    print("0. Exit")


def add_student(roster: Dict[str, List[float]]) -> None:
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be blank.")
        return
    if name in roster:
        print("Student already exists.")
        return
    scores: List[float] = []
    while True:
        entry = input("Enter score (blank to finish): ").strip()
        if entry == "":
            break
        try:
            score = float(entry)
        except ValueError:
            print("Please enter a number.")
            continue
        if 0 <= score <= 100:
            scores.append(score)
        else:
            print("Score must be between 0 and 100.")
    roster[name] = scores
    print(f"Added {name} with {len(scores)} scores.")


def list_students(roster: Dict[str, List[float]]) -> None:
    if not roster:
        print("No students available.")
        return
    print("\nCURRENT STUDENTS")
    for name, scores in roster.items():
        display_scores = ", ".join(f"{score:.1f}" for score in scores) or "No scores"
        print(f"- {name}: {display_scores}")


def class_average(roster: Dict[str, List[float]]) -> None:
    total = 0.0
    count = 0
    for scores in roster.values():
        for score in scores:
            total += score
            count += 1
    if count == 0:
        print("No scores to average.")
        return
    print(f"Class average: {total / count:.2f}")


def remove_student(roster: Dict[str, List[float]]) -> None:
    name = input("Student name to remove: ").strip()
    if name in roster:
        del roster[name]
        print(f"Removed {name}.")
    else:
        print("Student not found.")


def main() -> None:
    roster: Dict[str, List[float]] = {}
    actions: Dict[str, Callable[[Dict[str, List[float]]], None]] = {
        "1": add_student,
        "2": list_students,
        "3": class_average,
        "4": remove_student,
    }

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            sys.exit(0)
        action = actions.get(choice)
        if action:
            action(roster)
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
