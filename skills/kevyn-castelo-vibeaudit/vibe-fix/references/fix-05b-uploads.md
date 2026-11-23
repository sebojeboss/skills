# Fix 5b — Restrict uploads


Five checks. All five, because each covers a different failure:

```typescript
import { fileTypeFromBuffer } from 'file-type'
import { randomUUID } from 'crypto'

const MAX = 5 * 1024 * 1024
const ALLOWED = new Set(['image/jpeg','image/png','image/webp'])

export async function POST(req: Request) {
  const user = await requireUser()

  const form = await req.formData()
  const file = form.get('file')
  if (!(file instanceof File)) return bad('No file')

  // 1. size
  if (file.size > MAX) return bad('File too large')

  // 2. type — from content, not from the header or the filename
  const buf = Buffer.from(await file.arrayBuffer())
  const detected = await fileTypeFromBuffer(buf)
  if (!detected || !ALLOWED.has(detected.mime)) return bad('Unsupported file type')

  // 3. filename — generated, never user-supplied
  const name = `${user.id}/${randomUUID()}.${detected.ext}`

  // 4. storage — a bucket, not the app's own origin
  await storage.from('uploads').upload(name, buf, { contentType: detected.mime })

  return Response.json({ path: name })
}
```

The fifth is the bucket's own policy, which is separate from table RLS and is missed constantly — see `fix-01-rls.md` for Supabase Storage and Firebase Storage rules.

Why content-based type detection: `Content-Type` and the filename extension are both supplied by the client. A `.png` extension on an HTML file with a spoofed header passes any check that trusts either one.

Why generated filenames: user-supplied names give path traversal and overwrite for free, and the fix is not sanitizing them — it is not using them. Keep the original in a database column if you need it for display.

Why a separate origin: an uploaded `.html` or `.svg` served from your domain executes as same-origin script, with access to cookies and session. If a separate domain is not possible, force `Content-Disposition: attachment`.

SVGs deserve their own decision: they are XML and can carry script. Either reject them or sanitize as XML — `file-type` will call them `image/svg+xml`, which passes an image-only allowlist that includes it.


## Verify

Upload a disallowed type with a spoofed extension and a spoofed `Content-Type`
and confirm rejection — spoofing both is the case that separates a real check
from a decorative one. Confirm an oversized file is rejected before it is fully
buffered, not after.

