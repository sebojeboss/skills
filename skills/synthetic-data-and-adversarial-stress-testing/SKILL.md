---
name: synthetic-data-and-adversarial-stress-testing
description: 'Use this skill after a strategy has passed [monte-carlo-trade-resampling-and-drawdown-distribution](../monte-carlo-trade-resampling-and-drawdown-distribution/SKILL.md), to test it against price conditions that did not literally occur historically but are plausible. Also use it whenever a user asks "what happens if the market does something it hasn''t done before" or wants to know how a strategy would handle a crash, a liquidity crunch, or a regime that isn''t in the historical sample. This skill exists because resampling historical trades, however rigorously, can only ever recombine outcomes that actually happened; a strategy that has never been tested against a plausible-but-unprecedented scenario has a real, unmeasured gap in what''s been checked.'
---

# Synthetic Data and Adversarial Stress Testing

## Why this matters

[monte-carlo-trade-resampling-and-drawdown-distribution](../monte-carlo-trade-resampling-and-drawdown-distribution/SKILL.md) resamples the trades that actually happened, in different orders and combinations, which is a real and necessary check, but it can never produce a scenario outside the range of what already occurred in the historical sample. A market condition that hasn't happened yet in the backtest period, a faster crash, a longer liquidity drought, a correlation structure that breaks down differently than any historical episode, is a real risk that pure historical resampling structurally cannot surface, because it isn't built from recombining history; it has to be generated.

## Do this

### Generate simulated price paths using a model fit to the instrument's actual statistical properties

Fit a model (a GARCH-family model for volatility clustering, a jump-diffusion model if the instrument exhibits real jump risk, or a simpler bootstrapped-returns model as a baseline) to the actual historical statistical properties of the instrument being traded, then generate new, synthetic price paths from that model rather than from the literal historical sequence. These paths will share the instrument's real volatility and tail characteristics without being constrained to only ever recombine historically-realized moves, which is exactly the gap pure trade resampling can't close.

### Deliberately construct adversarial scenarios beyond what any fitted model would typically generate

In addition to model-generated synthetic paths, construct specific, deliberately harsh scenarios by hand: a volatility spike materially larger than any historical episode in the sample, a liquidity drought lasting longer than any historical gap, a correlation breakdown between instruments the strategy assumes are related. These aren't meant to be probable; they're meant to answer "if this specific bad thing happened, what does the strategy actually do," which is a different and complementary question to "how likely is a bad outcome given the historical distribution."

### Test the strategy's actual behavior under each synthetic scenario, not just its theoretical exposure

Run the strategy's real logic, including its risk management, stop-loss, and position-sizing rules, against each synthetic or adversarial scenario, rather than only computing a theoretical loss from a static position. A strategy's actual behavior under stress depends on how its rules react in real time (does a stop-loss rule trigger and actually get filled at a reasonable price, or does the scenario include exactly the kind of gap or liquidity conditions that would prevent that fill), and that has to be simulated through the strategy's real decision logic to be meaningful.

### Pay special attention to scenarios that break assumed relationships between instruments

Strategies that rely on a relationship between multiple instruments (pairs, baskets, hedges) are particularly exposed to scenarios where that relationship breaks down in ways no historical episode fully captures. Deliberately construct scenarios where an assumed hedge stops hedging, where a normally stable spread widens far beyond its historical range, or where correlations that are usually stable temporarily invert, and check what the strategy actually does when that assumption fails.

### Treat a strategy that fails badly on a plausible synthetic scenario as a finding, not a false alarm

A strategy that performs acceptably on all historical resampling but fails catastrophically on a plausible (even if historically unprecedented) synthetic scenario has a real, identified weakness, even though it never showed up in any historical backtest. The temptation to dismiss synthetic-scenario failures as "unrealistic" needs to be checked against whether the scenario is actually implausible, versus simply being a scenario that happens not to have occurred yet in the available historical window; markets regularly produce conditions with no exact historical precedent.

## Never do this

- Never treat historical trade resampling as sufficient stress testing on its own; it can only recombine outcomes that already occurred, and cannot surface genuinely unprecedented-but-plausible conditions.
- Never generate synthetic price paths from a model that wasn't actually fit to the instrument's real statistical properties (volatility clustering, tail behavior); an arbitrary or generic simulation model doesn't test anything meaningful about this specific instrument.
- Never stress-test only the theoretical exposure of a static position; run the strategy's actual decision logic, including risk management and execution assumptions, through each scenario.
- Never skip stress-testing the specific relationships (hedges, pairs, spreads) a multi-instrument strategy depends on; these are exactly where synthetic scenario testing adds the most value over historical resampling alone.
- Never dismiss a bad result on a synthetic scenario as "unrealistic" without a specific, concrete reason the scenario genuinely couldn't occur, rather than it simply not having occurred yet historically.

## Verification checklist

- [ ] Synthetic price paths were generated from a model actually fit to the instrument's real statistical properties, not an arbitrary or generic simulation
- [ ] At least one deliberately adversarial, hand-constructed scenario beyond what the fitted model would typically generate was tested (a larger-than-historical volatility spike, a longer liquidity drought, or similar)
- [ ] For any multi-instrument strategy, at least one scenario specifically breaking an assumed relationship (hedge, spread, correlation) between the instruments was tested
- [ ] Each scenario was run through the strategy's actual decision logic and execution assumptions, not just a static theoretical exposure calculation
- [ ] Any scenario that produced a bad outcome was evaluated for whether it's genuinely implausible or simply unprecedented-so-far, before being dismissed
