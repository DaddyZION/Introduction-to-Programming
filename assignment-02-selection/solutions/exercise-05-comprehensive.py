"""Assignment 2 – Exercise 5: Comprehensive Decision System

Implements a mini business assistant that combines multiple selection
techniques: customer categorisation, order approval, and support routing.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Customer:
    name: str
    lifetime_value: float
    visits_this_month: int
    loyalty_points: int
    account_status: str


@dataclass
class Order:
    customer: Customer
    total_amount: float
    rush_delivery: bool
    risk_score: int
    payment_verified: bool


SUPPORT_CHANNELS = {
    "billing": "Billing Specialists",
    "technical": "Tech Support",
    "shipping": "Logistics",
}


def categorise_customer(customer: Customer) -> str:
    if customer.account_status != "active":
        return "Inactive"
    if customer.lifetime_value > 5000 or customer.loyalty_points > 2000:
        return "Platinum"
    if customer.lifetime_value > 2000 or customer.loyalty_points > 1000:
        return "Gold"
    if customer.visits_this_month >= 3:
        return "Silver"
    return "Bronze"


def approve_order(order: Order) -> Tuple[bool, str]:
    if not order.payment_verified:
        return False, "Payment verification failed"
    if order.total_amount > 1000 and order.rush_delivery:
        if order.risk_score > 50:
            return False, "High risk rush order"
        return True, "Approved with manual review"
    if order.risk_score > 80:
        return False, "Risk score too high"
    return True, "Approved"


def route_support_request(issue_type: str, is_vip: bool, urgency: str) -> str:
    urgency = urgency.lower()
    issue_type = issue_type.lower()

    if is_vip:
        if urgency == "critical":
            return "VIP Concierge"
        return "VIP Priority Queue"

    if issue_type in SUPPORT_CHANNELS:
        base = SUPPORT_CHANNELS[issue_type]
    else:
        base = "Customer Care"

    if urgency == "critical":
        return f"{base} - Escalated"
    if urgency == "high":
        return f"{base} - Priority"
    return f"{base} - Standard"


def demo() -> None:
    print("=== CUSTOMER CATEGORISATION ===")
    alice = Customer("Alice", lifetime_value=6500, visits_this_month=5, loyalty_points=2100, account_status="active")
    print(alice.name, categorise_customer(alice))

    print("\n=== ORDER APPROVAL ===")
    order = Order(customer=alice, total_amount=1200, rush_delivery=True, risk_score=40, payment_verified=True)
    print(approve_order(order))

    print("\n=== SUPPORT ROUTING ===")
    print(route_support_request("technical", is_vip=False, urgency="critical"))
    print(route_support_request("billing", is_vip=True, urgency="medium"))


if __name__ == "__main__":
    demo()
