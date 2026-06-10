"""RED test — the agent must make this pass by creating app/discounts.py.

Contract:
    apply_discount(subtotal: float, tier: str) -> float

Rules:
    - bronze   ->  0% discount
    - silver   ->  5% discount
    - gold     -> 10% discount
    - platinum -> 15% discount
    - Returns the *discount amount* (not the discounted total), rounded to 2 decimals.
    - Unknown tier raises ValueError.
    - Negative subtotal raises ValueError.
"""

from __future__ import annotations

import pytest

# This import will fail until the agent creates app/discounts.py
from app.discounts import apply_discount  # type: ignore


@pytest.mark.parametrize(
    "subtotal,tier,expected",
    [
        (100.0, "bronze", 0.0),
        (100.0, "silver", 5.0),
        (100.0, "gold", 10.0),
        (100.0, "platinum", 15.0),
        (250.0, "silver", 12.5),
        (1000.0, "gold", 100.0),
        (2500.0, "platinum", 375.0),
        (0.0, "platinum", 0.0),
    ],
)
def test_apply_discount_known_tiers(subtotal: float, tier: str, expected: float) -> None:
    assert apply_discount(subtotal, tier) == pytest.approx(expected, abs=0.01)


def test_apply_discount_unknown_tier_raises() -> None:
    with pytest.raises(ValueError):
        apply_discount(100.0, "diamond")


def test_apply_discount_negative_subtotal_raises() -> None:
    with pytest.raises(ValueError):
        apply_discount(-1.0, "silver")
