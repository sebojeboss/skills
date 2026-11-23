# Failure 2 — Authorization decided in the frontend

## The shape of it

An AI asked to "add an admin panel" produces exactly what was asked: a menu item that appears when `user.isAdmin` is true. That is a *rendering* decision, and it is correct as a rendering decision. It becomes a vulnerability the moment it is also the *only* decision — when the server behind that menu trusts whoever calls it.

The frontend cannot enforce anything. It runs on the attacker's machine. React DevTools, a paused debugger, or a hand-rolled `fetch` from the console bypasses every check in the bundle. Frontend permission checks are a UX feature; the server is the security boundary.

## What to check

### A. Find the frontend permission checks

```bash
grep -rIn --exclude-dir={node_modules,.git,dist,build,.next} \
  -e 'isAdmin' -e 'is_admin' -e 'role ===' -e 'role ==' -e "role\s*!=" \
  -e 'hasPermission' -e 'canEdit' -e 'userRole' -e 'user\.role' \
  -e 'permissions\.includes' -e 'ADMIN' \
  --include='*.tsx' --include='*.jsx' --include='*.ts' --include='*.js' \
  --include='*.vue' --include='*.svelte' .
```

Each hit is a *lead*, not a finding. The finding is on the server side.

### B. For each one, trace to the server

This is the whole check. Take the guarded capability — "delete any user", "view all orders", "change plan" — and find the endpoint that performs it. Then answer one question:

> If I call this endpoint directly with a valid non-admin session token, does it refuse?

Look at the handler itself. Not the router config, not a comment, not the client that calls it. The handler.

Findings:
- Endpoint has **no** role check → **critical**
- Endpoint checks a role supplied in the request body, query string, or a custom header → **critical** (the client controls it; it is not a check)
- Endpoint reads the role from the JWT/session but the token is issued with client-supplied claims → **critical**
- Endpoint checks a role loaded from the database using the authenticated subject's ID → sound

### C. Role coming from the wrong place

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'req.body.role' -e 'req.query.role' -e 'req.headers\[.x-role' \
  -e 'body.isAdmin' -e 'params.role' -e 'searchParams.get(.role' .
```

Any authorization decision reading from `body`, `query`, `params`, or a custom header is client-controlled. Critical.

Also check where the role is *stored*. In Supabase, a `role` column on a user-writable table is the same bug one layer down: if a user can `UPDATE` their own profile row and `role` is a column on it, they promote themselves. The role must live somewhere the user cannot write — a separate table with its own restrictive policy, or a JWT custom claim set server-side.

### D. Route-level protection that only exists in the client router

```bash
grep -rIn --exclude-dir={node_modules,.git} \
  -e 'ProtectedRoute' -e 'RequireAuth' -e 'AuthGuard' -e 'requireAuth' \
  -e 'beforeEnter' -e 'canActivate' -e 'middleware.*auth' .
```

A client-side route guard hides a page. It does not protect the data the page fetches. For every guarded route, check whether its data endpoints are independently protected. If the guard is the only thing standing between a user and the data, the data is public.

Next.js specifically: `middleware.ts` matchers are easy to get wrong. Confirm the matcher pattern actually covers the API routes, not just the page routes — and remember middleware does not run for every rendering path in every version. Server-side checks inside the handler are the reliable layer.

### E. Server Components and server actions

In Next.js App Router, `"use server"` functions are network endpoints. They are callable directly regardless of which component renders the button that calls them.

```bash
grep -rIn --include='*.ts' --include='*.tsx' -e '"use server"' -e "'use server'" . | grep -v node_modules
```

Every server action needs its own auth check inside the function body. Being imported only by an admin-gated component protects nothing.

## Verifying a finding

The clean way to confirm without touching production: read the handler and show that no branch rejects a non-privileged subject. That is sufficient evidence for the report — trace the code path, quote the handler, done.

If the user wants a live confirmation, that is their call to make on their own staging environment with their own account. Do not run credential-based probes against systems on the user's behalf without them explicitly setting that up.

## False positives

- A check duplicated in both places is correct architecture, not redundancy. Frontend for UX, server for enforcement. Do not report the frontend copy as a finding when the server copy exists — say it is sound.
- Static site generators with no backend: if a "role" only controls which static content renders and there is no protected data behind it, there is nothing to enforce. Note it and move on.
- An internal admin tool on a private network still needs the check, but the severity is lower. Reflect that rather than pretending network isolation counts for nothing or for everything.

## Evidence to capture

The frontend check (file:line), the server handler it corresponds to (file:line), and the specific absence — quote the handler's opening lines showing what it does before touching data.

Remediation: `vibe-fix` reference `fix-02-broken-authz.md`.
