---
name: portfolio-construction-and-correlation-checks
description: 'Use this skill whenever combining more than one strategy or position into a portfolio, and whenever a user believes they''ve diversified by running multiple strategies without having checked the actual correlation between them. Also use it when a user asks "how many strategies do I need" or wants to know if adding a new strategy actually reduces portfolio risk. This skill exists because running multiple strategies feels like diversification, but strategies that look different on the surface (different indicators, different instruments, different rules) frequently share the same underlying risk factor and move together exactly when it matters most, during real stress.'
---

# Portfolio Construction and Correlation Checks

## Why this matters

Running five strategies feels safer than running one, but that feeling is only justified if those five strategies actually behave differently from each other, especially during the market conditions where risk concentration matters most. Two strategies that look completely different, different instruments, different indicators, different holding periods, can still both be, structurally, "buy the same underlying risk factor" bets that will lose money at the same time in a real drawdown, and a portfolio built without checking for this can carry far more concentrated risk than the number of strategies in it would suggest.

## Do this

### Compute actual correlation between strategies' returns, not just their apparent rule differences

Two strategies with completely different entry rules, indicators, and instruments can still have highly correlated returns if they're both, underneath the specific mechanics, exposed to the same broader risk factor (both effectively long equity market beta, both effectively short volatility, both exposed to the same macro regime). Compute the actual historical correlation of strategy-level returns directly, and treat a high correlation as evidence of shared underlying risk regardless of how different the strategies' rules look on paper.

### Check correlation specifically during stress periods, not just over the full sample average

Correlations between strategies (and between assets generally) are well known to rise during market stress, sometimes sharply, even when they look comfortably low during calm periods. A full-sample average correlation can look reassuringly low while masking a much higher correlation specifically during the drawdown periods that matter most for portfolio risk. Explicitly compute correlation conditional on stress periods (using the strategies' own drawdown periods, or broader market stress periods) in addition to the full-sample average.

### Identify the actual underlying risk factors each strategy is exposed to, not just the pairwise return correlation

Pairwise correlation is a useful summary statistic, but understanding what each strategy is actually exposed to (equity beta, a specific commodity, a currency, a volatility regime, a sector) gives a more durable picture of diversification than correlation alone, since two strategies could have a moderate historical correlation purely by coincidence while genuinely sharing (or not sharing) a real underlying factor exposure that correlation alone won't reliably reveal in a limited sample.

### Size portfolio-level risk from the actual correlation structure, not from naive per-strategy risk summed independently

As covered in [position-sizing-and-risk-management](../position-sizing-and-risk-management/SKILL.md), a portfolio's real aggregate risk depends on the correlation between its components, not just the sum of their individual risk contributions. Compute portfolio-level risk (value-at-risk, expected drawdown, or a similar aggregate measure) using the actual measured correlation structure, and recognize that naively summing independent per-strategy risk limits will understate real portfolio risk whenever correlations are positive, which they usually are during exactly the periods that matter.

### Re-evaluate correlation periodically, since it changes as strategies, markets, and regimes evolve

The correlation structure measured when a portfolio was built doesn't necessarily hold indefinitely, since strategies can drift, market regimes change, and previously uncorrelated risk factors can become correlated as the environment shifts (as they notably tend to during systemic stress events). Re-check correlation periodically rather than treating an initial diversification analysis as a permanent property of the portfolio.

## Never do this

- Never assume running multiple strategies constitutes real diversification without computing their actual return correlation.
- Never rely only on full-sample average correlation; explicitly check correlation conditional on stress/drawdown periods, since it commonly rises exactly when it matters most.
- Never treat pairwise return correlation as the complete picture of shared risk; also consider each strategy's actual underlying factor exposures.
- Never compute portfolio-level risk limits by simply summing independently-set per-strategy risk limits without accounting for the actual correlation structure between them.
- Never treat a portfolio's correlation structure as permanent; re-evaluate it periodically as strategies and market regimes evolve.

## Verification checklist

- [ ] Actual historical return correlation between strategies has been computed directly, not assumed low based on differing rules or instruments
- [ ] Correlation has been checked specifically during stress/drawdown periods, not only as a full-sample average
- [ ] Each strategy's underlying risk factor exposures have been considered as a complement to pairwise correlation, not as a substitute for it or ignored entirely
- [ ] Portfolio-level risk is computed from the actual measured correlation structure, not from naively summed independent per-strategy risk limits
- [ ] Correlation and factor exposure are periodically re-evaluated rather than treated as a fixed, one-time analysis
