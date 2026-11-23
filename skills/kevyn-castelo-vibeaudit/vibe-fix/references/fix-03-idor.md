# Fix 3 — Add the ownership check

## The two correct shapes

**Scoped query** — put ownership in the `WHERE` clause. A foreign ID returns nothing; there is no window between fetch and check, and no way to forget the check because it is the query.

```typescript
const invoice = await db.invoice.findFirst({
  where: { id: params.id, ownerId: user.id },
})
if (!invoice) return new Response('Not found', { status: 404 })
```

**Fetch then verify** — needed when you must distinguish "does not exist" from "not yours", or when the ownership rule is more complex than a column comparison.

```typescript
const invoice = await db.invoice.findUnique({ where: { id: params.id } })
if (!invoice || invoice.ownerId !== user.id) {
  return new Response('Not found', { status: 404 })
}
```

Prefer the scoped query. It is one statement, and the failure mode of forgetting to write the second half does not exist.

## 404, not 403

Returning 403 for someone else's record confirms the record exists. That turns the endpoint into an enumeration oracle: an attacker learns which IDs are real even without reading them. Return 404 for both "no such record" and "not yours" — unless the resource is genuinely shared and the user needs to know it exists to request access, which is a deliberate product decision.

## ORM specifics

**Prisma** — `findUnique` only accepts unique fields, which is why AI-generated handlers land on it and then have nowhere to put the owner. Use `findFirst`:
```typescript
db.invoice.findFirst({ where: { id, ownerId: user.id } })
```
Updates and deletes take the compound filter directly:
```typescript
db.invoice.updateMany({ where: { id, ownerId: user.id }, data: { status } })
// count === 0 means it wasn't theirs
```
`updateMany`/`deleteMany` over `update`/`delete` for exactly this reason — the single-record versions cannot express the ownership filter.

**Drizzle**
```typescript
db.select().from(invoices)
  .where(and(eq(invoices.id, id), eq(invoices.ownerId, user.id)))
```

**Django**
```python
invoice = get_object_or_404(Invoice, pk=pk, owner=request.user)
```
DRF, on the viewset so every action inherits it:
```python
def get_queryset(self):
    return Invoice.objects.filter(owner=self.request.user)
```

**SQLAlchemy**
```python
invoice = session.query(Invoice).filter_by(id=id, owner_id=user.id).first()
if not invoice:
    raise HTTPException(404)
```

**Mongoose**
```javascript
const doc = await Invoice.findOne({ _id: id, owner: user.id })
```

**Supabase client** — `.eq('id', id)` is safe *only if RLS covers the table and the client was built with the anon key plus the user's session*. In a server route using `service_role`, RLS is bypassed and you must add the filter yourself:
```typescript
.from('invoices').select().eq('id', id).eq('owner_id', user.id).single()
```
The same line is safe in one place and vulnerable in another depending on the key. This is the trap worth naming explicitly in the fix.

## Nested routes — check the whole chain

`/api/projects/:projectId/tasks/:taskId`. Verifying the project belongs to the user is not enough if the task's `projectId` is never compared to `:projectId` — a user passes their own project ID with someone else's task ID and the first check passes.

```typescript
const task = await db.task.findFirst({
  where: {
    id: params.taskId,
    projectId: params.projectId,
    project: { ownerId: user.id },   // ownership at the root of the chain
  },
})
```

One query, whole chain. Splitting it into sequential checks is where links get dropped.

## Mass assignment

An update handler spreading the request body lets a user set fields they should never control:

```typescript
// vulnerable — user sends { ownerId, isPaid, balance }
await db.invoice.update({ where: { id }, data: req.body })
```

Whitelist through a schema:

```typescript
const UpdateInvoice = z.object({
  title: z.string().min(1).max(200),
  notes: z.string().max(2000).optional(),
}).strict()          // reject unknown keys rather than dropping them silently

const data = UpdateInvoice.parse(req.body)
await db.invoice.updateMany({ where: { id, ownerId: user.id }, data })
```

`.strict()` matters: without it an extra `role` field is silently ignored, which is safe here but hides the attempt. Rejecting surfaces it.

Pydantic equivalent: `model_config = ConfigDict(extra='forbid')`.

## Push the check to the database

Application-layer checks hold until someone adds an endpoint and forgets. RLS holds regardless of how many endpoints exist. If Supabase or Postgres RLS is available, the ownership policy from `fix-01-rls.md` is a second layer that catches the route you have not written yet. Do both.

## Shared helper

```typescript
export async function findOwned<T>(
  model: { findFirst: (a: any) => Promise<T | null> },
  id: string,
  userId: string,
) {
  const record = await model.findFirst({ where: { id, ownerId: userId } })
  if (!record) throw new HttpError(404, 'Not found')
  return record
}
```

## IDs

Sequential integers make the whole table enumerable in a loop. Switching to UUIDv4 does not fix the vulnerability — an ID is not an access control, and treating it as one is the "security through obscurity" version of this bug — but it does reduce blast radius from "everything" to "whatever leaks a reference". Change IDs as hardening after the ownership check exists, never instead of it.

## Verify

With a valid session for user A, request one of user B's record IDs on every fixed route. Expect 404 and no data. Do the same for `PUT`, `PATCH` and `DELETE` — mutations are where the thin handlers live, and where an unfixed route does the most damage.
