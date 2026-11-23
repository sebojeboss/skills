---
name: creative-diversity-scorer
description: Scores whether an ad account has enough genuinely distinct creative concepts for modern creative-led delivery (Meta Andromeda, Advantage+, and creative-diversity-as-targeting generally), counting distinct concepts rather than ad rows and flagging the Entity-ID trap where variations of one concept count as one. Use whenever the user asks how many creatives or concepts they need, why creative isn't scaling, whether their testing is diverse enough, or shares a list of ads/creatives. Also use proactively before launching or scaling a creative-led campaign.
license: MIT
metadata:
  version: 1.0.0
  category: creative
  channels: [meta, tiktok, google-ads]
  inputs: [creatives CSV with a concept column and optional format/angle columns]
  outputs: [distinct concept count, format/angle coverage, variations-per-concept ratio, 0-100 diversity score, gap flags]
  playbooks: [demand-gen-prospecting-for-dtc]
---

# Creative Diversity Scorer

## When to use
Deciding whether you have enough distinct creative to feed a creative-led engine, or diagnosing
why creative isn't scaling. NOT for ranking creative performance (see `asset-performance-ranker`)
or hook analysis (see `hook-rate-analyzer`).

## Required inputs — refuse to proceed without them
1. A **creatives CSV** with, at minimum, a **concept** column (concept / theme / idea) so distinct
   ideas can be counted — not just ad IDs.
2. Ideally **format** and **angle** columns too, for coverage scoring.
If concepts aren't labeled, ask the user to label them; do not guess concepts from filenames.

## Method
1. Count **distinct concepts** (deduped), not ad rows — this is the number modern delivery engines
   effectively "see."
2. Compute **variations-per-concept** = rows ÷ distinct concepts. A high ratio means a big ad count
   is hiding a small idea count (the Entity-ID trap).
3. Score coverage across **formats** and **angles**.
4. Emit a **0–100 diversity score** (concept count vs target + format coverage) and gap flags.
5. Run it:
   ```bash
   python scripts/score.py --csv creatives.csv --target-concepts 12
   ```
   Use `--concept-col/--format-col/--angle-col` to map columns, `--json` for machine output.

## Guardrails
- **Recommendations only** — it never edits campaigns or creative.
- **Concepts must be labeled by a human.** The tool counts labels; it does not judge whether two
  ads are "really" the same concept — that's the operator's call.
- A high score means diverse *inputs*, not guaranteed performance; pair with performance data.

## References
- `references/entity-id-trap.md` — what counts as one concept, and why.
