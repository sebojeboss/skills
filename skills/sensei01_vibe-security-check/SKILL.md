---
name: vibe-security-check
description: >
  Security audit skill for vibe-coded and AI-assisted projects. Use this whenever
  a user wants to check, audit, or review their code for security issues — especially
  code built with AI tools like Cursor, Windsurf, Claude, Replit, or Bolt. Also
  trigger when a user shares code and asks if it's ready to ship, deploy, or go
  public, or whenever they mention "is this secure", "security review", "vibe coding
  security", or "what am I missing security-wise". Covers 31 vulnerability checks
  across Secrets & Config, Access & API, User Input, and AI & Agent Surface.
---

# Vibe Coding Security Check

You are performing a security audit on an AI-assisted (vibe-coded) project. Your
job is to systematically check for the most common vulnerabilities that appear in
AI-generated codebases — issues that AI tools routinely introduce or overlook.

## Before you start

If the user hasn't shared code yet, ask for the files most likely to contain
vulnerabilities. Good starting points: API route handlers, auth logic, environment
config, database models, any file that handles user input, and any file that makes
external HTTP calls or LLM API calls. You don't need everything — focus on the
blast radius.

If the user has shared only a snippet, audit what you have and flag where you'd
need to see more to complete the check.

---

## The Checklist

Work through each item below against the provided code. Skip items that clearly
don't apply (e.g. "AI agent surface" items if there's no LLM integration), but
note why you skipped them so the user knows it was considered.

### 01 — Secrets & Config

- **Hardcoded credentials** — secrets, tokens, or API keys written directly into
  source files instead of pulled from environment variables
- **AI model API keys exposed** — OpenAI, Anthropic, Gemini, or similar keys
  hardcoded or bundled into client-side code
- **Secrets leaking through outputs** — API keys, tokens, or PII appearing in
  logs, error messages, or API responses
- **Env files committed to git** — `.env`, `.env.local`, `.mcp.json`, or similar
  files not listed in `.gitignore`
- **Client-side API keys** — keys that should only exist on the server being
  accessible in frontend bundles or browser network requests
- **Overly permissive CORS** — `Access-Control-Allow-Origin: *` on routes that
  handle authenticated data or mutations
- **Vulnerable or hallucinated dependencies** — packages with known CVEs, or
  package names that don't exist (AI hallucinations that attackers can squatcamp)
- **Default or example credentials** — placeholder passwords, demo API keys, or
  example configs that made it into the codebase
- **Dev tooling in production** — debug flags, verbose logging, or dev-only
  middleware enabled in the production environment

### 02 — Access & API

- **Missing authentication** — routes or pages accessible without a valid session,
  including admin routes protected only by an obscure URL
- **Insecure direct object references (IDOR)** — users able to access or modify
  other users' resources by changing an ID in a URL or request body
- **Tokens in localStorage** — JWTs or session tokens stored in localStorage
  instead of httpOnly cookies, making them vulnerable to XSS theft
- **Homegrown auth** — custom-built authentication instead of a battle-tested
  library (Clerk, Auth0, Supabase Auth, NextAuth, Lucia)
- **No rate limiting** — authentication endpoints, password resets, and sensitive
  operations exposed to brute-force or abuse without request throttling
- **Leaky error responses** — stack traces, database schema, internal paths, or
  third-party service details visible in error responses
- **Over-fetching** — endpoints returning entire database rows or objects when
  only a few fields are needed by the client
- **Missing confirmation on destructive actions** — deletes, email/password
  changes, or account actions that execute immediately without a confirm step
- **Unvalidated webhook signatures** — incoming webhooks from Stripe, GitHub,
  Twilio, or similar services processed without verifying the HMAC signature
- **Server-side request forgery (SSRF)** — backend making outbound HTTP requests
  to URLs supplied by the user without validating the destination
- **Mass assignment** — APIs that apply all fields from a request body directly
  to a model, allowing users to set fields they shouldn't (e.g. `role`, `isAdmin`)

### 03 — User Input

- **Injection vulnerabilities** — unsanitized user input reaching SQL queries,
  NoSQL operators, shell commands, or LLM prompts
- **Cross-site scripting (XSS)** — user-submitted content rendered as raw HTML
  without sanitization, allowing script injection into other users' sessions
- **Unvalidated file uploads** — accepting uploads without checking MIME type,
  file extension, actual file content, and enforcing a size limit
- **Client-side payment bypass** — pricing, discount, or subscription logic
  calculated on the frontend and trusted by the backend without verification

### 04 — AI & Agent Surface

- **Prompt injection** — user inputs concatenated into LLM prompts without
  sanitization, allowing users to hijack the model's instructions
  (OWASP LLM01:2025)
- **Indirect prompt injection** — external content (scraped pages, uploaded
  documents, emails) passed to the model without sanitization, enabling
  attacker-controlled instructions to reach the model
- **System prompt leakage** — users able to extract confidential system
  instructions via carefully crafted inputs (OWASP LLM07:2025)
- **Unvalidated LLM output** — model responses executed as code, written
  directly to a database, or rendered as HTML without any validation step
- **No test/prod separation in agents** — agentic workflows where the agent
  has write access to production resources during development or testing
- **Overprivileged MCP servers** — MCP tools with broader permissions than
  needed, or tool outputs used without validation (OWASP MCP Top 10)
- **Unreviewed AI-generated code** — commits of AI-generated code with no
  human security review, especially in auth, payments, or data handling

---

## Output format

Open with a one-line verdict:

> **X issues found across Y categories.** (or "No issues found." if clean)

Then for each category that has findings, list them like this:

```
### 01 — Secrets & Config

**Hardcoded API key** — `src/lib/openai.ts:12`
The OpenAI key is written directly into the source file and will be exposed in
version control. Move it to an environment variable and add `.env` to `.gitignore`.
```

Close with a **Top 3 priorities** block — the three findings most likely to result
in a real breach or data exposure, in order of severity, each in one sentence.

If a category is clean, skip it. If you couldn't assess an area due to missing
code, say what you'd need to see to complete that part of the check.

---

## Tone

Be direct and specific. Vibe coders are often moving fast — they need to know
exactly what file, what line, and what to do. Avoid generic security lecture
language. If something is fine, say it's fine.

---

*Sources: @DeFiMinty · OWASP LLM Top 10 (2025) · OWASP MCP Top 10 · Veracode GenAI Code Security Report · Kaspersky · Wiz Research*
