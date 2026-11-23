---
name: alternative-data-evaluation
description: 'Use this skill before paying for or integrating any alternative data source (sentiment data, options flow, on-chain data, satellite/web-scraped data, or any non-price/volume dataset) into a strategy, and whenever a user is deciding whether a data subscription is actually worth its cost. Also use it when a user asks "does this data actually help" or wants to justify an alternative-data expense. This skill exists because alternative data is expensive and heavily marketed on the promise of edge, but most of it adds cost and complexity without adding real, testable signal, and the burden of proof needs to be on the data before it''s trusted, not after.'
---

# Alternative Data Evaluation

## Why this matters

Alternative data providers have a strong incentive to market their data as edge-generating, and it's easy to convince yourself a new dataset is valuable just because it's expensive, exclusive, or intuitively plausible-sounding. None of that is evidence the data actually improves a strategy's real, out-of-sample performance. Alternative data needs to earn its place in a pipeline the same way any feature does under [feature-and-signal-engineering-discipline](../feature-and-signal-engineering-discipline/SKILL.md), through a specific, tested contribution, not through plausibility or cost alone.

## Do this

### Require a stated hypothesis for why this specific alternative dataset should add signal, before testing it

Consistent with [hypothesis-driven-strategy-design](../hypothesis-driven-strategy-design/SKILL.md), state a specific reason a given alternative dataset should relate to the outcome being predicted, tied to an actual mechanism (options flow data reflecting informed positioning ahead of a move, satellite data revealing real-world activity before it's reflected in reported figures, on-chain data revealing exchange flows relevant to short-term crypto price pressure). A dataset with no stated mechanism connecting it to the outcome is being added on faith, not evidence.

### Test the dataset's marginal contribution against a baseline that doesn't use it, not just its standalone correlation with returns

The relevant question isn't "does this data correlate with returns at all," it's "does adding this data improve performance versus a baseline strategy that doesn't have it," ideally out-of-sample and with the same overfitting safeguards ([overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md), [statistical-significance-and-deflated-metrics](../statistical-significance-and-deflated-metrics/SKILL.md)) applied to any other feature. A dataset that shows a raw correlation with returns but adds nothing once combined with the strategy's existing signals hasn't demonstrated real marginal value, and marginal value is what's actually being paid for.

### Check for point-in-time availability and reporting lag, which is a common lookahead-bias trap specific to alternative data

Many alternative datasets are provided, or backtested against, using a version of the data that wasn't actually available at the historical timestamp being simulated: sentiment scores recalculated with hindsight, on-chain data providers that backfill or revise metrics, satellite-derived estimates refined after the fact. Verify explicitly when each data point in the historical sample would have actually been available in real time, including any reporting lag, and use only that point-in-time-available version in a backtest; this is the same lookahead-bias concern as with restated fundamental data, applied to a less obvious data type.

### Check whether the dataset's history is long enough and stable enough to test properly

Many alternative data products have short histories (a provider that's only existed for two or three years, for instance), which makes it hard to test the data across enough independent market conditions to trust a result, and makes the data especially vulnerable to the same overfitting risk as a strategy tested on too little data relative to its complexity. A short, unstable history is a real constraint on how much confidence any test of the data can produce, regardless of how promising an initial result looks.

### Weigh the data's cost against its measured marginal contribution, not against its narrative appeal

Once a dataset's actual, tested marginal contribution to out-of-sample performance is known, weigh that concretely against its ongoing subscription or acquisition cost. A dataset that adds a small, statistically fragile improvement may not be worth a substantial ongoing cost, however compelling the sales narrative around it sounded before it was actually tested.

## Never do this

- Never add an alternative dataset to a strategy based on a provider's marketing claims or a plausible-sounding narrative without a stated mechanism and an actual out-of-sample test of marginal contribution.
- Never evaluate a dataset only by its standalone correlation with returns; test its marginal contribution over a baseline that doesn't include it.
- Never backtest with a version of alternative data that wasn't actually available at the historical timestamp being simulated; check for reporting lag and revisions explicitly.
- Never treat a short-history alternative dataset's promising initial result with the same confidence as a result tested over a long, stable history.
- Never keep paying for a data subscription whose actual, tested marginal contribution hasn't been reassessed against its ongoing cost.

## Verification checklist

- [ ] A specific, mechanism-based hypothesis exists for why this alternative dataset should relate to the target outcome, not just a plausible-sounding narrative
- [ ] The dataset's marginal contribution was tested against a baseline that doesn't include it, with the same overfitting safeguards applied as any other feature, not just checked for standalone correlation
- [ ] Point-in-time availability and reporting lag were verified, and only data that would have actually been available at each historical timestamp was used in backtesting
- [ ] The dataset's available history was checked for length and stability before drawing strong conclusions from a test of it
- [ ] The dataset's ongoing cost is being weighed against its actual measured marginal contribution, not its narrative appeal, and is periodically reassessed
