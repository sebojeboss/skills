# Failure 5c — Missing rate limits


```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'rate-limit' -e 'rateLimit' -e 'ratelimit' -e 'slowDown' \
  -e 'Throttle' -e 'limiter' -e 'upstash' .
```

Absence across the whole project is the common result. Report it scoped to the endpoints where it matters, in this order:

- **Login / signup / password reset / OTP verification** — no limit means credential stuffing and unlimited OTP guessing. An email/SMS endpoint without a limit is also a direct bill.
- **Anything calling a paid API** (LLM proxies especially) — no limit means someone else spends your money, and this is now among the most commonly exploited endpoints in AI-built apps.
- **Search and list endpoints** — unbounded `limit` parameters, no pagination cap.
- **Anything writing to storage.**

Serverless deployments need a shared store — in-memory counters reset per instance and give near-zero protection. Note the deployment target when reporting.

Related, same family: check that list endpoints cap their page size. `?limit=100000` with no ceiling is a denial-of-service and a bulk-extraction tool at once.


## Deployment target changes the finding

Serverless resets in-memory counters per instance. A limiter backed by process
memory on Vercel, Lambda or Cloud Run gives near-zero protection, so note the
deployment target in the finding — "has a rate limiter" and "has a working rate
limiter" are different states.

## Severity

- No limit on auth endpoints or a paid-API proxy → **high**
- No pagination cap on a list endpoint → **medium**
- In-memory limiter on a serverless deployment → **medium**, and say why

## False positives

- Edge rate limiting (Cloudflare, Vercel WAF, an API gateway) is legitimate and invisible in code. Ask before reporting absence.

## Evidence to capture

Which endpoints are unprotected, the deployment target, and whether any shared
store exists for counters.

Remediation: `vibe-fix` reference `fix-05c-rate-limits.md`.
