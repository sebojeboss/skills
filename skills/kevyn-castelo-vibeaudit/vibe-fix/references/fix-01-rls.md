# Fix 1 — Enable Row Level Security with scoped policies

## Warn first

Enabling RLS breaks the app. Every query that worked because the table was open now returns nothing until a policy allows it. Tell the user this before running the migration — otherwise they see a blank dashboard, assume the fix was wrong, and disable RLS. That rollback is the single most common way this vulnerability comes back.

Do it on a branch, against a staging database if one exists.

## Step 0 — `service_role` out of the client, first

None of what follows matters if the admin key is in the bundle: `service_role` bypasses every policy. Fix that before writing a single policy — see `fix-04-secrets.md`. In the browser, only the `anon` key.

## Step 1 — Enable, table by table

```sql
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
```

Generate the statements from the audit output rather than by hand:

```bash
python3 <path-to>/vibe-audit/scripts/check_rls.py --path supabase/migrations --json \
  | python3 -c "import json,sys; [print(f'ALTER TABLE {t[\"table\"]} ENABLE ROW LEVEL SECURITY;') for t in json.load(sys.stdin)['tables'] if t['status']=='NO_RLS']"
```

Review the list before applying. A lookup table of currency codes does not need the same treatment as a table of invoices — though enabling RLS on it and adding a read-only policy costs nothing and removes a decision from the next person.

## Step 2 — Policies per access pattern

RLS on with no policy denies everything. Write policies for what the app actually does.

### Owner-only (the common case)

```sql
CREATE POLICY "select own profile" ON public.profiles
  FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "insert own profile" ON public.profiles
  FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "update own profile" ON public.profiles
  FOR UPDATE USING (auth.uid() = user_id)
              WITH CHECK (auth.uid() = user_id);

CREATE POLICY "delete own profile" ON public.profiles
  FOR DELETE USING (auth.uid() = user_id);
```

`USING` controls which rows are visible to the operation. `WITH CHECK` controls which rows may be written. Both are needed on `UPDATE` — with `USING` alone, a user can take a row they own and rewrite `user_id` to hand it to someone else, or take ownership of nothing and leave it orphaned.

Separate policies per command beat one `FOR ALL`, because they make the intent readable and let you tighten one operation without touching the others.

### Public read, owner write

```sql
CREATE POLICY "anyone reads published" ON public.posts
  FOR SELECT USING (published = true);

CREATE POLICY "author writes own" ON public.posts
  FOR INSERT WITH CHECK (auth.uid() = author_id);
```

### Membership / team scoping

Direct subqueries in policies recurse badly and run per row. Use a `SECURITY DEFINER` helper:

```sql
CREATE OR REPLACE FUNCTION public.is_org_member(org uuid)
RETURNS boolean
LANGUAGE sql
SECURITY DEFINER
SET search_path = public
STABLE
AS $$
  SELECT EXISTS (
    SELECT 1 FROM public.memberships
    WHERE org_id = org AND user_id = auth.uid()
  );
$$;

CREATE POLICY "org members read" ON public.documents
  FOR SELECT USING (public.is_org_member(org_id));
```

`SECURITY DEFINER` bypasses RLS *inside the function* — that is why it avoids the recursion, and also why the function body must be tightly scoped and must pin `search_path`. A `SECURITY DEFINER` function taking user-controlled input and building dynamic SQL is a privilege-escalation path; keep the body to a fixed query.

### Roles

The role must live where the user cannot write it. If `role` is a column on a profiles table the user can `UPDATE`, they promote themselves — you have moved the vulnerability, not fixed it.

```sql
CREATE TABLE public.user_roles (
  user_id uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  role text NOT NULL CHECK (role IN ('user','admin'))
);
ALTER TABLE public.user_roles ENABLE ROW LEVEL SECURITY;

-- readable by the owner, writable by nobody through the API
CREATE POLICY "read own role" ON public.user_roles
  FOR SELECT USING (auth.uid() = user_id);

CREATE OR REPLACE FUNCTION public.is_admin()
RETURNS boolean LANGUAGE sql SECURITY DEFINER SET search_path = public STABLE AS $$
  SELECT EXISTS (SELECT 1 FROM public.user_roles WHERE user_id = auth.uid() AND role = 'admin');
$$;

CREATE POLICY "admins read all invoices" ON public.invoices
  FOR SELECT USING (public.is_admin());
```

With no write policy, `user_roles` is modifiable only via `service_role` from a server context. That is the point.

## Step 3 — Performance

`auth.uid()` re-evaluates per row. Wrapping it makes Postgres treat it as a constant:

```sql
-- slow on large tables
USING (auth.uid() = user_id)
-- fast
USING ((SELECT auth.uid()) = user_id)
```

Index the column every policy filters on:

```sql
CREATE INDEX IF NOT EXISTS idx_profiles_user_id ON public.profiles (user_id);
```

Policies that cause table scans get blamed for slowness and removed. Indexing them is part of making the fix stick.

## Step 4 — Firebase equivalent

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    match /profiles/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }

    match /posts/{postId} {
      allow read: if resource.data.published == true;
      allow create: if request.auth != null
                    && request.request.resource.data.authorId == request.auth.uid;
      allow update, delete: if request.auth != null
                    && resource.data.authorId == request.auth.uid;
    }

    // deny anything not matched above
    match /{document=**} {
      allow read, write: if false;
    }
  }
}
```

Two things people get wrong here. `resource.data` is the *existing* document; `request.resource.data` is the incoming one — an update rule needs both to stop a user reassigning ownership. And the catch-all deny must be last; a permissive wildcard placed early swallows every rule beneath it.

Storage rules are separate and are missed constantly:

```javascript
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{userId}/{fileName} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow write: if request.auth != null
                   && request.auth.uid == userId
                   && request.resource.size < 5 * 1024 * 1024
                   && request.resource.contentType.matches('image/.*');
    }
  }
}
```

Test with the emulator before deploying:
```bash
firebase emulators:start --only firestore
firebase deploy --only firestore:rules,storage
```

## Verify

```sql
SELECT tablename, rowsecurity FROM pg_tables
WHERE schemaname = 'public' ORDER BY rowsecurity;

SELECT tablename, policyname, cmd, qual, with_check FROM pg_policies
ORDER BY tablename;
```

Then the functional check, which is the one that matters: log in as user A and confirm the app works; query with user B's session and confirm A's rows are not visible. Supabase's SQL editor runs as a superuser and bypasses RLS — testing there proves nothing. Use the client with a real user token.

## Make it stick

New tables default to RLS off, so the failure recurs on the next generated feature. A migration template that includes the `ENABLE` line, or a CI check that fails when a `CREATE TABLE` in `public` lands without a matching `ENABLE ROW LEVEL SECURITY`, converts "someone remembered" into "the build enforces it".
