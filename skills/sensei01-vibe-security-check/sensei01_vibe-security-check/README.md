# vibe-security-check

A Claude skill that audits AI-assisted (vibe-coded) projects for security vulnerabilities. When installed, Claude will systematically check your codebase against 31 of the most common issues that AI coding tools introduce or overlook — across secrets, access control, user input, and AI-specific attack surfaces.

## Install

```bash
npx skills add Sensei01/vibe-security-check
```

## Usage

Once installed, just ask Claude to review your code:

> "audit this project for security issues",
> "is this ready to ship?",
> "what am I missing security-wise?"

Claude will ask for your key files (API routes, auth logic, env config, anything that handles user input or LLM calls), then work through the full checklist and return a prioritized report.

## What it checks

### 01 — Secrets & Config
- Hardcoded secrets, tokens, or API keys
- AI model API keys (OpenAI, Anthropic, Gemini, etc.) exposed client-side
- Secrets leaking through logs, error messages, or API responses
- Environment files committed to git
- Overly permissive CORS
- Vulnerable or AI-hallucinated dependencies (typosquatting)
- Default credentials or debug mode left on in production

### 02 — Access & API
- Routes accessible without authentication (including hidden-URL admin routes)
- Insecure direct object references — IDOR (changing an ID to access other users' data)
- Auth tokens in localStorage instead of httpOnly cookies
- Homegrown auth instead of a battle-tested library
- Missing rate limiting on sensitive endpoints
- Leaky error responses exposing internals
- Over-fetching, missing confirmation on destructive actions
- Unvalidated webhook signatures (Stripe, GitHub, Twilio, etc.)
- Server-side request forgery — SSRF
- Mass assignment / over-posting

### 03 — User Input
- SQL/NoSQL injection and unsanitized input reaching LLM prompts
- Cross-site scripting — XSS
- Unvalidated file uploads
- Client-side payment bypass

### 04 — AI & Agent Surface
- Prompt injection (OWASP LLM01:2025)
- Indirect prompt injection via external content fed to the model
- System prompt leakage (OWASP LLM07:2025)
- Unvalidated LLM output executed or stored
- No test/prod separation in agentic workflows
- Overprivileged MCP servers (OWASP MCP Top 10)
- AI-generated code committed without security review

## Output

Claude opens with a one-line verdict, then lists each finding with the file and line where possible, what the risk is, and how to fix it. It closes with a **Top 3 priorities** block — the findings most likely to cause a real breach, in order of severity.

## Sources

@DeFiMinty · OWASP LLM Top 10 (2025) · OWASP MCP Top 10 · Veracode GenAI Code Security Report · Kaspersky · Wiz Research
