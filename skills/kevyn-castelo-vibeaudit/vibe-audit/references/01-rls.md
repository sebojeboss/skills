# Failure 1 — Row Level Security disabled

## Why this is the worst one

Supabase and Firebase invert the usual architecture: the database is reachable **directly from the browser**, with no server in between filtering anything. The `anon` key is public by design — it ships in the bundle and that is intended. The only thing standing between an anonymous visitor and every row in the table is Row Level Security.

It ships **disabled**.

CVE-2025-48757 is the canonical demonstration: a single misconfiguration class exposed data across 170+ applications. One line of SQL per table prevents it.

## What to check

### A. Tables without RLS enabled

Run the parser:

```bash
python3 scripts/check_rls.py --path supabase/migrations
python3 scripts/check_rls.py --path .          # searches for *.sql anywhere
```

It reports three states per table:
- `NO_RLS` — table created, never enabled. **Critical** if it holds user data.
- `RLS_NO_POLICY` — enabled but zero policies. Denies everything, breaks the app, and the usual "fix" is disabling RLS again. Report it as **High** with that context.
- `OK` — enabled with at least one policy. Still read the policy (see C).

If the project has live credentials and the user consents, the authoritative check is against the database itself:

```sql
SELECT schemaname, tablename, rowsecurity
FROM pg_tables
WHERE schemaname NOT IN ('pg_catalog','information_schema')
ORDER BY rowsecurity, tablename;
```

```sql
SELECT schemaname, tablename, policyname, cmd, qual, with_check
FROM pg_policies
ORDER BY tablename;
```

Migration files can lie — someone may have toggled RLS in the dashboard. Prefer the live query when it is available, and note in the report which source you used.

### B. `service_role` key reachable from the browser

This is the same failure wearing a different hat: `service_role` **bypasses RLS entirely**. If it reaches the client, no policy matters.

```bash
grep -rIn --exclude-dir={node_modules,.git,dist,build,.next} \
  -e 'service_role' -e 'SERVICE_ROLE' -e 'serviceRole' .
```

Flag as **critical** if it appears in:
- any variable prefixed `VITE_`, `NEXT_PUBLIC_`, `REACT_APP_`, `PUBLIC_`, `EXPO_PUBLIC_`, `NUXT_PUBLIC_`
- any file under a client/frontend directory
- a built bundle (`dist/`, `build/`, `.next/static/`)

Check the built output directly, not just the source — this is where the assumption breaks:

```bash
grep -rIn -e 'service_role' -e 'eyJ' dist/ build/ .next/static/ 2>/dev/null | head -50
```

Supabase JWTs decode without a secret. If you find one and need to confirm which role it carries, decode the middle segment:

```bash
echo '<jwt>' | cut -d. -f2 | base64 -d 2>/dev/null
```

A `"role":"service_role"` claim in a client bundle is a full database compromise. A `"role":"anon"` claim there is expected and fine.

### C. Policies that exist but do not restrict

RLS on with a permissive policy is decorative. Read every policy for the `USING` clause:

- `USING (true)` — allows all rows. Legitimate only for genuinely public tables (a published blog posts table). Anything else is **critical**.
- Policy without `WITH CHECK` on `INSERT`/`UPDATE` — reads are constrained, writes are not. A user can write rows they cannot read back, including rows owned by someone else.
- `USING (auth.uid() IS NOT NULL)` — this only checks that *someone* is logged in, not that it is the right someone. Any authenticated user sees every row. Very common, **critical** in practice.
- Ownership comparison against a client-supplied column rather than `auth.uid()`.

The shape you want is a comparison between `auth.uid()` and a column on the row itself.

### D. Firebase equivalent

Read `firestore.rules` / `storage.rules` (or `database.rules.json` for RTDB):

```bash
find . -name 'firestore.rules' -o -name 'storage.rules' -o -name 'database.rules.json' | grep -v node_modules
```

Critical patterns:
- `allow read, write: if true;`
- `".read": true` / `".write": true`
- rules whose expiry date has passed or is a test-mode placeholder — the default scaffold grants open access until a date, and expiry means the app breaks, which pressures people into setting `if true`
- `request.auth != null` alone, for the same reason as `auth.uid() IS NOT NULL` above

Also check that a matching rule actually covers each collection the client reads. Firestore denies by default, but wildcard `match /{document=**}` blocks written near the top routinely swallow everything below.

## False positives

- Tables in schemas not exposed to PostgREST are not client-reachable. Check the exposed-schemas setting before flagging non-`public` tables.
- Views do not inherit RLS from their base tables in older Postgres, but they also run as the view owner — a view over a protected table can be its own leak. Check views separately rather than assuming either way.
- A table that is genuinely public reference data (currency codes, plan tiers) with `USING (true)` is fine. Say so in the "Clean" section rather than silently skipping it.

## Evidence to capture

For each finding: the table name, the migration file and line where it was created, whether any `ENABLE ROW LEVEL SECURITY` exists for it anywhere in the repo, and the column names — column names are what tell the reader whether this table holds user data or lookup data.

Remediation: `vibe-fix` reference `fix-01-rls.md`.
