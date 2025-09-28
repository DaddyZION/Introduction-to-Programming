"""Assignment 1 – Exercise 4: Rectangle Properties Calculator"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class Rectangle:
    length: float
    width: float

    @property
    def area(self) -> float:
        return self.length * self.width

    @property
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

    @property
    def diagonal(self) -> float:
        return math.sqrt(self.length**2 + self.width**2)


def ask_for_positive(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a numeric value.")
            continue

        if value <= 0:
            print("Measurements must be positive. Try again.")
            continue

        return value


def display_results(rectangle: Rectangle) -> None:
    print()
    print("=== RECTANGLE PROPERTIES ===")
    print(f"Length:  {rectangle.length:.2f} units")
    print(f"Width:   {rectangle.width:.2f} units")
    print(f"Area:    {rectangle.area:.2f} square units")
    print(f"Perimeter: {rectangle.perimeter:.2f} units")
    print(f"Diagonal:  {rectangle.diagonal:.2f} units")


def main() -> None:
    length = ask_for_positive("Enter the rectangle length: ")
    width = ask_for_positive("Enter the rectangle width: ")
    rectangle = Rectangle(length=length, width=width)
    display_results(rectangle)


if __name__ == "__main__":
    main()
