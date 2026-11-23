---
name: market-data-sourcing
description: 'Use this skill whenever choosing, evaluating, or setting up a historical or live market data source for a trading strategy, and whenever a user asks "what data provider should I use," compares options like Databento vs. Yahoo Finance, or is about to backtest without having thought about where the data actually comes from. Also use it when reviewing an existing backtest to check whether its data source has known gaps (survivorship bias, adjustment issues, futures roll handling) that would explain suspiciously good or inconsistent results. This skill exists because data quality problems are invisible in a backtest''s output; a bad data source doesn''t throw an error, it just quietly produces a wrong answer that looks like a right one.'
---

# Market Data Sourcing

## Why this matters

A backtest is only ever as good as the data it's run on, and data quality problems don't announce themselves. A data feed with survivorship bias, incorrectly adjusted prices, or a badly-stitched continuous futures contract will still produce a clean-looking equity curve; it just won't be measuring what the strategy would actually have done historically. Choosing a data source is a real design decision with real tradeoffs by asset class, not a solved, interchangeable commodity, and getting it wrong is one of the most common invisible causes behind [overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md)'s red flags.

## Do this

### Match the data source to the asset class, since the difficulty is genuinely different

Sourcing decent historical and live data is not equally hard across markets:

- **Crypto** is the easiest and cheapest by far. Most major exchanges (Binance, Coinbase, Kraken) publish historical OHLCV and even tick/trade data for free through public REST APIs or bulk downloads (Binance Vision, for example), and libraries like CCXT provide a unified interface across dozens of exchanges. Free crypto data is generally usable for serious backtesting with minimal caveats.
- **US equities** have decent free options but with real caveats: Yahoo Finance's free data is widely used but has known reliability issues (occasional bad ticks, adjustment inconsistencies, and no delisted-symbol history by default, meaning survivorship bias unless deliberately corrected for). Paid options like Polygon.io, IEX Cloud, and Norgate Data (which specifically markets survivorship-bias-free historical data including delisted symbols) close those gaps at real cost.
- **Futures** are the hardest and most expensive asset class to source well. Exchange-direct feeds (CME, ICE) are built for institutions and priced accordingly. Databento is a modern, pay-per-use option built for exactly this use case, with proper continuous-contract construction and multiple resolutions. IQFeed is a longer-standing retail-friendly option. Free futures data exists but is typically limited in history, resolution, or continuous-contract quality, so budget for this being a real cost center if futures are the target market.
- **Forex** sits in between: free tick data exists (Dukascopy publishes historical tick data at no cost) and most retail forex brokers provide historical data through their own APIs, but spread/liquidity conditions vary meaningfully by provider and aren't always representative of what a live account would actually see.

See [references/data-provider-comparison.md](references/data-provider-comparison.md) for a fuller comparison table across specific providers.

### Check whether a data source is survivorship-bias-free before trusting equity or index backtests

A historical universe that only contains symbols still listed today silently excludes every company that got delisted, went bankrupt, or was acquired away, which biases any backtest that trades a broad universe toward better results than would have actually occurred. This matters most for equities and equity indices; it's largely a non-issue for crypto and futures, where the relevant contracts/pairs are more stable over the backtest window. If a data source doesn't explicitly advertise survivorship-bias-free historical constituents (Norgate does; Yahoo Finance's free tier generally doesn't by default), assume it isn't, and either source a delisted-symbol dataset separately or scope the backtest to acknowledge the limitation.

### Understand exactly how continuous futures contracts are built before trusting a futures backtest

Futures contracts expire, so any multi-year futures backtest is actually trading a "continuous contract" stitched together from many individual expiring contracts, and how that stitching happens materially changes the price series. Back-adjusted (price differences at roll carried through the whole series) and ratio-adjusted methods change historical price levels in ways that can create or hide P&L that never actually existed; unadjusted, spliced-at-roll series create artificial price gaps at every roll date that a naive backtest can misread as real moves. Know which method a data source or backtesting library defaults to, and make sure it matches how the strategy will actually be traded (a strategy that holds through rolls needs the roll mechanics modeled explicitly, not abstracted away by an adjustment method).

### Check price-adjustment methodology for equities the same way

Adjusted-close prices smooth over splits and dividends for return calculations, but a strategy that trades on actual intraday price levels (support/resistance, absolute price thresholds, options strikes) needs to know whether it's looking at adjusted or raw prices, and needs that to be consistent across the entire pipeline. A mismatch (indicators computed on adjusted data, execution simulated against raw data, for instance) introduces a subtle, hard-to-spot error that behaves exactly like a data bug because it is one.

### Verify point-in-time accuracy, especially for anything beyond raw price/volume

Fundamental data (earnings, financial statements) is very commonly reported with the value as it looks today, not the value as it was actually known on the historical date in question, since companies restate financials. A backtest using fundamentals needs data that specifically preserves point-in-time as-reported values, not fundamentals that have been silently updated to reflect later restatements; using restated data is a direct form of lookahead bias, see [overfitting-and-robustness-checks](../overfitting-and-robustness-checks/SKILL.md).

### Normalize timezone and session conventions before combining sources

Combining data from two different providers, or a data feed with a broker's execution data, without checking both use the same timezone and session-boundary conventions is a common, easy-to-miss source of timestamp misalignment, which itself is a lookahead-bias vector (see the main overfitting skill). Explicitly normalize every feed to one timezone and one definition of session/bar boundaries before using them together.

### Know the real historical depth and rate limits of any free tier before committing to it

Free tiers often advertise access without clearly stating how far back history goes, what resolution is available, or how aggressively requests get rate-limited; discovering this only after building a pipeline around it is expensive. Check these limits explicitly against what the strategy actually needs (a strategy needing 10 years of 1-minute bars is a very different ask than one needing 2 years of daily bars) before choosing a source, not after.

## Never do this

- Never assume a data source is survivorship-bias-free by default; check explicitly, especially for equities.
- Never use a continuous futures contract without knowing which adjustment method built it and whether that method fits how the strategy will actually be traded through rolls.
- Never mix adjusted and unadjusted price data across the same pipeline without an explicit, deliberate reason and consistent handling.
- Never use restated fundamental data for a historical backtest; use point-in-time as-reported data or don't use fundamentals in the backtest at all.
- Never combine two data feeds without first normalizing timezone and session-boundary conventions.
- Never discover a data source's real historical depth or rate limits after already building the pipeline around it; check first.
- Never treat "free" and "adequate for this asset class" as the same claim, especially for futures, where free options are usually genuinely limited.

## Verification checklist

- [ ] The data source was chosen with the specific asset class's real difficulty in mind (crypto easy/cheap, futures hard/expensive, equities and forex in between with their own specific caveats)
- [ ] For equities/index backtests, survivorship-bias status of the historical universe was explicitly checked, not assumed
- [ ] For futures backtests, the continuous-contract adjustment method is known and matches how the strategy actually trades through rolls
- [ ] Price-adjustment methodology (adjusted vs. raw) is known and applied consistently across the whole pipeline, not mixed
- [ ] Any fundamental or other non-price data used is point-in-time/as-reported, not silently restated
- [ ] All combined data feeds were normalized to one timezone and one session-boundary convention before use
- [ ] The chosen source's real historical depth, resolution, and rate limits were checked against what the strategy actually needs, before building the pipeline around it

See [references/data-provider-comparison.md](references/data-provider-comparison.md) for a comparison of specific free and paid providers by asset class.
