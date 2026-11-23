---
name: hypothesis-driven-strategy-design
description: 'Use this skill at the very start of any trading strategy build, before writing any backtest or optimization code, and especially whenever a user''s request amounts to "find me a profitable strategy" without specifying what market behavior it should actually be exploiting. Also use it when reviewing an existing strategy that has no stated rationale beyond its backtest results. This skill exists because searching for whatever pattern happens to backtest well is the single most direct route to overfitting there is; a strategy needs a reason to exist before it needs a backtest.'
---

# Hypothesis-Driven Strategy Design

## Why this matters

"Find a profitable strategy" is not a research question, it's an invitation to data-dredge. Given enough parameter combinations and indicator choices, a search process will always find something that looks profitable on historical data, because historical data contains noise, and noise can always be fit given enough freedom to search. The fact that a pattern was found says almost nothing about whether it reflects a real, persistent market behavior versus a coincidence in one specific historical sample.

A strategy that starts from a stated hypothesis, an actual theory about why a specific market behavior exists and why it should be expected to persist, is a fundamentally different research process than searching for whatever fits. The hypothesis constrains the search before the data is ever touched, which is the only point at which that constraint actually does any good.

## Do this

### Write the hypothesis down before writing any backtest code

State, in plain language, what specific market behavior the strategy is trying to capture, before any code runs. A real hypothesis names a mechanism: a specific behavioral bias, a structural friction, a flow-driven effect, or a risk premium, not just a pattern ("price tends to go up after it goes up" is an observation, not a hypothesis; "trend-followers as a group tend to be underweight after a sharp move because they're waiting for a pullback that often doesn't come, creating persistent one-directional flow" is a hypothesis with an actual mechanism attached).

### Require an answer to "who is on the other side of this trade, and why does this opportunity persist"

Every real trading edge exists because some other market participant is systematically willing to trade at a worse price, for a real reason: they're hedging, they're liquidity-constrained, they're subject to a behavioral bias, they're mechanically forced to trade regardless of price (index rebalancing, options expiry pinning, month-end flows), or the opportunity is too small or too illiquid for larger, better-capitalized participants to compete it away. If there's no plausible answer to who's persistently on the other side and why they keep doing it, that's a strong signal the "edge" is actually just noise the search process found and rationalized after the fact.

### Distinguish exploratory research from confirmatory validation, and don't let exploration bleed into validation

It's fine, even necessary, to explore data and iterate on an idea before it's fully formed. But once a hypothesis and its parameters are set for validation, that validation needs to run on data and in a process that isn't further adjusted based on the result. Continuing to tweak the hypothesis, the entry rule, or the parameters after seeing out-of-sample or validation results defeats the entire purpose of holding out that data in the first place; at that point it's not confirmatory validation anymore, it's just more exploration wearing a validation costume. Decide explicitly when exploration ends and pre-specify what will be tested before looking at the held-out result.

### Ground every parameter choice in the theory, not in whichever value backtests best

If the hypothesis involves monthly institutional rebalancing flows, a 20-day lookback has a reason to exist that a data-fit 23-day lookback picked because it scored 0.1 Sharpe higher does not. Parameter values chosen because they match the actual real-world timescale or mechanism the hypothesis describes are far more likely to generalize than values chosen purely because they optimized a backtest metric; the latter is functionally indistinguishable from fitting to noise even when the underlying theory is directionally sound.

### Check that the strategy's actual behavior matches what the theory would predict

A theory about a slow, structural, monthly-timescale effect should produce a strategy with a holding period and trade frequency on that same timescale; if the "monthly rebalancing" hypothesis somehow produced a strategy that enters and exits positions every few minutes, something has drifted between the stated theory and the actual implementation, and that gap needs to be resolved, not ignored because the fast version happened to backtest better. The instrument, timeframe, and frequency the strategy actually trades should be a direct, checkable consequence of the mechanism the hypothesis describes.

### Write down why the edge should keep working, not just why it worked historically

A credible hypothesis includes a reason the opportunity isn't already competed away and isn't likely to disappear immediately: a capacity constraint that keeps larger players out, a behavioral bias that's persistent across market cycles rather than specific to one historical period, or a structural feature of market plumbing that isn't about to change. "It worked for the last five years" is not that reason; markets that used to have real edges have had them arbitraged away before, and a strategy needs a story for why this one is different.

## Never do this

- Never start a strategy search from "find something profitable" without first requiring a stated hypothesis about what specific behavior is being exploited.
- Never treat a backtested pattern as evidence of a real edge without a plausible answer for who's persistently on the other side of the trade and why.
- Never keep adjusting the hypothesis, entry rules, or parameters after seeing out-of-sample or held-out validation results; that collapses the exploratory/confirmatory boundary that makes validation meaningful.
- Never choose a parameter value purely because it optimizes a backtest metric when the underlying theory implies a different, specific value.
- Never let a strategy's actual trading frequency, holding period, or instrument choice drift away from what its stated theory would predict without treating that mismatch as a problem to resolve.
- Never accept "it worked historically" as a sufficient reason to expect an edge to keep working; require a reason the opportunity persists.

## Verification checklist

- [ ] A specific hypothesis is written down, naming an actual mechanism (behavioral, structural, flow-driven, risk-premium), not just a described pattern
- [ ] There's a plausible, specific answer to who is persistently on the other side of this trade and why they keep taking the worse side of it
- [ ] The boundary between exploratory research and confirmatory validation was decided in advance, and no further hypothesis or parameter changes were made after seeing validation/out-of-sample results
- [ ] Parameter values are justified by the theory's actual real-world timescale or mechanism, not chosen because they scored best in a backtest
- [ ] The strategy's actual trading frequency, holding period, and instrument choice are consistent with what the stated hypothesis would predict
- [ ] There's a stated reason the edge should be expected to persist going forward (capacity constraint, durable behavioral bias, structural friction), not just historical performance
