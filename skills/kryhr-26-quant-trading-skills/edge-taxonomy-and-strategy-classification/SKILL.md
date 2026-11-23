---
name: edge-taxonomy-and-strategy-classification
description: 'Use this skill right after a strategy''s hypothesis is stated (see hypothesis-driven-strategy-design), and whenever evaluating whether a strategy''s backtest metrics, trade frequency, or capacity look reasonable for what it actually is. Also use it when a user asks "is this Sharpe good" or "does this look right" without having first classified what kind of edge the strategy is claiming to capture. This skill exists because different edge types have genuinely different normal ranges for every metric that matters, and judging a mean-reversion strategy by trend-following norms, or vice versa, produces wrong conclusions in both directions.'
---

# Edge Taxonomy and Strategy Classification

## Why this matters

"Is a Sharpe of 2.5 good" doesn't have a single answer; it depends enormously on what kind of strategy produced it. A market-making strategy running at high frequency with tight risk control can sustain a very different Sharpe and drawdown profile than a slow trend-following system, and neither should be judged against the other's norms. Classifying a strategy into a real category before evaluating it is what makes the evaluation meaningful; without it, [overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md)'s red-flag ranges are being applied blind to what's actually being tested.

## Do this

### Classify the strategy into an actual edge category before evaluating its metrics

See [references/edge-taxonomy.md](references/edge-taxonomy.md) for the full breakdown, but the major categories are: momentum/trend-following, mean-reversion, carry, statistical arbitrage/relative value, market-making/liquidity provision, event-driven, and volatility risk premium. Each has a different typical holding period, typical capacity ceiling, typical drawdown shape, and typical failure mode. A strategy should be classified into one of these (or an explicit hybrid, stated as such) before its metrics get evaluated against any benchmark.

### Calibrate expected metrics and validation approach to the category, not to a single universal standard

A statistical arbitrage strategy trading many small, largely uncorrelated positions can sustain a smoother equity curve and higher Sharpe than a directional trend-following strategy, which by nature has long stretches of chop between trending regimes, without that difference implying the stat-arb strategy is more overfit. Conversely, an unusually smooth equity curve from a trend-following strategy, which should structurally have real losing streaks during choppy regimes, is more suspicious than the same smoothness from a genuinely diversified stat-arb book. Read [overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md)'s thresholds through the lens of what category is actually being tested.

### Check the strategy's capacity constraint against its claimed category

Every edge category has a different relationship between opportunity size and capital capacity. Market-making and short-horizon statistical arbitrage typically have real capacity limits, the edge degrades as more capital chases it; slower macro or trend-following strategies typically have far more room. If a strategy is claimed to be in a low-capacity category (tight stat-arb, market-making) but is being sized as if it has unlimited capacity, or vice versa, that's a mismatch worth resolving explicitly before relying on backtested performance at a different size than was actually tested.

### Match the failure mode being checked for to the category

Each category tends to fail in a specific, recognizable way: trend-following strategies fail in extended choppy, range-bound regimes (whipsaw); mean-reversion strategies fail when a genuine regime break turns a temporary dislocation into a permanent one (catching a falling knife); carry strategies fail in sudden risk-off unwinds (the classic "picking up pennies in front of a steamroller" pattern); market-making strategies fail when adverse selection spikes faster than spread capture can compensate for it; event-driven strategies fail when the assumed event outcome distribution shifts. Check for the specific failure mode that actually applies to the category in question, not a generic list.

## Never do this

- Never evaluate a strategy's Sharpe ratio, drawdown profile, or equity curve smoothness against a single universal standard without first classifying what edge category it belongs to.
- Never treat an unusually smooth equity curve as equally suspicious across all categories; the baseline expectation for smoothness genuinely differs by category, and this needs to inform (not excuse) how strictly [overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md) gets applied.
- Never size or deploy a strategy as if it has different capacity characteristics than its actual category implies without an explicit, checked reason.
- Never check a strategy for a generic list of failure modes instead of the specific ones its edge category is actually prone to.
- Never assume classifying a strategy into a legitimate, real edge category is itself evidence the strategy has real edge; the category describes a plausible mechanism, it doesn't verify this specific implementation actually captures it.

## Verification checklist

- [ ] The strategy is classified into a specific edge category (or an explicitly stated hybrid), not left unclassified
- [ ] Expected Sharpe, drawdown shape, and equity curve smoothness are being judged against norms appropriate to that category, not a single universal standard
- [ ] The strategy's claimed or assumed capacity is consistent with what its category typically supports
- [ ] The strategy has been checked against the specific failure mode(s) its edge category is actually prone to
- [ ] Classification into a real category is treated as context for evaluation, not as evidence the specific strategy has real edge

See [references/edge-taxonomy.md](references/edge-taxonomy.md) for the full breakdown of each category's typical characteristics, capacity, and failure modes.
