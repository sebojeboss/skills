# Fix 4 — Rotate, then move the key behind a server

## Rotate first. Always.

Before any code change, before any history rewrite: revoke the key in the provider's dashboard and issue a new one.

This is not caution, it is the actual remediation. Around 24 million secrets leaked to GitHub in 2024, and the gap between a push and an automated harvester collecting it is measured in minutes. Nobody is targeting the user personally — bots crawl the whole platform continuously. A key that appeared in a scan should be assumed collected.

Deleting the commit does nothing. Making the repo private does nothing. Rewriting history does nothing to a key already in someone's database. Only revocation does.

Where to rotate:

| Provider | Where |
|---|---|
| Supabase | Project Settings → API → rotate keys (this invalidates existing JWTs — plan for it) |
| OpenAI / Anthropic | API keys dashboard → revoke → create new |
| Stripe | Developers → API keys → roll |
| AWS | IAM → the access key → deactivate, then delete after cutover |
| Google / Firebase | Cloud Console → Credentials |
| GitHub tokens | Settings → Developer settings → revoke |
| SMTP / SendGrid / Twilio / Resend | Provider dashboard → API keys |

For AWS, also check CloudTrail for use of the key you are revoking. For a paid API key, check billing for the exposure window. If usage appears that the user does not recognize, that is an incident, not a cleanup — say so directly.

## Then: get the key out of the client

The structural fix is **Backend for Frontend**. The browser stops talking to the third-party API and talks to an endpoint you own; your server holds the key.

```typescript
// app/api/ai/route.ts — server only
export async function POST(req: Request) {
  const user = await requireUser()              // failure 2
  await checkRateLimit(user.id)                 // failure 5 — this endpoint costs money
  const { prompt } = ChatSchema.parse(await req.json())

  const res = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,  // no public prefix
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ model: 'gpt-4o-mini', messages: [{ role: 'user', content: prompt }] }),
  })

  return Response.json(await res.json())
}
```

```typescript
// client — no key anywhere
const res = await fetch('/api/ai', {
  method: 'POST',
  body: JSON.stringify({ prompt }),
})
```

Three things make this a real fix rather than a relocation of the problem:

1. **Drop the public prefix.** `NEXT_PUBLIC_`, `VITE_`, `REACT_APP_`, `EXPO_PUBLIC_` mean "inline this into the bundle". Rename the variable, or the build helpfully re-exposes it.
2. **Auth on the proxy.** An unauthenticated proxy to a paid API is a key that anyone can spend, just with an extra hop. This is now one of the most commonly abused endpoint types in AI-built apps.
3. **Rate limit it.** Same reason.

Static hosting with no server: use an edge function (Cloudflare Workers, Vercel/Netlify Functions, Supabase Edge Functions). Same shape, same three requirements.

## Which prefixed keys are fine

Leave these alone — they are public by design and protected by other mechanisms:

- Supabase `anon` key (protected by RLS — which is why failure 1 matters so much)
- Firebase web config (protected by security rules)
- Stripe **publishable** key `pk_...`
- Analytics/error-tracking public keys (PostHog, Sentry DSN)
- Mapbox public tokens

Never public, no exceptions: `service_role`, Stripe `sk_`, model-provider keys, database connection strings, SMTP passwords, JWT signing secrets, webhook signing secrets, private keys.

The distinction is whether the provider designed the key to be public and gave you a separate enforcement layer. If the key's only protection is that nobody looked, it is not public.

## Hygiene

```bash
printf '.env\n.env.*\n!.env.example\n' >> .gitignore
git rm --cached .env 2>/dev/null   # stops tracking; does not remove from history
```

Commit a `.env.example` with placeholder values, so the next person knows which variables exist without needing the real ones.

Also check the places people forget are code: `docker-compose.yml`, `vercel.json`, CI workflow files, `Dockerfile` (`ENV` and `ARG` both persist into image layers, so a build-arg secret is in the published image), notebooks, `.mcp.json`.

## History rewriting — ask first

This is cleanup, not remediation, and it breaks every clone and fork. Do not run it unprompted.

```bash
pip install git-filter-repo
git filter-repo --path .env --invert-paths --force
git push origin --force --all
git push origin --force --tags
```

Then every collaborator re-clones; existing forks and pull requests break. On GitHub, cached blobs can survive in the API for a while and need support to purge — another reason rotation is the fix and this is the tidying.

Worth saying to the user: if the repo was ever public, treat the history as permanently disclosed and skip this step unless they need it for compliance.

## Verify

```bash
gitleaks detect --source . --no-git -v          # working tree clean
npm run build
grep -rIoE '(sk-|AKIA|AIza|xox[baprs]-|service_role)' dist/ build/ .next/static/ 2>/dev/null
```

Then confirm the old key is actually dead — call the provider with it and expect a 401. A rotation that was never applied looks identical to one that was, right up until it doesn't.

## Stop the next one

`gitleaks protect --staged` as a pre-commit hook catches a secret in the only cheap moment — before it becomes history:

```bash
# .git/hooks/pre-commit  (or via husky / pre-commit framework)
gitleaks protect --staged --verbose || {
  echo "Secret detected in staged changes. Commit blocked."
  exit 1
}
```

Offer it; do not install it silently. Hooks that appear without warning get deleted the first time they block something at a bad moment.
