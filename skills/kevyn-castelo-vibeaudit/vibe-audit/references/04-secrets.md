# Failure 4 — Secrets exposed in the bundle, the repo, or Git history

## The shape of it

Two distinct failures share this heading, and they need separate checks.

**In the bundle.** Every framework has a prefix convention that marks an environment variable as safe to inline into client JavaScript — `NEXT_PUBLIC_`, `VITE_`, `REACT_APP_`, `EXPO_PUBLIC_`, `PUBLIC_`, `NUXT_PUBLIC_`. The convention exists precisely because the value becomes public. An AI asked to "call the OpenAI API from the app" produces a `fetch` from a component, hits the build error about the missing variable, and the prefix is the obvious fix. The build passes. The key is now in a JavaScript file anyone can open.

**In Git.** Roughly 24 million secrets were leaked to GitHub in 2024 alone, and the average time between an exposed key being pushed and a bot harvesting it is minutes. Deleting the commit does nothing — the object stays in history. This is not targeted attention; it is automated scraping of the entire platform, continuously.

## What to check

### A. Git history — run gitleaks

```bash
gitleaks detect --source . -v
gitleaks detect --source . --no-git -v    # working tree, including untracked
```

Not installed:
```bash
brew install gitleaks          # macOS / Linuxbrew
# or grab the binary from github.com/gitleaks/gitleaks/releases
```

Every hit is presumed live until the user confirms otherwise. Report the commit SHA, the file, and the rule that matched.

Manual fallback if gitleaks is unavailable:
```bash
git log --all --full-history -- '*.env' '*.env.*' '*secrets*' '*credentials*' '*.pem' '*.p12' '*.key'
git grep -nI -E '(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|xox[baprs]-|AIza[0-9A-Za-z_-]{35}|-----BEGIN [A-Z ]*PRIVATE KEY-----)' $(git rev-list --all) 2>/dev/null | head -50
```
That last one is slow on large repos. Prefer gitleaks.

### B. The bundle

Source grep first:

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -E '(NEXT_PUBLIC|VITE|REACT_APP|EXPO_PUBLIC|NUXT_PUBLIC|PUBLIC)_[A-Z_]*(KEY|SECRET|TOKEN|PASSWORD|API|CREDENTIAL|PRIVATE)' .
```

Then the built output, which is what actually ships:

```bash
npm run build 2>/dev/null
grep -rIoE '(sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|xox[baprs]-[A-Za-z0-9-]+|service_role)' \
  dist/ build/ .next/static/ out/ public/build/ 2>/dev/null | sort -u | head -50
```

Building may not be possible (missing deps, no lockfile). Say so rather than reporting the source grep as if it were bundle verification.

Which prefixed variables are *fine*: Supabase `anon` key, Firebase web config, Stripe **publishable** key (`pk_`), PostHog/Sentry/analytics public keys, Mapbox public tokens. These are designed to be public and are protected by other mechanisms (RLS, Firebase rules, Stripe's own scoping). Do not report them as findings — but do check that the mechanism protecting them is actually in place, which is failure 1.

Which are never fine: anything with `secret`, `service_role`, a Stripe `sk_`, an OpenAI/Anthropic/model-provider key, a database connection string, an SMTP password, a JWT signing secret, a webhook signing secret, a private key.

### C. Hardcoded literals

Keys skip `.env` entirely more often than people expect:

```bash
grep -rIn --exclude-dir={node_modules,.git,dist,build} \
  -E "(api[_-]?key|apikey|secret|password|passwd|token|bearer|authorization)\s*[:=]\s*['\"][^'\"]{12,}" \
  --include='*.ts' --include='*.js' --include='*.tsx' --include='*.jsx' \
  --include='*.py' --include='*.go' --include='*.rb' --include='*.java' \
  --include='*.json' --include='*.yaml' --include='*.yml' .
```

Also check config files people forget are code: `docker-compose.yml`, `vercel.json`, CI workflow files, `Dockerfile` (`ENV` and `ARG` both persist into image layers), notebooks, `.mcp.json`, editor configs.

### D. Tracked env files

```bash
git ls-files | grep -E '^\.env|/\.env|\.env\.' 
grep -c '.env' .gitignore 2>/dev/null || echo "no .gitignore"
```

A tracked `.env` is a finding even if the values look like placeholders — placeholders get replaced in place and the next commit ships the real ones. A `.env.example` with obviously fake values is correct practice, not a finding.

### E. Client-side calls to third-party APIs

The structural version of the problem. If the browser talks directly to a paid or privileged API, a key has to be there:

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'api.openai.com' -e 'api.anthropic.com' -e 'api.stripe.com' \
  -e 'api.sendgrid.com' -e 'api.twilio.com' -e 'api.resend.com' \
  --include='*.tsx' --include='*.jsx' --include='*.vue' --include='*.svelte' .
```

Any hit in client code means either an exposed key or a proxy that should be verified. This is what the Backend-for-Frontend pattern exists to solve — see the fix reference.

## Reporting

Rotation comes first, before any code change. State it in the finding itself:

> This key is compromised. Revoke it in the provider dashboard and issue a new one **before** removing it from the code — history rewriting does not un-leak a key that bots have already harvested.

Then, for repos that were ever public, note that scrubbing history (`git filter-repo`, BFG) is cleanup, not remediation. The rotation is the remediation.

## Severity

- Live privileged key in a public repo or shipped bundle → **critical**
- Live privileged key in a private repo's history → **high** (every collaborator, every fork, every CI log)
- Key in `.env` that is untracked but with `.env` missing from `.gitignore` → **medium** (one `git add .` away)
- Public-by-design key flagged by a scanner → **not a finding**; note it in "Clean" with the mechanism that protects it

## False positives

- Example/placeholder values (`sk-xxxxxxxx`, `your-api-key-here`) — verify by shape before dismissing, since real keys have provider-specific formats.
- Test fixtures with revoked keys — confirm revocation with the user rather than assuming; "it's just a test key" is where real ones hide.
- Base64 blobs and hashes that trip entropy rules. Decode or identify before reporting.

## Evidence to capture

File, line, commit SHA (for history hits), which scanner rule matched, and the key's provider and prefix — *never the full key value in the report*. Truncate to the first 6 characters. A findings document is itself a place secrets leak from.

Remediation: `vibe-fix` reference `fix-04-secrets.md`.
