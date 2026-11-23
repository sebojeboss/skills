# Fix 2 — Move the authorization decision to the server

## The principle

Keep the frontend check. Add the server check. The frontend one is a UX feature — it stops users from seeing buttons that would fail — and removing it makes the app worse without making it safer. What changes is that the frontend check stops being the *only* one.

The role must come from a source the client cannot influence: a session looked up server-side, or a JWT claim signed by your server. Never from the request body, a query parameter, or a custom header.

## Next.js App Router

Route handlers:

```typescript
// app/api/admin/users/route.ts
import { createServerClient } from '@/lib/supabase/server'
import { NextResponse } from 'next/server'

export async function GET() {
  const supabase = createServerClient()

  const { data: { user } } = await supabase.auth.getUser()
  if (!user) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 })
  }

  const { data: roleRow } = await supabase
    .from('user_roles')
    .select('role')
    .eq('user_id', user.id)
    .single()

  if (roleRow?.role !== 'admin') {
    return NextResponse.json({ error: 'Forbidden' }, { status: 403 })
  }

  // ...
}
```

`getUser()` rather than `getSession()`: `getUser` revalidates the token with the auth server, `getSession` reads what the client sent. On the server, only the revalidated one is a security check.

Server actions are network endpoints regardless of which component renders the button:

```typescript
'use server'

export async function deleteUser(userId: string) {
  const admin = await requireAdmin()   // throws on failure
  // ...
}
```

Every `'use server'` function needs its own check inside the body. Being imported only by an admin-gated component protects nothing — the action is callable directly.

Middleware is useful for redirecting unauthenticated visitors, but do not treat it as the enforcement layer. Matchers are easy to get wrong, and middleware does not run on every path in every version. Put the check in the handler; use middleware for the redirect.

## Shared helper

The pattern that survives contact with a growing codebase is one helper everyone reaches for, because the correct thing has to be the easy thing:

```typescript
// lib/auth.ts
export async function requireUser() {
  const supabase = createServerClient()
  const { data: { user } } = await supabase.auth.getUser()
  if (!user) throw new HttpError(401, 'Unauthorized')
  return user
}

export async function requireAdmin() {
  const user = await requireUser()
  const { data } = await supabase
    .from('user_roles').select('role').eq('user_id', user.id).single()
  if (data?.role !== 'admin') throw new HttpError(403, 'Forbidden')
  return user
}
```

## Express / Fastify

```javascript
function requireAuth(req, res, next) {
  const token = req.headers.authorization?.replace('Bearer ', '')
  if (!token) return res.status(401).json({ error: 'Unauthorized' })
  try {
    req.user = jwt.verify(token, process.env.JWT_SECRET)
    next()
  } catch {
    return res.status(401).json({ error: 'Unauthorized' })
  }
}

function requireRole(...roles) {
  return async (req, res, next) => {
    const role = await db.getRole(req.user.sub)   // from the DB, not the token body
    if (!roles.includes(role)) return res.status(403).json({ error: 'Forbidden' })
    next()
  }
}

app.delete('/api/users/:id', requireAuth, requireRole('admin'), handler)
```

Note `jwt.verify`, not `jwt.decode`. `decode` reads the claims without checking the signature — anyone can forge a token that passes it. This is a real and frequent mistake.

Router-level mounting reduces the chance of a new route being added unguarded:

```javascript
const adminRouter = express.Router()
adminRouter.use(requireAuth, requireRole('admin'))
app.use('/api/admin', adminRouter)
```

## FastAPI

```python
from fastapi import Depends, HTTPException, status

async def current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = await verify_token(token)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")
    return user

async def require_admin(user: User = Depends(current_user)) -> User:
    if user.role != "admin":
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Forbidden")
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: str, admin: User = Depends(require_admin)):
    ...
```

Or on the whole router, so new endpoints inherit it:
```python
router = APIRouter(prefix="/admin", dependencies=[Depends(require_admin)])
```

## Django

```python
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_view(request): ...
```

DRF:
```python
class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminOnly]
```

Set a restrictive project-wide default so the failure mode of forgetting is a 403, not an open endpoint:
```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated'],
}
```

## Roles as JWT claims (Supabase)

To avoid a role lookup on every request, put the role in the token via a custom claims hook — set server-side, signed, unmodifiable by the client. Then policies and handlers read it directly:

```sql
CREATE POLICY "admins read all" ON public.invoices
  FOR SELECT USING (
    (auth.jwt() -> 'app_metadata' ->> 'role') = 'admin'
  );
```

`app_metadata` is writable only with `service_role`. `user_metadata` is writable by the user — never make an authorization decision from it. The two look almost identical in the token payload and that is exactly why this gets confused.

## Fix the family, not the instance

Unprotected routes come in batches, because they were generated from one template. After fixing one, enumerate its siblings:

```bash
grep -rIn -E "(get|post|put|patch|delete)\(['\"]" --include='*.ts' src/ | grep -v node_modules
```

List every route with its guard status. A report that fixes one of eight and reads as complete is worse than one that fixes one and names the other seven.

## Verify

Call the privileged endpoint with a non-privileged session token and confirm a 403. Confirm a valid admin still succeeds — a fix that locks out the admin gets reverted, and reverts do not come back.
