# Data provider comparison by asset class

Specific products and pricing change; treat this as a map of what kinds of options exist and what to check, not a permanently accurate price list. Verify current pricing and coverage directly with the provider before committing.

## Crypto: easiest and cheapest asset class to source

| Source | Cost | Notes |
|---|---|---|
| Exchange public APIs (Binance, Coinbase, Kraken) | Free | OHLCV and often trade-level data via REST/WebSocket; Binance Vision publishes free historical bulk downloads |
| CCXT (library, not a data source itself) | Free | Unified API across 100+ exchanges, useful for normalizing multiple exchanges' data into one interface |
| CryptoCompare, Kaiko | Free tier + paid | Aggregated cross-exchange data, useful when a single exchange's liquidity/history isn't sufficient |

Caveats that still apply: exchange outages and API changes happen; very old history on smaller exchanges can be thin or unreliable; perpetual futures funding-rate history is not always as complete as spot OHLCV.

## US equities: decent free options, real caveats

| Source | Cost | Notes |
|---|---|---|
| Yahoo Finance (via yfinance or similar) | Free | Widely used, but has known reliability issues: occasional bad ticks, inconsistent adjustment handling, no delisted-symbol history by default (survivorship bias risk) |
| Alpaca Market Data | Free tier (recent history) + paid (deeper history) | Free tier is usable for strategies that don't need deep history |
| Polygon.io | Paid (has a limited free tier) | Better data quality and depth than free options, tick-level available |
| IEX Cloud | Paid (has a limited free tier) | Reasonable equities data, exchange-sourced |
| Norgate Data | Paid subscription | Specifically markets survivorship-bias-free historical data including delisted symbols; a real answer to the biggest free-tier equity data gap |

## Futures: hardest and most expensive asset class to source well

| Source | Cost | Notes |
|---|---|---|
| Exchange-direct feeds (CME, ICE) | Expensive, institutional pricing | Highest quality, priced for firms, not individuals |
| Databento | Pay-per-use | Modern API, proper continuous-contract construction with documented methodology, multiple resolutions including tick |
| IQFeed | Paid subscription | Longer-standing retail-friendly option, real-time and historical |
| Norgate Futures | Paid subscription | Continuous contracts with documented adjustment methodology |
| Free options | Free | Generally limited in history depth, resolution, or continuous-contract quality; treat as adequate for prototyping only, verify before relying on for real validation |

Futures-specific check regardless of provider: know exactly how the continuous contract is built (back-adjusted, ratio-adjusted, or unadjusted/spliced) and whether that matches how the strategy will actually be traded through contract rolls. See the main [market-data-sourcing SKILL.md](../SKILL.md) for why this matters.

## Forex: free tick data exists, but representativeness varies

| Source | Cost | Notes |
|---|---|---|
| Dukascopy | Free | Publishes historical tick data at no cost, widely used for retail forex backtesting |
| Broker-provided historical data (OANDA, IC Markets, etc.) | Usually free with an account | Reflects that specific broker's pricing/spread, which may not generalize to other brokers or execution venues |
| Paid aggregators | Paid | Useful when cross-broker or deeper history is needed |

Forex-specific check: spread and liquidity conditions vary meaningfully by provider and by time of day (session overlaps); a backtest using one broker's historical spread assumptions may not reflect what a different live account actually experiences.

## Quick decision guide

- Prototyping a crypto strategy: free exchange APIs are genuinely sufficient, no need to pay for data early.
- Prototyping an equities strategy: free tier is fine for initial exploration, but budget for a survivorship-bias-free source (Norgate or similar) before trusting any result that trades a broad universe or spans a period with real delistings.
- Prototyping a futures strategy: budget for paid data from the start if the strategy needs continuous-contract history beyond a couple of years or needs a resolution finer than daily bars; free futures data is the option most likely to quietly produce a backtest that doesn't reflect reality.
- Any asset class, any source: verify historical depth, resolution, and rate limits against actual strategy needs before building a pipeline around it.
