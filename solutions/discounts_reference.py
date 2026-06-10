"""Reference implementation — for instructor rehearsal only.

DO NOT copy this into app/discounts.py before the live demo.
This is what the agent SHOULD converge to in Act 3.
"""

from __future__ import annotations

DISCOUNT_RATES: dict[str, float] = {
    "bronze": 0.0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15,
}


def apply_discount(subtotal: float, tier: str) -> float:
    """Return the discount AMOUNT (not the discounted total) for a given tier.

    Args:
        subtotal: cart subtotal in USD (>= 0)
        tier: one of "bronze", "silver", "gold", "platinum"

    Returns:
        Discount amount in USD, rounded to 2 decimals.

    Raises:
        ValueError: if subtotal is negative or tier is unknown.
    """
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if tier not in DISCOUNT_RATES:
        raise ValueError(f"unknown tier: {tier!r}")
    return round(subtotal * DISCOUNT_RATES[tier], 2)
