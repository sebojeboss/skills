# Edge taxonomy reference

## Momentum / trend-following

- **Mechanism**: prices that have moved in a direction tend to keep moving, driven by underreaction to news, herding behavior, and slow-moving capital (institutional flows that take time to fully adjust).
- **Typical holding period**: days to months.
- **Typical equity curve shape**: long stretches of small losses during choppy/range-bound periods, punctuated by large gains during sustained trends. Should NOT look smooth; a trend-following strategy with a near-linear equity curve is a red flag, not a good sign.
- **Typical capacity**: generally high, especially on liquid futures/FX; less constrained than short-horizon strategies.
- **Typical failure mode**: extended choppy or mean-reverting regimes cause repeated small losses (whipsaw) with no trend to eventually pay for them.

## Mean-reversion

- **Mechanism**: prices that have moved away from some reference level (short-term average, fair value estimate, pairs relationship) tend to move back, driven by liquidity provision, overreaction correction, or temporary order-flow imbalances.
- **Typical holding period**: minutes to days, generally shorter than trend-following.
- **Typical equity curve shape**: can look smoother than trend-following in normal conditions, but has a distinct tail risk: rare, large losses when a "temporary" dislocation turns out to be a genuine regime break.
- **Typical capacity**: often more capacity-constrained than trend-following, especially at short horizons.
- **Typical failure mode**: catching a falling knife, a real structural break gets treated as a normal temporary dislocation and mean-reversion never occurs.

## Carry

- **Mechanism**: earning a persistent yield or roll return for bearing a specific risk (interest rate differentials in FX carry, term structure roll yield in futures, volatility risk premium).
- **Typical holding period**: weeks to months, often held continuously with periodic rebalancing.
- **Typical equity curve shape**: smooth, low-volatility gains most of the time, with sharp, infrequent drawdowns during risk-off unwinds.
- **Typical capacity**: often high in normal conditions, but liquidity can vanish exactly when the strategy most needs to exit, which is the core risk of the category.
- **Typical failure mode**: "picking up pennies in front of a steamroller," a sudden unwind erases a large fraction of accumulated gains in a short window.

## Statistical arbitrage / relative value

- **Mechanism**: exploiting a temporary mispricing between related instruments (pairs, baskets, index vs. components) expected to converge, often at high trade frequency with many small, largely uncorrelated positions.
- **Typical holding period**: minutes to days.
- **Typical equity curve shape**: can legitimately look smoother than single-instrument strategies specifically because of diversification across many simultaneous positions, not necessarily because of overfitting; this is the category where [overfitting-and-robustness-checks](../../overfitting-and-robustness-checks/SKILL.md)'s smoothness heuristic needs the most careful, category-aware judgment.
- **Typical capacity**: often meaningfully capacity-constrained; edge degrades as more capital competes for the same relative-value opportunities.
- **Typical failure mode**: the assumed relationship between instruments breaks down structurally (a merger falls through, an index methodology changes, a historically stable spread genuinely decouples).

## Market-making / liquidity provision

- **Mechanism**: capturing the bid-ask spread by continuously quoting both sides, compensated for the risk of being adversely selected by better-informed order flow.
- **Typical holding period**: seconds to minutes.
- **Typical equity curve shape**: many small wins, occasional larger losses during adverse-selection events or volatility spikes.
- **Typical capacity**: tightly constrained by the actual liquidity of the instrument being made markets in.
- **Typical failure mode**: adverse selection spikes faster than the spread captured can compensate for, especially around news events or regime shifts.

## Event-driven

- **Mechanism**: positioning around a specific, identifiable event (earnings, M&A, index rebalancing, macro releases) where the market's typical reaction is at least partially predictable.
- **Typical holding period**: hours to weeks, clustered around event dates rather than continuous.
- **Typical equity curve shape**: choppy, lumpy, gains and losses concentrated around event dates rather than smoothly distributed through time.
- **Typical capacity**: varies enormously by event type; some (index rebalancing flows) are well-studied and capacity-constrained, others are more idiosyncratic.
- **Typical failure mode**: the assumed distribution of event outcomes shifts (a historically reliable earnings-reaction pattern stops holding once enough participants trade it, or the events themselves become genuinely more unpredictable).

## Volatility risk premium (selling volatility)

- **Mechanism**: implied volatility tends to be priced above subsequently realized volatility on average, compensating the seller for bearing tail risk.
- **Typical holding period**: days to months, often via options or variance products.
- **Typical equity curve shape**: steady small gains most of the time, with sharp, severe drawdowns during volatility spikes; structurally similar to carry in shape, for a related underlying reason.
- **Typical capacity**: substantial but genuinely tail-risk-bearing; this category has produced some of the most dramatic real-world blowups in systematic trading history when volatility spiked far beyond what position sizing assumed.
- **Typical failure mode**: a volatility spike far larger than the position sizing assumed, converting a long history of small gains into a single catastrophic loss.
