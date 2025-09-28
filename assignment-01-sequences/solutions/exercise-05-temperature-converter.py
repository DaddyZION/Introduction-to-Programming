"""Assignment 1 – Exercise 5: Temperature Converter"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class TemperatureRow:
    celsius: float
    fahrenheit: float
    kelvin: float


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def round_rows(rows: Iterable[TemperatureRow]) -> List[TemperatureRow]:
    return [
        TemperatureRow(
            celsius=round(row.celsius, 2),
            fahrenheit=round(row.fahrenheit, 2),
            kelvin=round(row.kelvin, 2),
        )
        for row in rows
    ]


def build_conversion_table(value: float, scale: str) -> List[TemperatureRow]:
    scale = scale.lower()
    if scale == "c":
        base_c = value
        base_f = celsius_to_fahrenheit(value)
        base_k = celsius_to_kelvin(value)
    elif scale == "f":
        base_c = fahrenheit_to_celsius(value)
        base_f = value
        base_k = fahrenheit_to_kelvin(value)
    elif scale == "k":
        base_c = kelvin_to_celsius(value)
        base_f = kelvin_to_fahrenheit(value)
        base_k = value
    else:
        raise ValueError("Scale must be C, F, or K")

    rows = [
        TemperatureRow(base_c, base_f, base_k),
        TemperatureRow(base_c + 10, celsius_to_fahrenheit(base_c + 10), celsius_to_kelvin(base_c + 10)),
        TemperatureRow(base_c - 10, celsius_to_fahrenheit(base_c - 10), celsius_to_kelvin(base_c - 10)),
    ]
    return round_rows(rows)


def ask_for_float(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a numeric value.")


def ask_for_scale(prompt: str) -> str:
    while True:
        scale = input(prompt).strip().lower()
        if scale in {"c", "f", "k"}:
            return scale
        print("Please enter C for Celsius, F for Fahrenheit, or K for Kelvin.")


def display_table(rows: List[TemperatureRow]) -> None:
    print()
    print("=== TEMPERATURE CONVERSION TABLE ===")
    print(f"{'Celsius':>10} | {'Fahrenheit':>12} | {'Kelvin':>8}")
    print("-" * 36)
    for row in rows:
        print(f"{row.celsius:>10.2f} | {row.fahrenheit:>12.2f} | {row.kelvin:>8.2f}")


def main() -> None:
    value = ask_for_float("Enter the temperature value: ")
    scale = ask_for_scale("Enter the scale (C/F/K): ")
    rows = build_conversion_table(value, scale)
    display_table(rows)


if __name__ == "__main__":
    main()
