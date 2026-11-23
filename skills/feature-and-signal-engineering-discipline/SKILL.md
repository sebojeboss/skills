---
name: feature-and-signal-engineering-discipline
description: 'Use this skill whenever building, adding to, or reviewing the set of indicators, features, or signals a trading strategy uses, especially whenever the approach involves computing many indicators and letting an optimizer or model select among them. Also use it when a user asks to "add more indicators," "throw in some more features," or otherwise wants to expand a signal set without a stated reason tied to the strategy''s hypothesis. This skill exists because indiscriminate feature/indicator proliferation is one of the most common and least obvious ways a strategy becomes overfit, since each added feature is an added degree of freedom the optimizer can use to fit noise, even when no single feature looks unreasonable on its own.'
---

# Feature and Signal Engineering Discipline

## Why this matters

Every feature or indicator added to a strategy is a new degree of freedom available to whatever process selects among or weights them, and degrees of freedom are exactly what [overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md) warns about: more of them, relative to the amount of independent data available, means more capacity to fit the noise in a specific historical sample rather than a real signal. A pile of twenty plausible-sounding technical indicators, fed into an optimizer that picks the best-performing combination, will reliably produce something that looks great in-sample and means very little, even though no individual indicator in the pile looks unreasonable.

## Do this

### Derive every feature from the strategy's stated hypothesis, not from a general list of popular indicators

If [hypothesis-driven-strategy-design](../hypothesis-driven-strategy-design/SKILL.md) named a specific mechanism, the features used to detect or trade that mechanism should be a direct, explicable consequence of it. A hypothesis about monthly institutional rebalancing flows implies specific features (day-of-month effects, flow-proxy measures), not an unrelated grab-bag of RSI, MACD, Bollinger Bands, and a dozen other indicators added because they're commonly used. Each feature should have a one-sentence answer to "why does this specific feature relate to the stated mechanism," and a feature that doesn't have one is a candidate for removal, not inclusion.

### Prefer fewer, well-motivated features over many marginally-justified ones

A smaller feature set that's harder to overfit and easier to reason about is almost always preferable to a larger one that scores slightly better in-sample. When genuinely unsure whether a feature adds value, the default should be to leave it out and test its addition as its own explicit, logged experiment (see the research-log skill for why this matters), not to include it "just in case" alongside everything else.

### Check feature stability across time and regimes before relying on it

A feature whose relationship to the target outcome is stable across different time periods and market regimes is far more likely to reflect something real than one that only worked in a specific historical window. Explicitly check this (split the data into multiple periods and verify the feature's relationship to outcomes holds up in each) rather than assuming a feature that worked well over the full sample worked consistently throughout it; a feature that only worked during one specific regime is a narrower, more fragile finding than it looks from full-sample statistics alone.

### Check for redundancy and multicollinearity, which inflate effective parameter count without adding real information

Several highly correlated features (multiple moving-average-based indicators computed over similar lookback windows, for instance) can add much more effective fitting freedom than their apparent count suggests, since the optimizer has many near-equivalent ways to express essentially the same underlying signal, each one a further opportunity to fit noise in the specific correlations of the historical sample. Check correlation between candidate features and consolidate or remove redundant ones rather than treating "more features" as automatically safe just because each one is individually simple.

### Compute any normalization or scaling using only information available at that point in time

Z-scoring, min-max scaling, or any other normalization computed using full-sample statistics (the mean or standard deviation across the entire dataset, including future data relative to any given historical point) leaks future information backward into the past, which is a direct form of the lookahead bias [overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md) warns about, and a very easy one to introduce by accident through a single careless normalization step. Compute any such statistics using only data available up to that point (a rolling or expanding window), never the full sample.

### Document why each feature was included, so the set can be audited later

A feature list with a one-line rationale for each entry, tied back to the hypothesis, makes it possible to later ask "does this still make sense" and to catch feature creep before it accumulates into an unreviewable pile. A feature list with no documented rationale is much harder to prune, because removing anything starts to feel risky without a record of why it was there in the first place.

## Never do this

- Never add a feature or indicator to a strategy purely because it improved a backtest metric, without a theoretical reason tied to the strategy's stated hypothesis.
- Never treat "it's a popular/standard indicator" as sufficient justification for including it in a specific strategy that has no stated mechanism connecting it to that indicator.
- Never compute a normalization or scaling statistic using full-sample data when the strategy trades sequentially through time; use only data available up to each point.
- Never assume a large set of individually-simple features is safe from overfitting just because no single feature looks complex; check for redundancy and multicollinearity, which inflate effective degrees of freedom in ways that aren't obvious from the feature count alone.
- Never keep a feature in the active set with no documented rationale for why it's there.
- Never let a feature set expand without each addition tracing back to the strategy's stated hypothesis and being logged as an explicit, individually-evaluated experiment.

## Verification checklist

- [ ] Every feature in the strategy has a documented, one-sentence rationale tying it to the stated hypothesis, not just "it's a common indicator"
- [ ] The feature set was kept as small as could be justified, with additions treated as individually logged experiments rather than added freely
- [ ] Each feature's relationship to the target outcome was checked for stability across multiple time periods/regimes, not just measured once over the full sample
- [ ] Candidate features were checked for correlation/redundancy with each other, and redundant ones were consolidated or removed
- [ ] Any normalization or scaling was computed using only information available at each point in time, never full-sample statistics
