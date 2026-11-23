# Fix 5c — Rate limits


Serverless resets in-memory counters per instance, so a shared store is required — otherwise the limiter is decorative.

```typescript
import { Ratelimit } from '@upstash/ratelimit'
import { Redis } from '@upstash/redis'

const authLimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(5, '15 m'),
  prefix: 'auth',
})

const { success, reset } = await authLimit.limit(ip)
if (!success) {
  return new Response('Too many requests', {
    status: 429,
    headers: { 'Retry-After': String(Math.ceil((reset - Date.now()) / 1000)) },
  })
}
```

Express: `express-rate-limit` with a Redis store — the default memory store does not survive multiple processes.
FastAPI: `slowapi`. Django: `django-ratelimit`.

Where it goes, in priority order:

| Endpoint | Suggested | Key on |
|---|---|---|
| Login | 5 / 15 min | IP + account |
| Signup | 3 / hour | IP |
| Password reset, OTP send | 3 / hour | IP + account |
| OTP verify | 5 / 15 min | account |
| Email / SMS send | 10 / hour | user |
| Paid API proxy (LLM etc.) | per plan | user |
| Search / list | 60 / min | user or IP |
| Upload | 20 / hour | user |

Key on the account as well as the IP for login: IP-only lets a distributed attempt through, account-only lets one attacker lock out a real user. Both.

Behind a proxy, `req.ip` is the proxy. Read the forwarded header your platform sets and trust only that — configure `trust proxy` correctly, or every request shares one bucket.

Edge rate limiting (Cloudflare, Vercel WAF) is legitimate and does not appear in code. If the user has it, the code-level limiter is defense in depth rather than the primary control.


Cheap, and it closes bulk extraction:

```typescript
const limit = Math.min(Number(searchParams.get('limit')) || 20, 100)
```


## Verify

Fire repeated auth requests and confirm the 429 arrives at the expected count —
and that it resets. A limiter that never releases is an outage waiting for a
traffic spike. On serverless, verify across cold starts: a limiter that works in
one instance and not across them is the failure this fix exists to prevent.

