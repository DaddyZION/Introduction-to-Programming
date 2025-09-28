"""Assignment 2 – Exercise 1: Basic Conditions

Contains a handful of small decision-making utilities that demonstrate simple if,
if/else, and elif chains.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


WeatherAdvice = Literal["Take an umbrella", "Wear a jacket", "Enjoy the sunshine"]


@dataclass
class WeatherConditions:
    temperature_c: float
    is_raining: bool
    wind_speed_kmh: float


def weather_advice(conditions: WeatherConditions) -> WeatherAdvice:
    if conditions.is_raining:
        return "Take an umbrella"
    if conditions.temperature_c < 12 or conditions.wind_speed_kmh > 35:
        return "Wear a jacket"
    return "Enjoy the sunshine"


def grade_from_score(score: float) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def age_category(age: int) -> str:
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age < 13:
        return "Child"
    if age < 20:
        return "Teenager"
    if age < 65:
        return "Adult"
    return "Senior"


def validate_positive_number(value: float) -> str:
    if value < 0:
        return "Value must be positive"
    if value == 0:
        return "Value should be greater than zero"
    return "Value accepted"


def demo() -> None:
    print("=== WEATHER ADVICE ===")
    sample = WeatherConditions(temperature_c=18, is_raining=True, wind_speed_kmh=10)
    print("Example:", weather_advice(sample))

    print("\n=== GRADE CLASSIFICATION ===")
    for score in (95, 82, 74, 65, 40):
        print(f"Score {score} -> {grade_from_score(score)}")

    print("\n=== AGE CATEGORIES ===")
    for age in (4, 15, 32, 77):
        print(f"Age {age} -> {age_category(age)}")

    print("\n=== SIMPLE VALIDATION ===")
    for value in (-3, 0, 5):
        print(f"Input {value}: {validate_positive_number(value)}")


if __name__ == "__main__":
    demo()
