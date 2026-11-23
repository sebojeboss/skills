# Failure 3 — Fetching by ID without checking the owner (IDOR / BOLA)

## The shape of it

`GET /api/invoices/1042` returns invoice 1042. The user is authenticated, the token is valid, the middleware passed. Then someone changes the number to 1041 and receives an invoice belonging to a different company.

This is Broken Object Level Authorization — API #1 on the OWASP API Security Top 10 — and it is the failure AI-generated CRUD produces most reliably, because "write me an endpoint that returns a record by ID" is a complete specification of exactly this bug. Authentication and authorization get conflated: the handler confirms *who you are* and never asks *whether this record is yours*.

## What to check

### A. Enumerate every route that accepts an identifier

```bash
# Express / Fastify / NestJS
grep -rIn --exclude-dir={node_modules,.git} \
  -E "(get|post|put|patch|delete)\(['\"][^'\"]*:[a-zA-Z]+" \
  --include='*.ts' --include='*.js' .

# Next.js App Router — dynamic segments
find . -path ./node_modules -prune -o -type d -name '\[*\]' -print

# FastAPI / Flask
grep -rIn -E "@(app|router)\.(get|post|put|patch|delete)\(.*\{" --include='*.py' .
grep -rIn -E "@app\.route\(.*<" --include='*.py' .

# Django
grep -rIn -E "<(int|str|uuid|slug):" --include='urls.py' .
```

Also catch the ones taking an ID in the body or query rather than the path — the bug is identical and the grep above misses them:

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'body.id' -e 'body.userId' -e 'body\.\w*Id' \
  -e 'query.id' -e 'searchParams.get' .
```

### B. Trace each handler

For every route, follow the identifier from request to query and answer: **is the authenticated subject's ID part of the lookup, or checked against the result?**

Two sound shapes:

*Scoped query* — ownership is in the `WHERE` clause, so a foreign ID simply returns nothing:
```
findOne({ id: params.id, ownerId: session.user.id })
```

*Fetch then verify* — load, compare, reject:
```
record = findById(params.id)
if record.ownerId != session.user.id: return 404
```

The vulnerable shape is a lookup on the ID alone with no subsequent comparison:
```
findById(params.id)  →  return record
```

Grep for the vulnerable shape as a starting point, then read the handlers:

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'findById' -e 'findUnique' -e 'findOne' -e 'get(id' -e '.get(' \
  -e 'query.get' -e 'objects.get' -e 'session.get' .
```

Then check each hit for a nearby ownership comparison. Absence of one is the finding.

### C. ORM-specific traps

- **Prisma**: `findUnique({ where: { id } })` cannot express a compound ownership filter unless the schema declares one. The common correct pattern is `findFirst({ where: { id, ownerId } })`. `findUnique` on a bare ID followed by no check is the classic hit.
- **Supabase client**: `.from('t').select().eq('id', id)` is safe *only if RLS covers the table*. Server-side code using `service_role` bypasses RLS — so the same line that is safe in the browser is a vulnerability in an API route. Check which key the client was constructed with. This intersects with failure 1; report it under whichever gives the reader the clearer picture, and cross-reference.
- **Django**: `Model.objects.get(pk=pk)` unfiltered. `get_object_or_404(Model, pk=pk, owner=request.user)` is the fix shape.
- **Mongoose**: `findById` — same as Prisma. Look for `findOne({ _id, owner })`.

### D. Mutations matter more than reads

Check `PUT`, `PATCH` and `DELETE` first. An unprotected read leaks data; an unprotected write destroys or hijacks it. Handlers that update by ID are frequently even thinner than the read handlers, because "update the record with this ID using this body" reads like a complete instruction.

Also check for **mass assignment** while you are in there: an update handler spreading the whole request body into the record lets a user set `ownerId`, `role`, `isPaid`, or `balance` on a record they legitimately own.

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'data: req.body' -e 'data: body' -e '\.\.\.req\.body' -e '\.\.\.body' \
  -e 'update(req.body' -e 'Object.assign(' .
```

### E. Nested and indirect ownership

`GET /api/projects/:projectId/tasks/:taskId` — checking that the project belongs to the user is not enough if the task's `projectId` is never compared against `:projectId`. A user can pass their own project ID with someone else's task ID. Verify the full chain, not just the first link.

### F. Predictable identifiers raise severity

Sequential integers mean the whole table is enumerable in a loop. UUIDv4 does not fix the vulnerability — it is not an access control — but it changes exposure from "everything" to "whatever leaks a reference". Note the ID type in the finding; it belongs in the impact assessment, not in the fix.

## Severity

- Unauthenticated + no ownership check → **critical**
- Authenticated, any user reads another's records → **critical**
- Authenticated, any user writes/deletes another's records → **critical**
- Ownership checked but only on the first level of a nested route → **high**
- Mass assignment on an owned record → **high**

## False positives

- Genuinely public resources by design (a public profile page, a shared link feature) — but confirm the *intent* with the user rather than inferring it from the route name.
- Endpoints where RLS on the database already enforces ownership *and* the server uses the user-scoped client, not `service_role`. Verify which key; do not assume.
- Admin endpoints that are supposed to read any record — provided failure 2 checks out for them.

## Evidence to capture

Route path and method, handler file:line, the exact lookup call, and confirmation that no ownership comparison exists between the lookup and the response. Include the ID type.

Remediation: `vibe-fix` reference `fix-03-idor.md`.
