#!/usr/bin/env bash
# Resets the repo to "Act 1" state — broken rules active, no discounts.py, PLAN.md blank.
set -euo pipefail

cd "$(dirname "$0")/.."

# 1. Remove any discounts.py the agent created
rm -f app/discounts.py

# 2. Ensure ONLY 00-broken.mdc is active. Cursor reads every .mdc file in
#    .cursor/rules/, so we disable the hardened one by renaming it.
if [ -f .cursor/rules/10-hardened.mdc ]; then
  mv .cursor/rules/10-hardened.mdc .cursor/rules/10-hardened.mdc.disabled
fi
if [ -f .cursor/rules/00-broken.mdc.disabled ]; then
  mv .cursor/rules/00-broken.mdc.disabled .cursor/rules/00-broken.mdc
fi

# 3. Reset PLAN.md to the empty template
cat > PLAN.md <<'EOF'
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
EOF

echo "✅ Demo reset to Act 1 state."
echo "   - app/discounts.py removed"
echo "   - hardened rules disabled (.cursor/rules/10-hardened.mdc.disabled)"
echo "   - PLAN.md reset"
echo ""
echo "Run: pytest -q   →  expect tests/test_discounts.py to FAIL on import."
