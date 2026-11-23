# Analyze Meta reports and proposals

## When to read

Read when report arithmetic, contribution scenarios or a concrete budget/status proposal would resolve the question. Use the user's reporting surface, spreadsheet, calculator or local analysis tools. Keep source exports intact and show the assumptions that affect the answer.

## Make the report comparable

Record account, currency, timezone, date range, level, purchase event, value basis, attribution window and report time. State whether coverage is the whole account or a selected subset. Do not add campaign totals to their ad sets, mix demographic breakdowns with totals, or sum overlapping purchase action types.

Use consistent entity identities and compatible periods. Preserve fractional estimated conversions rather than relabeling them as whole observed orders. Missing rows or metrics remain explicit. A partial sum should be labeled as a known subtotal, not a complete account total.

Calculate ratios from compatible sums using the [metric definitions](metric-definitions-and-reconciliation.md#worked-decisions). Multiply link CTR by 100 when expressing it as a percentage.

A zero denominator is undefined; a missing denominator is unknown. Keep those explanations separate. Illustrative totals of 1,000 spend, 50,000 impressions, 1,000 link clicks, 40 purchases and 3,000 purchase value yield CPC 1, CTR 2%, CPM 20, CPA 25 and ROAS 3. These are arithmetic examples, not an observed campaign or causal estimate.

Inspect representative source rows and reconcile narrative versus table conflicts before proceeding. Currency conversion, overlapping entities and attribution semantics require an explicit explanation; the arithmetic cannot establish them.

## Compare contribution and cash

Contribution = retained revenue − relevant variable costs − ad spend. Keep modeled scenarios distinct from observed outcomes and use matched horizons. Missing costs prevent a complete comparison, and a scenario difference is not experimental lift. Declining ROAS alone doesn't prove an expansion loses money, and higher total contribution doesn't prove the extra spend was worth its risk. Worked contribution and dated-cash examples live in [acquisition contribution and funding](acquisition-contribution-and-funding.md); campaign metrics don't supply a cash forecast.

## Prepare the change

Identify the exact account/entity, current state, budget owner, currency, observation time, proposed value and authorized bound. Distinguish daily and lifetime budgets and display amounts from API minor units. An illustrative 80→100 daily budget within a 110 bound is a proposal, not proof that the field, entitlement or operation is available.

For bid/ROAS controls, use the current supported interface and state the actual change. A daily budget setting is not an exact daily-spend ceiling. Preserve a rollback condition based on fresh state; another operator's edit can invalidate the previous inverse.

Before acting, follow [execution and reconciliation](execute-and-reconcile-changes.md): read current state, verify supported encoding and scope, apply the authorized change, then read back. An unknown response requires reconciliation before retry. Keep the calculation, allocation decision and causal claim separate.
