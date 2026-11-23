"""Tests for the creative diversity scorer. Run: python -m pytest -q"""
import score as s


def rows(concepts, fmt="video"):
    return [{"concept": c, "format": fmt, "angle": ""} for c in concepts]


def test_distinct_concepts_counted_not_rows():
    r = s.score(rows(["a", "a", "a", "b", "b"]))
    assert r["total_creatives"] == 5
    assert r["distinct_concepts"] == 2


def test_variation_ratio():
    r = s.score(rows(["a", "a", "a", "a", "b", "b"]))  # 6 rows, 2 concepts
    assert r["variation_ratio"] == 3.0
    assert any("VARIATION-HEAVY" in f for f in r["flags"])


def test_under_diverse_flag():
    r = s.score(rows(["a", "b", "c"]), target_concepts=12)
    assert any("UNDER-DIVERSE" in f for f in r["flags"])


def test_full_diversity_scores_high():
    concepts = [f"c{i}" for i in range(12)]
    data = (
        [{"concept": c, "format": "video", "angle": ""} for c in concepts]
        + [{"concept": c, "format": "static", "angle": ""} for c in concepts[:6]]
        + [{"concept": c, "format": "carousel", "angle": ""} for c in concepts[:6]]
    )
    r = s.score(data, target_concepts=12)
    assert r["diversity_score"] == 100
    assert r["distinct_formats"] == 3


def test_single_format_flag():
    r = s.score(rows([f"c{i}" for i in range(12)], fmt="video"))
    assert any("SINGLE-FORMAT" in f for f in r["flags"])


def test_score_is_bounded():
    r = s.score(rows([f"c{i}" for i in range(100)]))
    assert 0 <= r["diversity_score"] <= 100
