"""Assignment 2 – Exercise 2: Boolean Logic"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass(frozen=True)
class User:
    username: str
    password: str
    is_locked: bool = False
    multi_factor_enabled: bool = False


def can_login(user: User, *, password_attempt: str, mfa_provided: bool) -> bool:
    return (
        not user.is_locked
        and user.password == password_attempt
        and (not user.multi_factor_enabled or mfa_provided)
    )


def discount_for_cart(total: float, *, has_coupons: bool, is_member: bool) -> float:
    discount = 0.0
    if total >= 200:
        discount += 0.15
    elif total >= 100:
        discount += 0.10
    if has_coupons and is_member:
        discount += 0.05
    elif has_coupons or is_member:
        discount += 0.02
    return min(discount, 0.25)


def event_eligibility(age: int, *, has_ticket: bool, vip_pass: bool) -> str:
    if vip_pass:
        return "VIP Access Granted"
    if age < 18:
        return "Underage"
    if not has_ticket:
        return "Ticket Required"
    return "Access Granted"


def filter_applicants(applicants: Dict[str, Tuple[int, bool, bool]]) -> Dict[str, str]:
    results = {}
    for name, (age, experience, portfolio) in applicants.items():
        if age >= 21 and (experience or portfolio):
            results[name] = "Shortlisted"
        else:
            results[name] = "Not selected"
    return results


def demo() -> None:
    print("=== LOGIN CHECKS ===")
    alice = User("alice", "s3cret", multi_factor_enabled=True)
    print("Alice valid attempt:", can_login(alice, password_attempt="s3cret", mfa_provided=True))
    print("Alice missing MFA:", can_login(alice, password_attempt="s3cret", mfa_provided=False))

    print("\n=== DISCOUNT CALCULATOR ===")
    basket_value = 185.40
    print(
        f"Cart ${basket_value:.2f} member+coupon -> "
        f"{discount_for_cart(basket_value, has_coupons=True, is_member=True)*100:.0f}%"
    )

    print("\n=== EVENT ELIGIBILITY ===")
    print(event_eligibility(25, has_ticket=True, vip_pass=False))
    print(event_eligibility(16, has_ticket=True, vip_pass=False))
    print(event_eligibility(30, has_ticket=False, vip_pass=True))

    print("\n=== APPLICANT FILTER ===")
    applicants = {
        "Sam": (22, True, False),
        "Tina": (19, True, True),
        "Lee": (28, False, False),
        "Ana": (24, False, True),
    }
    for name, status in filter_applicants(applicants).items():
        print(f"{name}: {status}")


if __name__ == "__main__":
    demo()
