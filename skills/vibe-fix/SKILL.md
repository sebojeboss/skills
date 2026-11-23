---
name: vibe-fix
description: Remediates the five security failures that AI-generated code leaves behind — enabling Row Level Security with scoped policies on Supabase/Firebase, moving authorization decisions from the frontend to the server, adding ownership checks to routes that fetch by ID (IDOR/BOLA), moving exposed API keys behind a Backend-for-Frontend proxy and rotating them, and adding input validation, upload restrictions and rate limiting. Use this skill whenever the user asks to fix, patch, harden or "make secure" something an audit or scanner flagged, and whenever they say a key leaked, RLS is off, an endpoint is unprotected, or they need to lock something down before shipping. Includes framework-specific recipes for Next.js, Express, FastAPI, Django, Supabase and Firebase. Pair with vibe-audit, which finds the problems this skill fixes.
---

# vibe-fix

Apply the remediation, then prove it worked.

Every fix here follows the same arc: **rotate what's compromised → close the hole at the server → verify the hole is closed → check nothing else broke.** Skipping the verification step is how security work turns into a false sense of security, which is worse than the original state because it stops anyone from looking again.

## Order of operations

Fix in this order regardless of what the report lists first. It reflects what an attacker can reach and how fast they can reach it:

1. **Rotate exposed secrets** — before any code change. A key that appeared in a scan is compromised. Bots harvest GitHub continuously; the window between push and harvest is minutes, and deleting the commit changes nothing.
2. **`service_role` / admin keys out of the client** — one key in a bundle voids every policy you are about to write.
3. **Enable RLS** on tables holding user data.
4. **Server-side authorization** on privileged endpoints.
5. **Ownership checks** on routes taking an ID.
6. **Input validation, upload limits, rate limits** — only the sub-checks that apply; an app with no upload path has no 5b.

| # | Failure | Recipe |
|---|---------|--------|
| 1 | RLS disabled | `references/fix-01-rls.md` |
| 2 | Authorization in the frontend | `references/fix-02-broken-authz.md` |
| 3 | Missing ownership check (IDOR) | `references/fix-03-idor.md` |
| 4 | Exposed secrets | `references/fix-04-secrets.md` |
| 5a | Injection and XSS | `references/fix-05a-injection-xss.md` |
| 5b | Uploads without checks | `references/fix-05b-uploads.md` |
| 5c | Missing rate limits | `references/fix-05c-rate-limits.md` |

Read the relevant reference before writing code. Each one has the framework-specific shape, and getting the framework idiom wrong is how a fix becomes a new bug.

## Before touching anything

**Work on a branch.** Security fixes change access control, and access control changes break things in ways that are invisible until a real user hits them. `git checkout -b security-fixes`.

**Enabling RLS will break the app.** Say this out loud before running the migration, not after. Every query that worked because the table was wide open stops returning rows. That is the fix working. The user needs to expect it, or they will roll it back within the hour — which is the single most common way this failure gets reintroduced.

**Ask before rewriting Git history.** `filter-repo` and BFG break every clone and fork. Rotation is the actual remediation; history scrubbing is cleanup, and it is the user's call whether the disruption is worth it.

## Applying a fix

For each finding:

1. **Read the surrounding code first.** A generic fix pasted into an unfamiliar codebase creates inconsistency, and inconsistent security code is where the next hole appears. Match the project's existing patterns for auth, error handling and validation.
2. **Fix the class, not the instance.** One unprotected route usually means the whole route family was generated from the same template. When you find the pattern, grep for its siblings and list them — fixing one of eight is a report that reads as done and is not.
3. **Prefer the layer closest to the data.** RLS beats a middleware check, because RLS holds even when someone adds a new endpoint next month and forgets. Defense in depth means both, but if effort is limited, push the check down.
4. **Do not change behaviour beyond the fix.** Refactoring alongside a security patch makes the diff unreviewable, and unreviewable security diffs get merged without review.

## Verifying

A fix is not done until it is demonstrated. Per failure:

| Failure | Verification |
|---|---|
| 1 | `SELECT tablename, rowsecurity FROM pg_tables WHERE schemaname='public'` shows `true`; `pg_policies` shows the expected policy; app still works when logged in |
| 2 | Call the privileged endpoint with a non-privileged session — it refuses |
| 3 | Request another user's record ID with a valid session — 403 or 404, no data |
| 4 | Old key rejected by the provider; new key absent from `dist/`, `build/`, `.next/static/`; `gitleaks detect` clean on the working tree |
| 5 | The injection payload no longer reaches the sink; upload of a disallowed type rejected; repeated auth requests hit the limiter |

Then re-run `vibe-audit`. If the audit produced a report, update it with the verification result per finding rather than writing a new one — the delta is what the user needs to see.

## Regression protection

A fix that nothing enforces gets undone by the next generated feature. Offer these; do not add them silently, since CI changes are the user's call:

- `gitleaks protect --staged` as a pre-commit hook — catches a secret before it becomes history, which is the only cheap moment
- Scanners in CI (`gitleaks detect`, `opengrep --config auto`, `bandit -r .`) failing the build on new findings
- A default-deny RLS policy on new tables, so the failure mode of forgetting is "broken" rather than "public"
- A shared `requireAuth` / `requireOwnership` helper, so the correct pattern is the easy one to reach for

## When a fix is out of scope

Some findings cannot be fixed from the code: a key that only the account owner can rotate, a Supabase dashboard setting, a bucket policy behind credentials you do not have. Say so specifically — the exact dashboard, the exact setting — rather than producing a patch that looks complete. A remediation report that quietly omits what it could not do is the same failure as an audit that implies completeness it lacks.
