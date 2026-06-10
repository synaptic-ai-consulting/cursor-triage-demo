<!--
  PLAN.md — filled in by the agent at the start of every task.
  Required by .cursor/rules/10-hardened.mdc (Rule #1).
-->

# Plan

**Goal:**
_(1 sentence — what are you about to do?)_

**Files to TOUCH (allow-list):**
- `app/discounts.py`
- `PLAN.md`

**Files to NOT touch (deny-list):**
- `app/main.py`
- `app/pricing.py`
- `tests/**`
- `.cursor/**`

**Tests that must pass:**
- `tests/test_discounts.py`
- `tests/test_pricing.py` (must remain green)

**Risks / open questions:**
- _(list any uncertainty before editing)_
