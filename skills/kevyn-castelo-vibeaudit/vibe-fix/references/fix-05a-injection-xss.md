# Fix 5a — Validate at the boundary, sanitize at the sink

Match the fix to the stack's default. In an escape-by-default framework the
job is removing the opt-out. In an opt-in stack (raw PHP, manual string
building) the job is adding escaping everywhere and the diff is much larger —
scope that with the user before starting.


One schema per endpoint, parsed before the body touches anything else. The schema becomes the contract, and the handler stops guessing.

```typescript
import { z } from 'zod'

const CreatePost = z.object({
  title: z.string().min(1).max(200),
  body: z.string().max(50_000),
  tags: z.array(z.string().max(30)).max(10),
  published: z.boolean().default(false),
}).strict()

export async function POST(req: Request) {
  const user = await requireUser()
  const parsed = CreatePost.safeParse(await req.json())
  if (!parsed.success) {
    return Response.json({ error: parsed.error.flatten() }, { status: 400 })
  }
  // parsed.data is typed and bounded
}
```

`.strict()` rejects unknown keys instead of dropping them — which is what stops mass assignment (see `fix-03-idor.md`). Length caps are not cosmetic: an unbounded string field is a memory and storage denial-of-service.

Python: Pydantic with `model_config = ConfigDict(extra='forbid')`. FastAPI applies it automatically when the body is typed as a model. NestJS: `app.useGlobalPipes(new ValidationPipe({ whitelist: true, forbidNonWhitelisted: true }))` — global, so new endpoints inherit it.

### XSS

Prefer removing the opt-out. `dangerouslySetInnerHTML`, `v-html`, `@html`, `innerHTML` exist because someone needed rendered markup; usually the requirement is satisfied by rendering markdown to React elements instead of to an HTML string.

When raw HTML is genuinely required, sanitize on the way in and on the way out:

```typescript
import DOMPurify from 'isomorphic-dompurify'

const clean = DOMPurify.sanitize(userHtml, {
  ALLOWED_TAGS: ['p','br','strong','em','ul','ol','li','a','code','pre','blockquote'],
  ALLOWED_ATTR: ['href','title'],
  ALLOWED_URI_REGEXP: /^(?:https?|mailto):/i,
})
```

The URI restriction is the part that gets skipped and matters: `javascript:` in an `href` is an XSS vector no HTML escaper catches. Same for user-controlled `src`.

Python: `bleach.clean(html, tags=[...], attributes={...}, protocols=['http','https','mailto'])`.

Add a Content-Security-Policy as a second layer — it turns a missed sanitization into a blocked script rather than an executed one:

```typescript
// next.config.js headers
"Content-Security-Policy": "default-src 'self'; script-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'"
```

`'unsafe-inline'` in `script-src` removes most of the benefit. If the framework needs it, use a nonce.

### SQL injection

Parameters, never interpolation.

```typescript
// vulnerable
db.$queryRawUnsafe(`SELECT * FROM users WHERE email = '${email}'`)
// safe — tagged template parameterizes
db.$queryRaw`SELECT * FROM users WHERE email = ${email}`
```

```python
cursor.execute("SELECT * FROM users WHERE email = %s", (email,))   # safe
```

Table and column names cannot be parameterized. If they come from user input, validate against an allowlist of known-good names — never interpolate directly.

### Command execution and paths

Pass arguments as an array so there is no shell to inject into:

```javascript
execFile('convert', [inputPath, '-resize', '100x100', outputPath])  // no shell
```

```python
subprocess.run(['convert', src, dst], shell=False, check=True)
```

For paths, resolve and confirm containment rather than filtering `../`:

```typescript
const base = path.resolve('./uploads')
const target = path.resolve(base, userPath)
if (!target.startsWith(base + path.sep)) throw new Error('Invalid path')
```


## Verify

Send the payload that previously reached the sink and confirm it is escaped or
rejected. Confirm legitimate rich content still renders — an over-aggressive
sanitizer that strips normal formatting gets removed, and removals do not come back.

