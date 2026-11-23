#!/usr/bin/env python3
"""Score creative-concept diversity for modern auction/retrieval engines.

Meta's Andromeda (and creative-led delivery generally) rewards genuinely distinct
CONCEPTS, and treats variations of one concept as effectively one ad (the "Entity-ID
trap"). This tool counts distinct concepts (not ad rows), format/angle coverage, and
flags when a big ad count hides a tiny idea count.

Recommendations only — it never edits campaigns.

Example:
    python score.py --csv creatives.csv --target-concepts 12
"""
from __future__ import annotations

import argparse
import csv
import json
import sys

ALIASES = {
    "concept": ["concept", "theme", "idea", "concept_name"],
    "format": ["format", "type", "media_type", "placement", "asset_type"],
    "angle": ["angle", "message", "hook_type", "angle_type"],
    "id": ["id", "ad_id", "creative_id", "name"],
}


def _resolve(fieldnames, key, override=None):
    norm = {f.strip().lower(): f for f in fieldnames}
    if override:
        return norm.get(override.strip().lower())
    for a in ALIASES[key]:
        if a in norm:
            return norm[a]
    return None


def load_creatives(csv_path, concept_col=None, format_col=None, angle_col=None):
    with open(csv_path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row.")
        cc = _resolve(reader.fieldnames, "concept", concept_col)
        fc = _resolve(reader.fieldnames, "format", format_col)
        ac = _resolve(reader.fieldnames, "angle", angle_col)
        if not cc:
            raise ValueError(
                "CSV needs a concept column (concept/theme/idea) so distinct ideas can be counted. "
                f"Found: {reader.fieldnames}"
            )
        rows = []
        for row in reader:
            rows.append(
                {
                    "concept": (row.get(cc) or "").strip(),
                    "format": (row.get(fc) or "").strip() if fc else "",
                    "angle": (row.get(ac) or "").strip() if ac else "",
                }
            )
    rows = [r for r in rows if r["concept"]]
    if not rows:
        raise ValueError("No rows with a concept value.")
    return rows, {"concept": cc, "format": fc, "angle": ac}


def score(rows, target_concepts=12) -> dict:
    total = len(rows)
    concepts = sorted({r["concept"] for r in rows})
    formats = sorted({r["format"] for r in rows if r["format"]})
    angles = sorted({r["angle"] for r in rows if r["angle"]})
    combos = {(r["concept"], r["format"]) for r in rows if r["format"]}

    variation_ratio = round(total / len(concepts), 2)
    concept_component = min(len(concepts) / target_concepts, 1.0) * 70
    format_component = min(len(formats) / 3, 1.0) * 30 if formats else 0.0
    diversity_score = round(concept_component + format_component)

    flags = []
    if len(concepts) < target_concepts:
        flags.append(
            f"UNDER-DIVERSE: {len(concepts)} distinct concepts (< target {target_concepts}). "
            "Creative-led delivery treats variations of one concept as one ad — add distinct concepts, "
            "not more crops of the same one."
        )
    if variation_ratio >= 3:
        flags.append(
            f"VARIATION-HEAVY: {total} creatives but only {len(concepts)} concepts "
            f"({variation_ratio}x variations each). Most of that volume counts as one entity."
        )
    if formats and len(formats) < 2:
        flags.append(f"SINGLE-FORMAT: only '{formats[0]}'. Add formats (e.g. video + static) to widen delivery.")
    if not formats:
        flags.append("No format column — can't assess format coverage.")

    return {
        "total_creatives": total,
        "distinct_concepts": len(concepts),
        "distinct_formats": len(formats),
        "distinct_angles": len(angles),
        "variation_ratio": variation_ratio,
        "concept_format_combos": len(combos),
        "target_concepts": target_concepts,
        "diversity_score": diversity_score,
        "concepts": concepts,
        "formats": formats,
        "flags": flags,
    }


def _render(r) -> str:
    lines = [
        "Creative Diversity Scorer - Entity-ID aware. Recommendations only.",
        "=" * 66,
        f"Creatives (rows)      : {r['total_creatives']}",
        f"Distinct concepts     : {r['distinct_concepts']} (target {r['target_concepts']})",
        f"Distinct formats      : {r['distinct_formats']}",
        f"Distinct angles       : {r['distinct_angles']}",
        f"Variations per concept: {r['variation_ratio']}x",
        f"Concept x format combos: {r['concept_format_combos']}",
        "-" * 66,
        f"DIVERSITY SCORE: {r['diversity_score']}/100",
        "-" * 66,
    ]
    if r["flags"]:
        lines.append("Flags:")
        for f in r["flags"]:
            lines.append(f"  ! {f}")
    else:
        lines.append("Flags: none - healthy concept diversity.")
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="score.py", description="Score creative-concept diversity. Recommendations only.")
    p.add_argument("--csv", required=True, help="Creatives CSV with a concept column (+ optional format/angle).")
    p.add_argument("--concept-col", default=None)
    p.add_argument("--format-col", default=None)
    p.add_argument("--angle-col", default=None)
    p.add_argument("--target-concepts", type=int, default=12, help="Distinct-concept target. Default 12.")
    p.add_argument("--json", action="store_true")
    args = p.parse_args(argv)

    try:
        rows, _ = load_creatives(args.csv, args.concept_col, args.format_col, args.angle_col)
        result = score(rows, args.target_concepts)
    except (ValueError, FileNotFoundError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2) if args.json else _render(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
