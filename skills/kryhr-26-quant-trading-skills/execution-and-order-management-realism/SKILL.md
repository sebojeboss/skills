---
name: execution-and-order-management-realism
description: 'Use this skill whenever moving a strategy from backtest toward live or paper trading, and whenever designing the actual order logic (order types, retry behavior, fill handling) a strategy will use. Also use it when a user asks why their live results don''t match the backtest despite realistic cost assumptions, since that gap is often an execution-mechanics problem rather than a cost-modeling problem. This skill exists because a backtest and a real broker connection are different environments in ways that go beyond cost: partial fills, rejected orders, and API quirks are routine in live trading and essentially never modeled in a typical backtest.'
---

# Execution and Order Management Realism

## Why this matters

[transaction-cost-and-market-impact-modeling](../transaction-cost-and-market-impact-modeling/SKILL.md) covers the cost of a trade actually filling; this skill covers whether the trade fills as intended at all. A backtest almost always assumes an order either fills completely and immediately or doesn't happen; live trading routinely produces partial fills, rejected orders, delayed acknowledgments, and broker-specific quirks that a backtest never has to reckon with. A strategy whose logic silently assumes clean, complete fills every time will behave differently, sometimes badly, once it starts encountering the real mechanics of an actual broker connection.

## Do this

### Handle partial fills explicitly, not by assuming every order fills completely

Real order fills, especially for anything beyond a small order in a liquid market, can come back partially filled, filled in multiple pieces at different prices, or not filled at all within the intended time window. The strategy's logic needs an explicit answer for what happens next in each case (does it wait, does it cancel the remainder, does it adjust position sizing based on what actually filled), rather than code that implicitly assumes a full fill and would behave unpredictably if a partial one occurs.

### Design explicit retry and error-handling behavior for rejected or failed orders

Orders get rejected for real reasons (insufficient margin, price outside a collar, a temporary API error, an unsupported order parameter for a specific instrument) and a strategy needs a defined, deliberate response, not silent failure or an unhandled exception that stops the strategy without anyone noticing. Define what happens on rejection for each realistic failure category: retry with adjusted parameters, alert and pause, or fall back to a different order type, and test that this logic actually executes correctly rather than assuming it will work when the actual failure occurs.

### Account for latency between decision and order placement, and between placement and confirmation

The time between a strategy deciding to trade and the order actually reaching the exchange, and the time between placing an order and getting a confirmed fill back, both introduce real delay during which conditions can change. For latency-sensitive strategies this matters a great deal; for slower strategies it matters less but still isn't zero. Know the actual, measured latency of the specific broker/API connection being used, not an assumed or hoped-for value, and design order logic (limit price buffers, timeout/cancel behavior) around the real number.

### Test against a broker's paper/sandbox environment for real API behavior, not just the strategy's own logic in isolation

A broker's sandbox or paper-trading API often behaves differently from its production API in exactly the edge cases that matter most (rate limits, specific error codes, order-type support), and even the sandbox environment can differ from documented behavior in ways only discovered by actually using it. Run the strategy's real order-management code against the actual broker connection (sandbox first, then live with minimal size) specifically to surface these mechanical differences, rather than trusting that code which works in a backtest simulation will behave identically against the real API.

### Build monitoring that would actually catch an execution failure, not just a strategy-logic failure

A strategy can be generating correct signals while its order execution silently fails or behaves wrongly (an order that should have executed didn't, a position that should have closed stayed open), and that's a different failure mode than the strategy's decision logic being wrong. Build monitoring that specifically checks execution outcomes against intended actions (does the actual position match what the strategy believes its position is), not just monitoring of the strategy's signals or P&L, which wouldn't necessarily catch a case where the intended and actual positions have quietly diverged.

## Never do this

- Never assume every order fills completely; build explicit handling for partial fills and test that handling actually works.
- Never let order rejections fail silently; every realistic rejection category needs a defined, tested response.
- Never assume zero or negligible latency between decision, order placement, and fill confirmation without measuring the actual latency of the real connection being used.
- Never trust that order-management code which works correctly in a backtest simulation will behave identically against a real broker API without testing it against the actual (sandbox, then live) connection.
- Never rely solely on signal-level or P&L-level monitoring to catch execution problems; build monitoring that specifically compares intended positions against actual positions.

## Verification checklist

- [ ] Partial-fill handling is explicit and tested, not assumed away
- [ ] Every realistic order-rejection category has a defined, tested response rather than silent failure
- [ ] Real, measured latency (decision-to-placement, placement-to-confirmation) for the actual broker connection informs the order logic's timeout and price-buffer behavior
- [ ] The strategy's order-management code has been tested against the broker's actual sandbox and/or live API, not only against a backtest simulation of order behavior
- [ ] Monitoring exists that specifically checks whether actual positions match intended positions, not only signal-level or P&L-level monitoring
