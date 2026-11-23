---
name: reproducibility-and-experiment-tracking
description: 'Use this skill whenever setting up or running any backtest or research experiment, to make sure its exact result can be reproduced later. Also use it when a user can''t reproduce a result they got previously, or asks "why did I get a different number this time running the same thing." This skill exists because a result that can''t be exactly reproduced can''t be fully trusted or properly audited, and the specific causes of irreproducibility in quantitative research (unpinned random seeds, unpinned library versions, unpinned data) are all avoidable with basic discipline established up front.'
---

# Reproducibility and Experiment Tracking

## Why this matters

If re-running the exact same backtest twice produces two different results, something in the process is non-deterministic in a way that isn't understood, and that's a real problem independent of whether either individual result happens to look good. [strategy-research-log-and-versioning](../strategy-research-log-and-versioning/SKILL.md) depends on being able to actually reproduce a logged result to verify what was really tested; without genuine reproducibility, a research log's entries are only as trustworthy as memory of what was run, which defeats much of the point of logging in the first place.

## Do this

### Pin and explicitly set random seeds for any stochastic process, and verify the same seed actually produces the same result

Monte Carlo resampling ([monte-carlo-trade-resampling-and-drawdown-distribution](../monte-carlo-trade-resampling-and-drawdown-distribution/SKILL.md)), any machine-learning component, and any other randomized process needs an explicitly set, logged random seed, and the reproducibility of that seed needs to actually be verified (run it twice, confirm identical output) rather than assumed to work correctly just because a seed was set somewhere in the code.

### Pin exact library and dependency versions, not just major version numbers

A calculation's result can change between minor or patch versions of a numerical library (a bug fix, a default parameter change, a different floating-point handling choice), so pin exact dependency versions (not just "numpy 1.x" but the specific version actually used) for any environment a result needs to be reproducible from, and record that pinned environment alongside the result itself.

### Snapshot or version the exact data used for each experiment, not just a description of the data source

As covered in [strategy-research-log-and-versioning](../strategy-research-log-and-versioning/SKILL.md), data providers can revise historical data, so "used data from provider X for date range Y" isn't sufficient for reproducibility if provider X's data for that range can change over time. Snapshot the actual data used (or record a specific, immutable version/checksum if the provider supports one) alongside the code and configuration that produced a given result.

### Separate configuration from code, and version both explicitly

Strategy parameters, feature definitions, and other configuration should be stored as explicit, versioned configuration (not hardcoded inline in ways that are easy to change without noticing, or left as ambient defaults that silently differ between runs), so that reproducing a result means restoring a specific, identified configuration rather than trying to remember or infer what values were actually used at the time.

### Periodically verify old, previously-generated results are still reproducible from their recorded environment

Environment drift can happen even to a supposedly pinned setup (an operating-system-level dependency changes, a package repository removes an old version), so periodically spot-check that older logged results can still actually be reproduced from their recorded seed, dependency versions, data snapshot, and configuration, rather than assuming a reproducibility setup that worked once will keep working indefinitely without any verification.

## Never do this

- Never leave a stochastic process (resampling, any ML component) with an unset or unlogged random seed, and never assume a seed is working correctly without actually verifying identical output across repeated runs.
- Never record only a library's major version when its exact version can affect a numerical result; pin and record exact versions.
- Never describe the data used for an experiment only by its source and date range without snapshotting the actual data or an immutable version identifier, given that provider data itself can be revised over time.
- Never hardcode configuration inline in a way that makes it easy to change without a record of the change; version configuration explicitly and separately from code.
- Never assume a reproducibility setup that worked once will keep working indefinitely without periodically verifying that older results can still actually be reproduced.

## Verification checklist

- [ ] Every stochastic process has an explicitly set, logged random seed, and reproducibility with that seed has actually been verified by rerunning, not just assumed
- [ ] Exact library and dependency versions (not just major versions) are pinned and recorded alongside each result
- [ ] The actual data used for each experiment is snapshotted or recorded via an immutable version/checksum, not just described by source and date range
- [ ] Configuration is stored and versioned explicitly and separately from code, not hardcoded inline in ways that are easy to change untracked
- [ ] Older logged results are periodically spot-checked to confirm they're still reproducible from their recorded environment
