---
name: data-cleaning-and-preprocessing-pitfalls
description: 'Use this skill whenever raw market data is being loaded, cleaned, resampled, or otherwise preprocessed before feeding a backtest, and whenever a backtest''s results seem inconsistent with a quick manual sanity check of the underlying price series. Also use it when a user asks "why does my backtest look weird around this date" or is setting up a new data pipeline. This skill exists because a single bad tick, a missed corporate action, or a careless resampling step can silently distort a backtest''s results in ways that look like a real signal or a real anomaly, and companion skill market-data-sourcing covers choosing a good source, not what still needs to happen to the data once it arrives.'
---

# Data Cleaning and Preprocessing Pitfalls

## Why this matters

Even data from a genuinely good source, chosen per [market-data-sourcing](../market-data-sourcing/SKILL.md), arrives with real imperfections: bad ticks, missing bars, unadjusted corporate actions, and gaps that need explicit handling before the data is fit to feed a backtest. None of these announce themselves; a bad tick doesn't throw an error, it just becomes a real number that a strategy's logic treats as a real price, potentially generating a signal or a trade that would never have existed with clean data. The backtest doesn't know the difference between a real anomaly and a data error, so the pipeline has to catch it before the backtest ever sees it.

## Do this

### Explicitly detect and handle outlier ticks rather than trusting every printed value

Raw tick and even bar data occasionally contains genuinely erroneous prints (a fat-finger trade, a feed glitch, a decimal-point error) that are orders of magnitude away from the surrounding data. Build explicit outlier detection (a check against a rolling volatility-scaled bound, for instance, flagging any move that's implausibly large relative to the instrument's recent realized volatility) and either correct or exclude flagged values rather than assuming every printed number in a data feed is real.

### Check for and explicitly handle missing bars/gaps, don't let a plotting or resampling library silently paper over them

A gap in the data (a missing bar, a feed outage, an exchange halt) needs an explicit decision: forward-fill, interpolate, or leave as a genuine gap the strategy has to handle, and that decision should be made deliberately based on what's actually appropriate for the instrument and strategy, not left to whatever a charting or resampling library defaults to silently. A resampling step that silently forward-fills a multi-day gap as though trading continued normally can introduce phantom continuity that never existed.

### Verify corporate-action adjustments are applied consistently, or not at all, but never inconsistently

For equities, splits and dividends need to be either fully and consistently adjusted for across the whole pipeline, or fully and consistently left raw, matching whatever decision was made in [market-data-sourcing](../market-data-sourcing/SKILL.md) about adjusted vs. raw prices. A pipeline that adjusts for splits but not dividends, or that adjusts historical prices but computes returns from unadjusted ones, introduces exactly the kind of quiet, structural error that looks like real signal in a backtest.

### Check resampling logic for off-by-one and boundary errors, which are a common, subtle lookahead vector

Resampling tick or intraday data into bars (turning trades into 1-minute or daily OHLCV bars, for instance) has real edge cases at bar boundaries: whether a trade exactly at a boundary timestamp belongs to the bar ending or the bar starting, whether a bar's "close" is actually available at the timestamp the bar is labeled with or only after some processing delay. Getting this wrong in either direction can introduce a look-ahead (a bar labeled as available before its data was actually final) or a lag (treating information as unavailable later than it actually was), both of which distort backtest timing in ways that are easy to miss and directly relevant to the lookahead-bias warnings in [overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md).

### Cross-check a data pipeline's output against an independent source or manual spot-check before trusting it at scale

Before running a full backtest on a newly built or modified data pipeline, spot-check its output against an independent source (a different data provider, or a manual look at a well-known historical event, like an obvious price around a known market crash date) for a handful of specific dates and instruments. This catches systematic pipeline errors (a timezone offset applied wrong, a units error, a misaligned join between two data sources) before they've silently shaped an entire backtest's results.

### Log every cleaning/correction decision, since undocumented data cleaning is itself a form of the multiple-testing problem

If outlier correction thresholds, gap-handling rules, or any other cleaning parameter got adjusted specifically because it improved backtest results, that's the same kind of search-and-select process [statistical-significance-and-deflated-metrics](../statistical-significance-and-deflated-metrics/SKILL.md) warns about, just happening in the data pipeline instead of the strategy logic. Document cleaning decisions and their rationale before looking at how they affect strategy performance, and treat any cleaning-parameter change made after seeing a performance improvement with the same skepticism as a strategy-parameter change made the same way.

## Never do this

- Never trust every value in a raw data feed as necessarily correct; build explicit outlier detection rather than assuming bad ticks don't exist in the source being used.
- Never let a gap or missing-bar situation be silently resolved by whatever a plotting or resampling library defaults to; make an explicit, deliberate decision appropriate to the instrument and strategy.
- Never apply corporate-action adjustments inconsistently across a pipeline (adjusting some elements but not others, or adjusting historical prices while computing returns from unadjusted data).
- Never resample data into bars without checking boundary-timestamp handling for lookahead or lag errors.
- Never trust a newly built or modified data pipeline at scale without first spot-checking its output against an independent source for at least a few known dates and instruments.
- Never adjust a data-cleaning parameter specifically because doing so improved backtest performance without treating that change with the same scrutiny as a strategy-parameter change chosen the same way.

## Verification checklist

- [ ] Outlier/bad-tick detection is applied explicitly to the raw data, not assumed unnecessary
- [ ] Gaps and missing bars are handled through an explicit, deliberate decision suited to the instrument and strategy, not a silent library default
- [ ] Corporate-action adjustments are applied consistently across the entire pipeline, matching the adjusted-vs-raw decision made during data sourcing
- [ ] Resampling/bar-construction logic has been checked for boundary-timestamp errors that could introduce lookahead or lag
- [ ] The pipeline's output has been spot-checked against an independent source or manual check for at least a few known dates/instruments before being trusted at scale
- [ ] Every data-cleaning decision and its rationale is documented, and no cleaning parameter was adjusted specifically because it improved backtest performance without applying the same scrutiny as a strategy-parameter change
