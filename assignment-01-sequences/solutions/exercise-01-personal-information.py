"""Assignment 1 – Exercise 1: Personal Information Calculator

Collects personal details from the user and prints a nicely formatted summary
including the person's age next year and the number of years until retirement.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date


RETIREMENT_AGE = 65


@dataclass
class PersonInfo:
    """Container for an individual's demographic information."""

    name: str
    age: int
    birth_year: int

    @property
    def age_next_year(self) -> int:
        return self.age + 1

    @property
    def years_until_retirement(self) -> int:
        return max(0, RETIREMENT_AGE - self.age)

    def as_summary(self) -> str:
        return (
            "=== PERSONAL INFORMATION SUMMARY ===\n"
            f"Name: {self.name}\n"
            f"Current Age: {self.age}\n"
            f"Birth Year: {self.birth_year}\n"
            f"Age Next Year: {self.age_next_year}\n"
            f"Years Until Retirement ({RETIREMENT_AGE}): {self.years_until_retirement}"
        )


def ask_for_int(prompt: str, *, min_value: int | None = None, max_value: int | None = None) -> int:
    """Prompt the user for an integer, validating ranges when provided."""

    while True:
        raw_value = input(prompt).strip()
        if not raw_value:
            print("Please enter a value – it can't be blank.")
            continue

        try:
            value = int(raw_value)
        except ValueError:
            print("That wasn't a whole number. Try again.")
            continue

        if min_value is not None and value < min_value:
            print(f"Value must be at least {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Value must be no more than {max_value}.")
            continue

        return value


def collect_person_info() -> PersonInfo:
    """Gather a person's name, age, and birth year from the console."""

    name = input("Enter your name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter your name: ").strip()

    current_year = date.today().year
    age = ask_for_int("Enter your age: ", min_value=0, max_value=120)

    lowest_birth_year = current_year - 120
    birth_year = ask_for_int(
        "Enter your birth year: ",
        min_value=lowest_birth_year,
        max_value=current_year,
    )

    return PersonInfo(name=name, age=age, birth_year=birth_year)


def main() -> None:
    """Program entry point."""

    person = collect_person_info()
    print()
    print(person.as_summary())


if __name__ == "__main__":
    main()
