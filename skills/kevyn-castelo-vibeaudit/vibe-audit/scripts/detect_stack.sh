#!/usr/bin/env bash
# detect_stack.sh — report what this project is built with and which scanners exist.
# Read this before choosing checks: greps aimed at absent frameworks produce noise,
# and noise is what makes people stop reading security reports.
set -uo pipefail

ROOT="${1:-.}"
cd "$ROOT" || { echo "cannot cd to $ROOT"; exit 1; }

# vibe-audit/vibe-fix excluded because these skills are installed inside the
# target project (.claude/skills/vibe-audit/...) and their own reference docs
# mention every framework name this script greps for — without the exclusion,
# every install self-detects every framework as present.
EX=(--exclude-dir=node_modules --exclude-dir=.git --exclude-dir=dist
    --exclude-dir=build --exclude-dir=.next --exclude-dir=venv
    --exclude-dir=.venv --exclude-dir=vendor --exclude-dir=__pycache__
    --exclude-dir=vibe-audit --exclude-dir=vibe-fix)

has_file() { [ -e "$1" ]; }
seen()     { grep -rIlq "${EX[@]}" -e "$1" . 2>/dev/null; }
mark()     { printf '  %-28s %s\n' "$1" "$2"; }

echo "=============================================="
echo " vibeaudit — stack detection"
echo " $(pwd)"
[ -d .git ] && echo " commit: $(git rev-parse --short HEAD 2>/dev/null || echo 'n/a')"
echo "=============================================="

echo
echo "LANGUAGES / MANIFESTS"
for f in package.json requirements.txt pyproject.toml Pipfile go.mod Gemfile \
         composer.json Cargo.toml pom.xml build.gradle; do
  has_file "$f" && mark "$f" "present"
done

echo
echo "FRAMEWORKS"
has_file next.config.js || has_file next.config.mjs || has_file next.config.ts && mark "Next.js" "config found"
[ -d app ] && [ -f package.json ] && grep -q '"next"' package.json 2>/dev/null && mark "Next.js App Router" "app/ present"
[ -d pages ] && grep -q '"next"' package.json 2>/dev/null && mark "Next.js Pages Router" "pages/ present"
has_file vite.config.js || has_file vite.config.ts && mark "Vite" "config found"
has_file nuxt.config.ts && mark "Nuxt" "config found"
has_file svelte.config.js && mark "SvelteKit" "config found"
has_file angular.json && mark "Angular" "config found"
has_file remix.config.js && mark "Remix" "config found"
has_file astro.config.mjs && mark "Astro" "config found"
has_file manage.py && mark "Django" "manage.py"
has_file artisan && mark "Laravel" "artisan"
seen 'from fastapi' && mark "FastAPI" "imported"
seen 'from flask' && mark "Flask" "imported"
seen "require('express')" || seen 'from .express.' && mark "Express" "imported"
seen '@nestjs/common' && mark "NestJS" "imported"
seen 'fastify' && mark "Fastify" "imported"

echo
echo "DATA LAYER  (drives failure 1 and 3 checks)"
seen '@supabase/supabase-js' || has_file supabase/config.toml && mark "Supabase" "client or config"
[ -d supabase/migrations ] && mark "  └ migrations" "$(ls supabase/migrations/*.sql 2>/dev/null | wc -l | tr -d ' ') .sql files"
seen 'firebase/app' || has_file firebase.json && mark "Firebase" "client or config"
has_file firestore.rules && mark "  └ firestore.rules" "present  ← READ THIS"
has_file storage.rules && mark "  └ storage.rules" "present  ← READ THIS"
has_file database.rules.json && mark "  └ RTDB rules" "present  ← READ THIS"
[ -d prisma ] && mark "Prisma" "schema dir"
seen 'drizzle-orm' && mark "Drizzle" "imported"
seen 'mongoose' && mark "Mongoose" "imported"
seen 'sequelize' && mark "Sequelize" "imported"
seen 'sqlalchemy' && mark "SQLAlchemy" "imported"

SQLC=$(find . -name '*.sql' -not -path './node_modules/*' -not -path './.git/*' 2>/dev/null | wc -l | tr -d ' ')
[ "$SQLC" -gt 0 ] && mark "SQL files" "$SQLC found  → run check_rls.py"

echo
echo "SECRET-BEARING FILES  (failure 4)"
for f in .env .env.local .env.production .env.development; do
  if has_file "$f"; then
    if git ls-files --error-unmatch "$f" >/dev/null 2>&1; then
      mark "$f" "*** TRACKED IN GIT ***"
    else
      mark "$f" "present, untracked"
    fi
  fi
done
if has_file .gitignore; then
  grep -q '\.env' .gitignore && mark ".gitignore" "covers .env" || mark ".gitignore" "*** does NOT cover .env ***"
else
  mark ".gitignore" "*** MISSING ***"
fi

echo
echo "PUBLIC-PREFIXED ENV VARS  (failure 4 — each must be public by design)"
PUBVARS=$(grep -rIhoE '(NEXT_PUBLIC|VITE|REACT_APP|EXPO_PUBLIC|NUXT_PUBLIC|PUBLIC)_[A-Z0-9_]+' \
  "${EX[@]}" . 2>/dev/null | sort -u | head -40)
if [ -n "$PUBVARS" ]; then
  echo "$PUBVARS" | sed 's/^/  /'
  echo "$PUBVARS" | grep -qE '(SERVICE_ROLE|SECRET|PRIVATE)' \
    && echo "  *** one of the above looks privileged — see references/04-secrets.md ***"
else
  echo "  (none found)"
fi

echo
echo "BUILD OUTPUT  (grep the bundle, not just the source)"
for d in dist build .next/static out public/build; do
  [ -d "$d" ] && mark "$d" "present — scan it"
done

echo
echo "SCANNERS AVAILABLE"
for t in gitleaks opengrep semgrep bandit trivy zap.sh zap-baseline.py; do
  if command -v "$t" >/dev/null 2>&1; then
    mark "$t" "installed"
  else
    mark "$t" "not installed"
  fi
done
command -v python3 >/dev/null 2>&1 && mark "python3" "$(python3 --version 2>&1)"

echo
echo "=============================================="
echo " Next: run_scanners.sh, then work through"
echo " references/01..05 for what scanners can't see."
echo "=============================================="
