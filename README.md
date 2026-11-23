# skills

A personal collection of agent skills (`SKILL.md` folders), split into branches so each stays under 1,000 skills.
Import a branch URL, e.g. `https://github.com/sebojeboss/skills/tree/skills-lovable`.

| Branch | Skills | Focus |
|---|---|---|
| `skills-extra-all` | 1,000 | Skills from the skills.sh leaderboards (all-time, trending, hot) |
| `skills-lovable` | 92 | Lovable app building (prompting, Supabase, SEO, payments, i18n) |
| `skills-design-security` | 253 | Anti-slop design, UI/UX, accessibility, defensive web security |
| `skills-design-security-2` | 503 | Design taste, landing pages, privacy/GDPR, vibe-coding security |
| `skills-web-build` | 156 | Motion, technical SEO, forms, e-commerce/checkout, QA, responsive design |
| `skills-business` | 886 | Dropshipping/DTC e-commerce, Shopify CRO, Meta/TikTok ads and UGC creatives, research, unit economics, trading/backtesting, voice |

Every skill name is unique across all branches except where noted in the original sources.

## Install as a plugin marketplace (recommended)
This repo is a Claude plugin marketplace. In Claude (Plugins -> Add marketplace) or in Claude Code:
```
/plugin marketplace add sebojeboss/skills
/plugin install lovable@sebojeboss-skills
```
Plugins (install only what you need): `ecom-business` (886), `lovable` (92), `design-security` (253),
`design-taste-privacy` (503), `web-build` (156), `skills-leaderboard` (1,000).
Each plugin lives on its own `plugin-*` branch with a flat `skills/<name>/SKILL.md` layout.

## Alternative: import skills directly
(Quick start: what to import)
Import these three (each is under the 1,000-skill limit, names are unique across them):

| Import URL | Skills | Contents |
|---|---|---|
| `https://github.com/sebojeboss/skills/tree/skills-core` | 978 | Business (e-commerce, ads/creatives, research, unit economics, trading, voice) + Lovable |
| `https://github.com/sebojeboss/skills/tree/skills-design-all` | 912 | Design, anti-slop, UI/UX, accessibility, SEO, forms, motion, defensive security, privacy |
| `https://github.com/sebojeboss/skills/tree/skills-extra-all` | 1,000 | skills.sh leaderboards |

The individual branches below are the same content split by topic.

## "Check skills before every task" rule
`CLAUDE.md` in this repo holds a global rule. Install it for every project on a machine:
```bash
mkdir -p ~/.claude && curl -fsSL https://raw.githubusercontent.com/sebojeboss/skills/main/CLAUDE.md >> ~/.claude/CLAUDE.md
```

## Lovable-ready archives (valid names/YAML, no name clashes with Lovable built-ins)
Lovable accepts one skill per import and limits files per skill. The 503 skills of `skills-design-security-2`
were fixed (lowercase names, valid YAML, folder = name, `bb-` prefix for the brand-building pack) and split into
branches `lovable-ds2-part-1`, `lovable-ds2-part-2`, `lovable-ds2-part-3` (163 / 169 / 170 skills).
The one oversized skill (`taste-skill`, 1,630 files) is excluded from these branches.

## Notice
Most skills are third-party content, copied from their original public repositories. Each skill folder keeps its
original files. Licenses and copyright stay with the original authors; check the source repository before reuse
or redistribution. Skills are instructions that agents can act on: read a skill before using it.
