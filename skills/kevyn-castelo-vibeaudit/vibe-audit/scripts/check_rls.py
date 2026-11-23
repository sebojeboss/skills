#!/usr/bin/env python3
"""
check_rls.py — find Postgres/Supabase tables that never get Row Level Security.

Parses CREATE TABLE / ALTER TABLE ... ENABLE ROW LEVEL SECURITY / CREATE POLICY
across a directory of .sql files and reports, per table:

  NO_RLS         created, RLS never enabled          -> critical if it holds user data
  RLS_NO_POLICY  RLS on, zero policies               -> denies everything; gets "fixed"
                                                        by turning RLS back off
  PERMISSIVE     RLS on, but a policy allows all rows -> decorative
  OK             RLS on with at least one scoped policy

Migrations can lie — someone may have toggled RLS in the dashboard. When live
credentials exist, prefer querying pg_tables / pg_policies directly. Use this
when you only have the repo.

Usage:
    python3 check_rls.py --path supabase/migrations
    python3 check_rls.py --path . --json
"""

import argparse
import json
import os
import re
import sys

# Strip line comments and block comments so commented-out DDL doesn't count.
RE_LINE_COMMENT = re.compile(r"--[^\n]*")
RE_BLOCK_COMMENT = re.compile(r"/\*.*?\*/", re.S)

RE_CREATE_TABLE = re.compile(
    r"\bcreate\s+table\s+(?:if\s+not\s+exists\s+)?"
    r"(?P<name>(?:\"[^\"]+\"|[\w]+)(?:\s*\.\s*(?:\"[^\"]+\"|[\w]+))?)",
    re.I,
)
RE_ENABLE_RLS = re.compile(
    r"\balter\s+table\s+(?:if\s+exists\s+)?(?:only\s+)?"
    r"(?P<name>(?:\"[^\"]+\"|[\w]+)(?:\s*\.\s*(?:\"[^\"]+\"|[\w]+))?)"
    r"\s+enable\s+row\s+level\s+security",
    re.I,
)
RE_DISABLE_RLS = re.compile(
    r"\balter\s+table\s+(?:if\s+exists\s+)?(?:only\s+)?"
    r"(?P<name>(?:\"[^\"]+\"|[\w]+)(?:\s*\.\s*(?:\"[^\"]+\"|[\w]+))?)"
    r"\s+disable\s+row\s+level\s+security",
    re.I,
)
RE_POLICY = re.compile(
    r"\bcreate\s+policy\s+(?P<policy>\"[^\"]+\"|[\w]+)\s+on\s+"
    r"(?P<name>(?:\"[^\"]+\"|[\w]+)(?:\s*\.\s*(?:\"[^\"]+\"|[\w]+))?)"
    r"(?P<body>.*?)(?=;)",
    re.I | re.S,
)

# Columns whose presence means "this table holds user data", which raises severity.
SENSITIVE_HINTS = re.compile(
    r"\b(user_id|owner_id|account_id|email|phone|cpf|cnpj|password|token|"
    r"stripe|customer|address|balance|amount|salary|ssn|birth|document|"
    r"medical|patient|diagnosis|prescription)\b",
    re.I,
)

# Policy predicates that don't actually scope anything to the caller.
RE_USING_TRUE = re.compile(r"using\s*\(\s*true\s*\)", re.I)
RE_ONLY_AUTHED = re.compile(
    r"using\s*\(\s*auth\.uid\(\)\s+is\s+not\s+null\s*\)", re.I
)
RE_AUTH_UID = re.compile(r"auth\.uid\(\)", re.I)
RE_WITH_CHECK = re.compile(r"with\s+check", re.I)
RE_WRITE_CMD = re.compile(r"\bfor\s+(insert|update|all)\b", re.I)


def norm(name: str) -> str:
    """public.\"Foo\" -> public.foo ; foo -> public.foo"""
    parts = [p.strip().strip('"').lower() for p in name.split(".")]
    if len(parts) == 1:
        return "public." + parts[0]
    return ".".join(parts)


def strip_comments(sql: str) -> str:
    sql = RE_BLOCK_COMMENT.sub(" ", sql)
    sql = RE_LINE_COMMENT.sub(" ", sql)
    return sql


def table_body(sql: str, start: int) -> str:
    """Grab the parenthesised column list following a CREATE TABLE match."""
    open_idx = sql.find("(", start)
    if open_idx == -1:
        return ""
    depth, i = 0, open_idx
    while i < len(sql):
        if sql[i] == "(":
            depth += 1
        elif sql[i] == ")":
            depth -= 1
            if depth == 0:
                return sql[open_idx : i + 1]
        i += 1
    return sql[open_idx : open_idx + 2000]


def collect(paths):
    files = []
    for path in paths:
        if os.path.isfile(path) and path.endswith(".sql"):
            files.append(path)
            continue
        for root, dirs, names in os.walk(path):
            dirs[:] = [
                d
                for d in dirs
                if d not in {"node_modules", ".git", "dist", "build", ".next",
                             "venv", ".venv", "__pycache__", "vendor"}
            ]
            for n in names:
                if n.endswith(".sql"):
                    files.append(os.path.join(root, n))
    return sorted(set(files))


def analyse(files):
    tables = {}

    def entry(name):
        return tables.setdefault(
            name,
            {
                "table": name,
                "created_in": None,
                "rls_enabled": False,
                "rls_disabled_later": False,
                "policies": [],
                "sensitive_columns": [],
                "notes": [],
            },
        )

    for f in files:
        try:
            with open(f, "r", encoding="utf-8", errors="replace") as fh:
                raw = fh.read()
        except OSError as e:
            print(f"  ! could not read {f}: {e}", file=sys.stderr)
            continue

        sql = strip_comments(raw)

        for m in RE_CREATE_TABLE.finditer(sql):
            name = norm(m.group("name"))
            e = entry(name)
            if e["created_in"] is None:
                line = sql[: m.start()].count("\n") + 1
                e["created_in"] = f"{f}:{line}"
            body = table_body(sql, m.end())
            cols = sorted(set(x.lower() for x in SENSITIVE_HINTS.findall(body)))
            for c in cols:
                if c not in e["sensitive_columns"]:
                    e["sensitive_columns"].append(c)

        for m in RE_ENABLE_RLS.finditer(sql):
            entry(norm(m.group("name")))["rls_enabled"] = True

        for m in RE_DISABLE_RLS.finditer(sql):
            e = entry(norm(m.group("name")))
            e["rls_disabled_later"] = True
            line = sql[: m.start()].count("\n") + 1
            e["notes"].append(f"RLS explicitly DISABLED at {f}:{line}")

        for m in RE_POLICY.finditer(sql):
            e = entry(norm(m.group("name")))
            body = m.group("body") or ""
            pol = {
                "name": m.group("policy").strip('"'),
                "file": f,
                "permissive_true": bool(RE_USING_TRUE.search(body)),
                "only_authenticated": bool(RE_ONLY_AUTHED.search(body)),
                "references_auth_uid": bool(RE_AUTH_UID.search(body)),
                "is_write": bool(RE_WRITE_CMD.search(body)),
                "has_with_check": bool(RE_WITH_CHECK.search(body)),
            }
            e["policies"].append(pol)

    for e in tables.values():
        e["sensitive"] = bool(e["sensitive_columns"])
        if not e["rls_enabled"] or e["rls_disabled_later"]:
            e["status"] = "NO_RLS"
            e["severity"] = "CRITICAL" if e["sensitive"] else "HIGH"
        elif not e["policies"]:
            e["status"] = "RLS_NO_POLICY"
            e["severity"] = "HIGH"
            e["notes"].append(
                "RLS on with no policy denies all access; the usual 'fix' is "
                "disabling RLS again. Add scoped policies instead."
            )
        else:
            perm = [p for p in e["policies"] if p["permissive_true"]]
            authed = [p for p in e["policies"] if p["only_authenticated"]]
            nocheck = [
                p for p in e["policies"] if p["is_write"] and not p["has_with_check"]
            ]
            if perm:
                e["status"] = "PERMISSIVE"
                e["severity"] = "CRITICAL" if e["sensitive"] else "MEDIUM"
                e["notes"].append(
                    "USING (true) allows every row: "
                    + ", ".join(p["name"] for p in perm)
                )
            elif authed:
                e["status"] = "PERMISSIVE"
                e["severity"] = "CRITICAL" if e["sensitive"] else "MEDIUM"
                e["notes"].append(
                    "auth.uid() IS NOT NULL only checks that *someone* is logged in, "
                    "not that it is the right someone: "
                    + ", ".join(p["name"] for p in authed)
                )
            else:
                e["status"] = "OK"
                e["severity"] = "INFO"
            if nocheck:
                e["notes"].append(
                    "Write policy without WITH CHECK (user may write rows they "
                    "cannot read): " + ", ".join(p["name"] for p in nocheck)
                )
            if not any(p["references_auth_uid"] for p in e["policies"]):
                e["notes"].append(
                    "No policy references auth.uid(); confirm ownership is scoped "
                    "to the caller and not to a client-supplied value."
                )

    return tables


ORDER = {"NO_RLS": 0, "PERMISSIVE": 1, "RLS_NO_POLICY": 2, "OK": 3}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--path", "-p", action="append", default=None,
                    help="file or directory to scan (repeatable)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    paths = args.path or ["supabase/migrations", "migrations", "db", "."]
    paths = [p for p in paths if os.path.exists(p)] or ["."]

    files = collect(paths)
    if not files:
        print("No .sql files found. If the schema lives only in the Supabase "
              "dashboard, query pg_tables and pg_policies directly instead.")
        return 0

    tables = analyse(files)

    if args.json:
        print(json.dumps(
            {"files_scanned": files, "tables": list(tables.values())}, indent=2
        ))
        return 0

    print(f"Scanned {len(files)} .sql file(s), found {len(tables)} table(s).\n")

    rows = sorted(tables.values(), key=lambda e: (ORDER.get(e["status"], 9), e["table"]))
    bad = [e for e in rows if e["status"] != "OK"]

    for e in rows:
        flag = {"NO_RLS": "❌", "RLS_NO_POLICY": "⚠️ ", "PERMISSIVE": "⚠️ ", "OK": "✅"}[e["status"]]
        print(f"{flag} {e['table']}  [{e['status']}]  severity={e['severity']}")
        if e["created_in"]:
            print(f"     created: {e['created_in']}")
        if e["sensitive_columns"]:
            print(f"     user-data columns: {', '.join(e['sensitive_columns'])}")
        if e["policies"]:
            print(f"     policies: {', '.join(p['name'] for p in e['policies'])}")
        for n in e["notes"]:
            print(f"     · {n}")
        print()

    print("-" * 60)
    if bad:
        print(f"{len(bad)} table(s) need attention.\n")
        print("For each NO_RLS table:")
        print("    ALTER TABLE <table> ENABLE ROW LEVEL SECURITY;")
        print("then add scoped policies — see vibe-fix/references/fix-01-rls.md.\n")
        print("Reminder: the service_role key bypasses every policy here. Confirm")
        print("it never reaches the browser, or none of this matters.")
    else:
        print("Every table found has RLS enabled with at least one scoped policy.")
        print("Still verify against the live database — migrations can be stale.")

    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
