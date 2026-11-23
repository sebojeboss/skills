# Failure 5b — File upload without checks

Applies only where an upload path exists. Run the detection below first; if
nothing matches, record it as not applicable rather than as clean.


```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'multer' -e 'formidable' -e 'busboy' -e 'UploadThing' \
  -e 'storage.from(.*).upload' -e 'getStorage' -e 'FileReader' \
  -e 'request.files' -e 'UploadFile' -e 'multipart' .
```

For each upload path, check five things:

1. **Type validation** — and whether it validates the *content* or just the filename/`Content-Type` header. Both of those are client-supplied. Magic-byte checking (`file-type`, `python-magic`) is the real check.
2. **Size limit** — missing means memory exhaustion or a storage bill. Multer without `limits` is unbounded.
3. **Filename handling** — user-supplied names reaching a path is traversal (`../../`) or overwrite. Generated names (UUID) sidestep it entirely.
4. **Storage location** — user uploads served from the app's own origin means an uploaded `.html` or `.svg` executes as same-origin script. Separate domain or forced `Content-Disposition: attachment`.
5. **Authorization on the bucket** — Supabase Storage and Firebase Storage have their own policies, separate from table RLS. An open bucket is failure 1 in a different room. Check `storage.rules` / storage policies explicitly; this is missed constantly.


## Severity

- Upload accepting arbitrary types served from the app's own origin → **high**
- No size limit → **medium** (memory exhaustion, storage bill)
- User-supplied filename reaching a path → **high** (traversal or overwrite)
- Open storage bucket → **critical** — this is failure 1 in a different room

## False positives

- Uploads restricted at the CDN or WAF layer do not appear in code. Ask before reporting absence.
- A signed-URL flow moves the checks to the URL-issuing endpoint. Audit that endpoint instead of the client.

## Evidence to capture

The upload handler (file:line), which of the five checks are present, and where
the file ends up — bucket, path, and serving origin.

Remediation: `vibe-fix` reference `fix-05b-uploads.md`.
