# Failure 5a — Injection and XSS

## The axis that varies: escaping by default, or not

Before checking anything, establish which side of this line the project sits on.
It inverts the entire check.

| Stack | Default | What you are looking for |
|---|---|---|
| React, Vue, Svelte, Angular | escapes | the **opt-out**: `dangerouslySetInnerHTML`, `v-html`, `@html`, `bypassSecurityTrust` |
| Jinja2, Django templates, ERB, Handlebars, Blade | escapes | the **opt-out**: `\|safe`, `\{\{\{ \}\}\}`, `raw`, `html_safe` |
| Plain PHP, raw string concatenation, manual HTML | does **not** escape | every point where user data reaches output — the safe cases are the exception |

In an escape-by-default stack, findings cluster at a handful of opt-out sites and
the audit is tractable. In an opt-in stack, the burden inverts: assume unsafe and
look for the sanitizer. Reporting a React app the way you would report raw PHP
produces noise; reporting raw PHP the way you would report React misses almost
everything.


### Cross-site scripting

React, Vue, Svelte and Angular escape by default. The vulnerability appears where someone deliberately opts out — usually because an AI was asked to "render the formatted description" and the escaping got in the way.

```bash
grep -rIn --exclude-dir={node_modules,.git,dist,build} \
  -e 'dangerouslySetInnerHTML' -e 'v-html' -e '@html' \
  -e 'innerHTML' -e 'outerHTML' -e 'insertAdjacentHTML' \
  -e 'document.write' -e 'bypassSecurityTrust' -e 'eval(' -e 'new Function(' .
```

For each hit, trace the value's origin. Constant or server-generated markdown that was sanitized → fine. Anything reaching it from a user-controlled field, a URL parameter, or a database column that users write → **finding**. The database round-trip is the one people miss: stored XSS looks like trusted data by the time it renders.

Also check `href`/`src` built from user input — `javascript:` URIs are an XSS vector that no HTML escaper catches:
```bash
grep -rIn -e 'href={' -e 'src={' --include='*.tsx' --include='*.jsx' . | grep -v node_modules | head -30
```

Server-side templating (Jinja, ERB, Handlebars) has its own opt-outs: `|safe`, `{{{ }}}`, `raw`, `html_safe`. Same trace.

### SQL injection

Rare with an ORM, which is why it slips through when it does appear — raw escape hatches:

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e '\$queryRawUnsafe' -e '\$executeRawUnsafe' -e 'sequelize.query' \
  -e '\.raw(' -e 'cursor.execute' -e 'text(' \
  --include='*.ts' --include='*.js' --include='*.py' .
```

The distinction is string interpolation versus parameters. `` `WHERE id = ${id}` `` is injectable; `WHERE id = $1` with a parameter array is not. Prisma's `$queryRaw` tagged template is parameterized and safe; `$queryRawUnsafe` is not — the names are the API telling you which is which.

Supabase `.rpc()` calling a `SECURITY DEFINER` function that builds dynamic SQL is a real path worth checking — that function runs with the definer's privileges and bypasses RLS.

### Command injection and path traversal

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'exec(' -e 'execSync' -e 'spawn(' -e 'child_process' \
  -e 'os.system' -e 'subprocess.*shell=True' \
  -e 'path.join(.*req\.' -e 'readFile(.*req\.' -e 'open(.*request\.' .
```

If Python is in the stack, `bandit -r .` covers most of this section automatically. Opengrep/Semgrep covers the JS side. Run them and use these greps to fill gaps.


## Validation at the boundary

A schema library in the dependencies is not evidence it is used. Check whether
handlers actually parse the body through a schema, or destructure it and hope.

```bash
grep -rIn -e 'zod' -e 'yup' -e 'joi' -e 'valibot' -e 'class-validator' \
  -e 'pydantic' -e 'marshmallow' package.json requirements.txt pyproject.toml 2>/dev/null
```

FastAPI and NestJS with a global validation pipe get this largely for free —
confirm the pipe is registered globally rather than per-route. An unbounded
string field is a memory and storage denial-of-service even when it never
reaches an injection sink.

## Severity

- Injection sink reachable from user input with no sanitization → **critical**
- `dangerouslySetInnerHTML` on content that is currently only admin-written → **medium** (one feature away)
- Missing schema validation where the framework already coerces types → **medium**

## False positives

- `dangerouslySetInnerHTML` fed by DOMPurify output, or markdown rendered with sanitization on — read the pipeline before flagging.
- Framework-level CSRF and escaping are real protections. Do not report a Django app for lacking manual escaping.

## Evidence to capture

The sink (file:line), the source of the value, and the path between them.
"Untrusted input" without a traced path is a guess, and guesses are what make
security reports get ignored.

Remediation: `vibe-fix` reference `fix-05a-injection-xss.md`.
