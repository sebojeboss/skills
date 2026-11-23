---
name: regime-detection-and-adaptation
description: 'Use this skill when a strategy has been trading live for a while and its performance seems to be drifting, or when designing how a strategy should respond to a market regime shift rather than mechanically continuing to apply the same rules regardless of conditions. Also use it when a user asks "how do I know the market has changed" or "should my strategy behave differently in this environment." This skill exists because a strategy validated across historical regimes can still eventually face a regime genuinely outside anything in its validation history, and the right response depends on actually recognizing that shift, not on mechanically continuing to apply rules that were built for different conditions.'
---

# Regime Detection and Adaptation

## Why this matters

[overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md) recommends testing across multiple historical regimes, but a strategy will eventually face live market conditions that don't closely resemble anything in its validation history, since markets do periodically produce genuinely new regimes. A strategy with no mechanism for recognizing when conditions have shifted meaningfully will just keep mechanically applying rules built for the regimes it was actually tested on, which can range from harmless to seriously costly depending on how different the new regime actually is and how the strategy's specific rules interact with it.

## Do this

### Define specific, measurable indicators of regime, not a vague sense that "things feel different"

Build concrete, measurable regime indicators relevant to the strategy's actual edge category ([edge-taxonomy-and-strategy-classification](../edge-taxonomy-and-strategy-classification/SKILL.md)): realized volatility relative to its own historical range, trend strength/persistence measures, correlation structure between relevant instruments, liquidity/spread conditions. A regime shift should be something the system can actually measure and flag, not something that only gets noticed after performance has already visibly suffered.

### Tie regime detection to the strategy's actual stated hypothesis, not a generic market-wide indicator unrelated to its edge

A regime shift that matters for a given strategy is specifically a shift in the conditions its hypothesis actually depends on; a trend-following strategy cares about trend persistence and whipsaw conditions, a carry strategy cares about risk-off/unwind conditions, a stat-arb strategy cares about the stability of the specific relationships it trades. Detecting a generic, broad market regime shift that has nothing to do with the specific mechanism the strategy is built around isn't actually useful; tie regime detection directly back to what the strategy's hypothesis says it depends on.

### Decide in advance what specific adaptation happens when a regime shift is detected, not react improvised in the moment

Predefine what the strategy should actually do when its regime indicators cross a defined threshold: reduce position size, pause trading entirely, switch to a different parameter set validated for that regime if one exists, or simply flag for human review. An improvised, in-the-moment reaction to a detected regime shift is subject to the same discretionary-decision-under-stress problem [position-sizing-and-risk-management](../position-sizing-and-risk-management/SKILL.md) warns about for drawdown de-risking.

### Distinguish a real regime shift from ordinary noise in the regime indicator itself

Regime indicators are themselves noisy measurements, and treating every fluctuation in a volatility or correlation measure as a "regime shift" produces a system that overreacts to normal variation. Set thresholds for regime-shift detection that are calibrated against the indicator's own normal historical variability (similar in spirit to the resampled-distribution approach in [monte-carlo-trade-resampling-and-drawdown-distribution](../monte-carlo-trade-resampling-and-drawdown-distribution/SKILL.md)), so the system reacts to genuinely unusual conditions rather than ordinary noise.

### Recognize that a strategy's own validation history doesn't cover every possible future regime, and build in a "genuinely unknown" response

Even a well-designed regime detector can flag a state of the world that simply wasn't in the strategy's validation history at all, rather than matching one of the regimes it was specifically tested against. Have an explicit, conservative default response for this case (reduce exposure and flag for review, rather than assuming the strategy's normal rules still apply) instead of implicitly treating "not clearly one of my known bad regimes" as equivalent to "this is fine."

## Never do this

- Never rely on a vague, undefined sense that market conditions "feel different" instead of concrete, measurable regime indicators.
- Never build regime detection around a generic market-wide indicator that has no specific connection to the strategy's actual stated hypothesis and edge category.
- Never leave the response to a detected regime shift to be improvised in the moment; decide the adaptation (size reduction, pause, parameter switch, human review) in advance.
- Never set regime-shift detection thresholds without calibrating them against the indicator's own normal historical noise, or every fluctuation will trigger an unnecessary reaction.
- Never assume a strategy's normal rules should keep applying by default when conditions clearly fall outside anything in its validation history; build an explicit conservative default for genuinely unrecognized regimes.

## Verification checklist

- [ ] Regime is tracked via concrete, measurable indicators, not a subjective impression of changed conditions
- [ ] Regime indicators are specifically tied to what the strategy's stated hypothesis actually depends on, not a generic, unrelated market-wide measure
- [ ] The specific adaptation triggered by a detected regime shift (size reduction, pause, parameter switch, human review) was decided in advance, not improvised
- [ ] Regime-shift detection thresholds are calibrated against the indicator's own normal historical variability, to avoid overreacting to ordinary noise
- [ ] An explicit, conservative default response exists for market conditions that fall outside anything in the strategy's validation history, rather than assuming normal rules apply by default
