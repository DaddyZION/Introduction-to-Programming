"""Assignment 2 – Exercise 3: Nested Decisions"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Applicant:
    name: str
    gpa: float
    extracurricular_score: int
    recommendation_strength: int


def university_admission(applicant: Applicant) -> str:
    if applicant.gpa >= 3.8:
        if applicant.recommendation_strength >= 8:
            return "Full Scholarship"
        return "Admitted"
    if applicant.gpa >= 3.2:
        if applicant.extracurricular_score >= 7 and applicant.recommendation_strength >= 6:
            return "Admitted"
        return "Waitlisted"
    return "Rejected"


def insurance_premium(age: int, accidents_last_3_years: int, credit_score: int) -> str:
    if age < 25:
        base = "High"
    elif age < 60:
        base = "Standard"
    else:
        base = "Senior"

    if accidents_last_3_years > 2:
        return f"{base} - Surcharge"
    if credit_score < 600:
        return f"{base} - Requires Review"
    if accidents_last_3_years == 0 and credit_score > 750:
        return f"{base} - Loyalty Discount"
    return base


def character_stat_bonus(role: str, level: int, alignment: str) -> int:
    role = role.lower()
    alignment = alignment.lower()
    bonus = 0

    if role == "warrior":
        bonus = 10 if level >= 20 else 5
        if alignment == "evil":
            bonus += 2
    elif role == "mage":
        bonus = 12 if level >= 18 else 6
        if alignment == "good":
            bonus += 3
    elif role == "rogue":
        bonus = 8 if level >= 15 else 4
        if alignment == "neutral":
            bonus += 1
    else:
        bonus = 2
    return bonus


def medical_triage(temp_c: float, heart_rate: int, breathing_rate: int) -> str:
    if temp_c > 39 or heart_rate > 130 or breathing_rate > 30:
        if temp_c > 40 or heart_rate > 150:
            return "Code Red - Immediate attention"
        return "Urgent - Doctor now"
    if temp_c < 35 or heart_rate < 45:
        return "Hypothermia risk - Warm patient"
    return "Stable - Monitor"


def demo() -> None:
    print("=== UNIVERSITY ADMISSION ===")
    lily = Applicant("Lily", 3.85, 7, 9)
    print(lily.name, "->", university_admission(lily))

    print("\n=== INSURANCE PREMIUM ===")
    print("Age 30, 0 accidents, 780:", insurance_premium(30, 0, 780))
    print("Age 22, 3 accidents, 680:", insurance_premium(22, 3, 680))

    print("\n=== GAME CHARACTER BONUS ===")
    print("Warrior level 25 evil:", character_stat_bonus("warrior", 25, "evil"))
    print("Mage level 12 good:", character_stat_bonus("mage", 12, "good"))

    print("\n=== MEDICAL TRIAGE ===")
    print(medical_triage(39.5, 120, 28))
    print(medical_triage(34.0, 70, 16))


if __name__ == "__main__":
    demo()
