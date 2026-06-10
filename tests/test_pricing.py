"""Green baseline. These tests already pass — do not modify."""

from __future__ import annotations

import pytest

from app.pricing import base_price, tier_for_subtotal


def test_base_price_basic() -> None:
    assert base_price(3, 10.0) == 30.0


def test_base_price_zero() -> None:
    assert base_price(0, 999.0) == 0.0


def test_base_price_rejects_negative() -> None:
    with pytest.raises(ValueError):
        base_price(-1, 10.0)


@pytest.mark.parametrize(
    "subtotal,expected",
    [
        (0.0, "bronze"),
        (99.99, "bronze"),
        (100.0, "silver"),
        (499.99, "silver"),
        (500.0, "gold"),
        (1999.99, "gold"),
        (2000.0, "platinum"),
        (10_000.0, "platinum"),
    ],
)
def test_tier_for_subtotal(subtotal: float, expected: str) -> None:
    assert tier_for_subtotal(subtotal) == expected
