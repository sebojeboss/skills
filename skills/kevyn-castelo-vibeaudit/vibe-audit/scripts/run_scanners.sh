#!/usr/bin/env bash
# run_scanners.sh — run whichever open-source scanners are installed, collect
# results into .vibeaudit/, and say plainly which ones were missing.
#
# Nothing here is required. Scanners find patterns; they cannot find *missing*
# authorization, because absence has no signature. The manual checks in
# references/01..05 cover that ground. Do not block an audit on installing tools.
#
# Usage:
#   ./run_scanners.sh                 # scan current directory
#   ./run_scanners.sh /path/to/repo
set -uo pipefail

ROOT="${1:-.}"
cd "$ROOT" || { echo "cannot cd to $ROOT"; exit 1; }

OUT=".vibeaudit"
mkdir -p "$OUT"
RAN=(); SKIPPED=()

echo "=============================================="
echo " vibeaudit — scanners"
echo " target: $(pwd)"
echo " output: $OUT/"
echo "=============================================="

# ---------------------------------------------------------------- gitleaks
echo
echo "--- gitleaks (failure 4: secrets in code and Git history) ---"
if command -v gitleaks >/dev/null 2>&1; then
  gitleaks detect --source . --report-format json --report-path "$OUT/gitleaks.json" -v \
    2>&1 | tail -25
  gitleaks detect --source . --no-git --report-format json \
    --report-path "$OUT/gitleaks-worktree.json" 2>/dev/null | tail -5
  N=$(grep -c '"RuleID"' "$OUT/gitleaks.json" 2>/dev/null || echo 0)
  echo ">> $N finding(s) in history. Treat every one as a live, compromised key"
  echo "   until proven otherwise — rotate before touching the code."
  RAN+=("gitleaks")
else
  echo "not installed — brew install gitleaks"
  echo "   (or: github.com/gitleaks/gitleaks/releases)"
  SKIPPED+=("gitleaks")
fi

# ---------------------------------------------------- opengrep / semgrep
echo
echo "--- opengrep/semgrep (failures 4,5: SAST — injection, XSS, secrets) ---"
SAST=""
command -v opengrep >/dev/null 2>&1 && SAST="opengrep"
[ -z "$SAST" ] && command -v semgrep >/dev/null 2>&1 && SAST="semgrep"
if [ -n "$SAST" ]; then
  "$SAST" --config auto --json --output "$OUT/sast.json" \
    --exclude node_modules --exclude dist --exclude build --exclude .next \
    . 2>&1 | tail -20
  echo ">> results: $OUT/sast.json"
  RAN+=("$SAST")
else
  echo "not installed — github.com/opengrep/opengrep (free Semgrep fork,"
  echo "   community-governed, no single owner)"
  SKIPPED+=("opengrep")
fi

# ------------------------------------------------------------------ bandit
echo
echo "--- bandit (failure 5: dangerous Python patterns) ---"
if ls ./*.py >/dev/null 2>&1 || [ -f requirements.txt ] || [ -f pyproject.toml ]; then
  if command -v bandit >/dev/null 2>&1; then
    bandit -r . -f json -o "$OUT/bandit.json" \
      -x ./node_modules,./venv,./.venv,./tests,./test 2>/dev/null
    bandit -r . -x ./node_modules,./venv,./.venv 2>/dev/null | tail -25
    echo ">> results: $OUT/bandit.json"
    RAN+=("bandit")
  else
    echo "Python detected but bandit not installed — pip install bandit"
    SKIPPED+=("bandit")
  fi
else
  echo "no Python in this project, skipping"
fi

# --------------------------------------------------------------- npm audit
echo
echo "--- dependency audit ---"
if [ -f package-lock.json ] || [ -f package.json ]; then
  if command -v npm >/dev/null 2>&1; then
    npm audit --json > "$OUT/npm-audit.json" 2>/dev/null
    npm audit 2>/dev/null | tail -15
    RAN+=("npm audit")
  fi
fi
if [ -f requirements.txt ] && command -v pip-audit >/dev/null 2>&1; then
  pip-audit -r requirements.txt 2>&1 | tail -15
  RAN+=("pip-audit")
fi

# ------------------------------------------------------------------- ZAP
echo
echo "--- OWASP ZAP (dynamic scan) ---"
echo "not run automatically. ZAP hits a live target, so it needs a URL the user"
echo "confirms they own. Ask first, then run the baseline (passive) profile:"
echo
echo "   docker run -t ghcr.io/zaproxy/zaproxy zap-baseline.py -t https://<their-app>"
echo
echo "Baseline is passive. An active scan writes data and can knock over a small"
echo "instance — only with explicit consent."
SKIPPED+=("zap (needs a target URL)")

# --------------------------------------------------------------- summary
echo
echo "=============================================="
echo " ran:     ${RAN[*]:-none}"
echo " skipped: ${SKIPPED[*]:-none}"
echo "=============================================="
echo
echo "Scanners are the easy half. The half that matters — RLS state, frontend-only"
echo "authorization, missing ownership checks — has no pattern to match on."
echo "Work through references/01..05 next."
