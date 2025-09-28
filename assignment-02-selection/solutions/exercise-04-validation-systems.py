"""Assignment 2 – Exercise 4: Validation Systems"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, List, Tuple


EMAIL_PATTERN = re.compile(r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}")
PASSWORD_PATTERN = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}")


@dataclass
class RegistrationForm:
    username: str
    email: str
    password: str
    confirm_password: str
    terms_agreed: bool


def validate_registration(form: RegistrationForm) -> Tuple[bool, List[str]]:
    errors: List[str] = []

    if len(form.username) < 3:
        errors.append("Username must be at least 3 characters long.")
    if not EMAIL_PATTERN.match(form.email):
        errors.append("Email address is not valid.")
    if not PASSWORD_PATTERN.match(form.password):
        errors.append("Password must contain upper, lower, digit and be 8+ characters.")
    if form.password != form.confirm_password:
        errors.append("Passwords do not match.")
    if not form.terms_agreed:
        errors.append("Terms and conditions must be accepted.")

    return not errors, errors


def check_record_quality(record: Dict[str, str]) -> List[str]:
    issues: List[str] = []
    if not record.get("name"):
        issues.append("Name missing")
    if record.get("country") not in {"USA", "Canada", "UK"}:
        issues.append("Unsupported country")
    try:
        age = int(record.get("age", "0"))
        if age <= 0:
            issues.append("Age must be positive")
    except ValueError:
        issues.append("Age must be a number")
    return issues


def validate_form_submission(payload: Dict[str, str]) -> str:
    mandatory_fields = {"full_name", "email", "message"}
    if not mandatory_fields.issubset(payload):
        return "Missing mandatory fields"
    if len(payload["message"].strip()) < 10:
        return "Message too short"
    if not EMAIL_PATTERN.match(payload["email"]):
        return "Invalid email"
    return "Submission accepted"


def demo() -> None:
    print("=== REGISTRATION VALIDATION ===")
    form = RegistrationForm(
        username="jd",
        email="john.doe@example.com",
        password="Secret123",
        confirm_password="Secret123",
        terms_agreed=False,
    )
    valid, errors = validate_registration(form)
    print("Valid:", valid)
    for error in errors:
        print(" -", error)

    print("\n=== DATA QUALITY CHECK ===")
    record = {"name": "Ana", "country": "Spain", "age": "-2"}
    print("Issues:", check_record_quality(record))

    print("\n=== FORM SUBMISSION ===")
    submission = {"full_name": "Lee", "email": "lee@sample.com", "message": "Hello team!"}
    print(validate_form_submission(submission))


if __name__ == "__main__":
    demo()
