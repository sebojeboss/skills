---
name: backtesting-engine-selection-and-known-bugs
description: 'Use this skill when choosing a backtesting framework or library for a new strategy, and when reviewing an existing backtest for engine-level bugs rather than strategy-level ones. Also use it when a user asks "which backtesting library should I use" or has a suspiciously good result that might be explained by how the engine itself handles fills, timing, or bar construction rather than by the strategy''s actual rules. This skill exists because the backtesting engine itself is software with its own bugs and design choices, and a well-designed strategy run through an engine with a same-bar-fill bug or a subtle lookahead in its bar construction will still produce a wrong, inflated result.'
---

# Backtesting Engine Selection and Known Bugs

## Why this matters

Every other skill in this repo assumes the backtest itself is correctly simulating what a strategy's rules actually produce. That assumption isn't automatic; backtesting engines, whether a popular open-source library or custom-built code, have their own design choices and their own bugs, and some of the most common ones (same-bar-fill assumptions, vectorized-engine lookahead, incorrect handling of corporate actions or overnight gaps) inflate backtest results in ways that look exactly like a real strategy edge until specifically checked for.

## Do this

### Understand whether an engine is vectorized or event-driven, and know each type's characteristic failure mode

Vectorized backtesting engines (computing signals and returns via array operations across the whole dataset at once) are fast but structurally prone to introducing lookahead bias if signal computation isn't carefully bounded to only use past data at each point; event-driven engines (processing one time step/event at a time, more closely mimicking how a live system actually operates) are typically slower but structurally less prone to this specific failure since they can only see data up to the current simulated point in time by construction. Know which type is being used and apply the correspondingly appropriate scrutiny: vectorized engines need explicit, deliberate verification that no computation leaks future data backward.

### Check specifically for same-bar-fill assumptions, a common and easy-to-miss engine default

Many simple backtesting setups assume a signal generated from a bar's data can be filled at that same bar's price (often its close), which implicitly assumes the fill happens at exactly the moment the bar's final price became known, with zero delay. Check explicitly whether the engine being used makes this assumption, and if so, whether it's appropriate for the strategy (a strategy that only acts on fully-confirmed end-of-day data with a next-bar-open fill assumption is different from one implicitly assuming a same-bar close fill), consistent with the timing concerns in [transaction-cost-and-market-impact-modeling](../transaction-cost-and-market-impact-modeling/SKILL.md).

### Verify how the engine handles overnight gaps, halts, and other discontinuities, especially for stop-loss and limit order logic

A backtesting engine's assumption about what happens when price gaps past a stop-loss or limit level overnight or during a halt (does it fill at the stop price, at the actual opening price after the gap, or does it mishandle the situation entirely) has a real impact on backtested risk-management performance, and getting this wrong specifically understates risk in exactly the scenarios where realistic risk management matters most. Test the engine's gap-handling behavior directly against a known historical gap event rather than assuming it's handled correctly.

### Cross-validate a new or unfamiliar engine's output against an independent implementation for at least one simple, known case

Before trusting a new backtesting engine (or a significant version upgrade of an existing one) for real strategy research, run at least one simple strategy with a hand-computable expected result through it and verify the engine's output actually matches the hand calculation. This catches configuration errors, unexpected default behaviors, or genuine engine bugs before they've shaped a real strategy's validation results.

### Read the engine's documentation and changelog for known issues and recent bug fixes relevant to the strategy's actual logic

Backtesting libraries have documented (and sometimes undocumented, only-discussed-in-issue-trackers) known bugs and limitations; checking whether any known issues are relevant to the specific order types, instruments, or logic a strategy actually uses is a cheap check that can surface a real, already-known problem before it's discovered independently and much more expensively.

## Never do this

- Never use a vectorized backtesting engine without explicitly verifying that signal computation is bounded to only use data available at each point in time; vectorized engines are structurally prone to accidental lookahead in ways event-driven engines are not.
- Never assume an engine's fill-timing default (same-bar close, next-bar open, or otherwise) is appropriate for a given strategy without checking what it actually is and whether it matches the strategy's real execution timing.
- Never assume an engine correctly handles overnight gaps, halts, or other price discontinuities for stop-loss and limit order logic without testing it against a known historical gap event.
- Never trust a new or unfamiliar backtesting engine's output for real strategy research without first cross-validating it against an independent, hand-computable result for at least one simple case.
- Never skip checking a backtesting library's documentation and issue tracker for known bugs relevant to the specific logic a strategy actually uses.

## Verification checklist

- [ ] The backtesting engine's type (vectorized or event-driven) is known, and vectorized engines have been explicitly checked for lookahead in signal computation
- [ ] The engine's fill-timing assumption (same-bar, next-bar, or other) is known and matches the strategy's intended real-world execution timing
- [ ] The engine's handling of overnight gaps, halts, and other discontinuities for stop-loss/limit logic has been tested against a known historical gap event
- [ ] A new or unfamiliar engine's output has been cross-validated against an independent, hand-computable result for at least one simple case before being trusted for real research
- [ ] The engine's documentation and known-issues history have been checked for anything relevant to the specific order types, instruments, or logic actually being used
