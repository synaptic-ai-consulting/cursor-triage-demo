"""FastAPI entrypoint. DO NOT MODIFY in the demo — agent must NOT touch this file."""

from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from app.pricing import base_price, tier_for_subtotal

# The agent must CREATE this module: app/discounts.py
# It must expose: apply_discount(subtotal: float, tier: str) -> float
try:
    from app.discounts import apply_discount  # type: ignore
except ImportError:  # pragma: no cover - expected before the agent runs
    apply_discount = None  # type: ignore

app = FastAPI(title="Cursor Triage Demo")


class QuoteRequest(BaseModel):
    units: int
    unit_price: float


class QuoteResponse(BaseModel):
    subtotal: float
    tier: str
    discount: float
    total: float


@app.post("/quote", response_model=QuoteResponse)
def quote(req: QuoteRequest) -> QuoteResponse:
    subtotal = base_price(req.units, req.unit_price)
    tier = tier_for_subtotal(subtotal)
    if apply_discount is None:
        raise RuntimeError(
            "app.discounts.apply_discount is missing — the agent has not "
            "implemented the loyalty discount module yet."
        )
    discount = apply_discount(subtotal, tier)
    total = round(subtotal - discount, 2)
    return QuoteResponse(subtotal=subtotal, tier=tier, discount=discount, total=total)
