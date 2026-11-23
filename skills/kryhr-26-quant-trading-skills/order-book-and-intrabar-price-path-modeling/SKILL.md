---
name: order-book-and-intrabar-price-path-modeling
description: 'Use this skill when tick-level, order-book, or Level 2 data is available and a backtest currently relies only on OHLC bar data to decide fills, especially for strategies sensitive to intrabar price movement (tight stops, short holding periods, or instruments with meaningfully wide spreads). Also use it when a user asks whether a backtest is losing accuracy by only knowing a bar''s open/high/low/close instead of what actually happened inside it. This skill exists because a single bar''s OHLC can be consistent with many different actual price paths inside that bar, some of which would have filled a given order and some of which wouldn''t, and picking the wrong one silently biases fill assumptions in [fill-feasibility-and-impossible-fill-detection](../fill-feasibility-and-impossible-fill-detection/SKILL.md).'
---

# Order Book and Intrabar Price Path Modeling

## Why this matters

OHLC bar data answers "what was the open, high, low, and close of this bar" but not "in what order did the price actually move, and what did the order book look like at each moment." A bar with a high above a limit order's price and a close below it is consistent with the price touching the limit early in the bar and never returning, or touching it right at the end after a full round trip, or touching it and immediately reversing without ever having real size available at that price; these different paths can imply genuinely different fill outcomes, and OHLC data alone can't distinguish between them. When finer-grained data is available, using only OHLC where tick or order-book data could resolve this ambiguity is leaving real fill-accuracy on the table.

## Do this

### Use tick or trade-level data to reconstruct the actual sequence of trades within a bar, not just its OHLC summary

Where tick data is available, reconstruct the actual sequence of trades that occurred within a bar and use that sequence to determine whether and when a limit or stop order would have actually filled, rather than only checking the bar's aggregate high/low against the order price. This directly resolves the path-ambiguity problem OHLC data can't: a limit order's fill probability and timing become a fact from the actual trade sequence rather than an assumption layered on top of a summary statistic.

### Use order-book (Level 2) data to check whether real size was actually available at the fill price, not just whether a trade printed there

A trade printing at a given price doesn't guarantee an arbitrary order size could have transacted at that exact price; order-book data shows the actual depth available at each price level at each moment, which is what determines whether a specific order size could have realistically filled there without moving through several price levels. Where order-book data is available, use it to check fill size against real available depth at the moment of the simulated fill, which is a more precise version of the volume-feasibility check in [fill-feasibility-and-impossible-fill-detection](../fill-feasibility-and-impossible-fill-detection/SKILL.md).

### Model queue position for passive (limit) orders when order-book data supports it

A limit order resting in the book doesn't fill just because the market trades at its price; it fills only after the orders ahead of it in the queue at that price level are consumed. For strategies that place passive limit orders, especially in markets with meaningful queue dynamics, model queue position explicitly using order-book data where available, rather than assuming any limit order at a touched price level fills immediately and completely, which is a common and significant source of backtest-to-live fill discrepancy for passive strategies specifically.

### Be explicit about the accuracy limitation when only OHLC data is available, rather than implicitly treating bar-level assumptions as certain

For strategies or instruments where only OHLC data is available (which, per [market-data-sourcing](../market-data-sourcing/SKILL.md), is common and often unavoidable, especially for retail-accessible historical data), be explicit that intrabar fill assumptions carry real uncertainty, and consider that uncertainty directly in the resampling and stress-testing done in [monte-carlo-trade-resampling-and-drawdown-distribution](../monte-carlo-trade-resampling-and-drawdown-distribution/SKILL.md) and [synthetic-data-and-adversarial-stress-testing](../synthetic-data-and-adversarial-stress-testing/SKILL.md), rather than treating the OHLC-based fill assumption as though it were a known fact.

### Weigh the cost of acquiring tick/order-book data against how much the strategy's results actually depend on intrabar precision

Tick and order-book data are meaningfully more expensive and harder to source than OHLC data (see [market-data-sourcing](../market-data-sourcing/SKILL.md)), so this investment should be prioritized specifically for strategies where intrabar path genuinely matters (tight stops relative to typical intrabar range, short holding periods, thin/wide-spread instruments), rather than applied uniformly to every strategy regardless of how sensitive its actual results are to intrabar assumptions.

## Never do this

- Never assume a single OHLC bar's high/low crossing an order price is sufficient to determine a realistic fill when tick or order-book data that could resolve the actual path is available and hasn't been used.
- Never assume a printed trade at a given price means an arbitrary order size could have filled there; check real order-book depth when it's available.
- Never assume a passive limit order fills immediately and completely whenever the market touches its price, without modeling queue position where order-book data supports it.
- Never treat OHLC-based intrabar fill assumptions as certain when only OHLC data is available; carry that uncertainty explicitly into resampling and stress-testing.
- Never acquire or build infrastructure for tick/order-book data without first checking whether the strategy's actual results are sensitive enough to intrabar precision to justify the cost.

## Verification checklist

- [ ] Where tick data is available, the actual trade sequence within a bar is used to determine limit/stop fill timing, not only the bar's aggregate OHLC
- [ ] Where order-book data is available, fill sizes are checked against real available depth at the fill moment, not only against whether a trade printed at that price
- [ ] Queue position for passive limit orders is modeled where order-book data supports it, rather than assuming immediate, complete fills whenever price touches the order level
- [ ] The accuracy limitation of OHLC-only fill assumptions is made explicit and factored into resampling/stress-testing, not treated as a known fact
- [ ] The decision to invest in tick/order-book data is based on whether the specific strategy's results are actually sensitive to intrabar precision, not applied as a blanket default
