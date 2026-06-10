#!/usr/bin/env bash
# Act 3: activate the hardened rules.
set -euo pipefail

cd "$(dirname "$0")/.."

if [ -f .cursor/rules/10-hardened.mdc.disabled ]; then
  mv .cursor/rules/10-hardened.mdc.disabled .cursor/rules/10-hardened.mdc
fi

# Also neuter the broken rules so they don't conflict
if [ -f .cursor/rules/00-broken.mdc ]; then
  mv .cursor/rules/00-broken.mdc .cursor/rules/00-broken.mdc.disabled
fi

echo "✅ Hardened rules ACTIVE. Broken rules disabled."
echo "   In Cursor: ask the agent to reload rules (open a new chat) and re-run the same prompt."
