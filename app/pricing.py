"""Base pricing logic. DO NOT MODIFY in the demo — agent must NOT touch this file."""

from __future__ import annotations

# Tier thresholds in USD of cart subtotal
TIERS: dict[str, float] = {
    "bronze": 0.0,
    "silver": 100.0,
    "gold": 500.0,
    "platinum": 2000.0,
}


def base_price(units: int, unit_price: float) -> float:
    """Compute the raw subtotal before any discount.

    Args:
        units: number of units in the cart (>= 0)
        unit_price: price per unit in USD (>= 0)

    Returns:
        Subtotal in USD.
    """
    if units < 0 or unit_price < 0:
        raise ValueError("units and unit_price must be non-negative")
    return round(units * unit_price, 2)


def tier_for_subtotal(subtotal: float) -> str:
    """Return the loyalty tier earned by this subtotal."""
    tier = "bronze"
    for name, threshold in TIERS.items():
        if subtotal >= threshold:
            tier = name
    return tier
