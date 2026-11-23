# Metric definitions and reconciliation

## When to read

Load before interpreting imported metrics, calculating thresholds, comparing windows or explaining a disagreement between Meta and commerce reports. Use the metric dictionary and arithmetic, with definitions immediately beside formulas.

## How to do the work

Write a measurement specification before joining incompatible reports: account, currency, timezone, complete window, entity level, selected event/value basis, attribution and report-time convention. Export one aggregate row per entity for that window. Map the selected purchase event deliberately: do not add a parent purchase total to website purchases it already contains. Preserve the original export and keep the mapping with the result.

Follow [report analysis](analyze-reports-and-proposals.md) to sum compatible quantities before computing ratios. Keep missing metrics and incomplete windows visible. Check duplicate entities, hidden overlap, modeled values and source coverage rather than trusting a declared complete flag. Compare representative rows and the account-level export with the derived totals; investigate attribution or breakdown differences instead of forcing equality.

## Worked decisions

Most reconciliation disputes come from a handful of mismatches: link clicks versus all clicks; one selected purchase event versus several overlapping purchase actions added together; attributed purchase value versus collected or net sales; orders versus customers; account-day boundaries in different time zones; click versus view attribution and when conversions are reported; cohorts too young for their refunds. Count a buyer as new only when a defensible source says so. Keep missing, zero, suppressed and estimated values distinct. Recompute ratios from compatible sums rather than averaging row ROAS or CPA. Don't sum overlapping account/campaign/ad totals or infer unique reach by adding rows.

Core calculations: link CPC = spend/link clicks; link CTR = link clicks/impressions; CPM = 1,000 × spend/impressions; purchase CPA = spend/selected purchases; attributed purchase ROAS = selected attributed purchase value/spend. A zero denominator produces an undefined result with the reason, not zero performance. Break-even CPA can use defensible pre-ad contribution per acquired order; break-even ROAS = 1/contribution-margin rate only when the revenue basis, marginal mix and included costs match. Blended revenue/spend and platform ROAS stay separately labeled.

Worked example: a report contains 20 selected website purchases plus a broader purchase action row that includes those events. Adding both is rejected. A second example compares a 1-day click report with a 7-day click/1-day view report: the agent can report both but cannot call their difference a change in demand. A third retains contradictory narrative and table totals as unresolved rather than silently repairing them. Deliverable: reproducible metric table, assumptions and reconciliation exceptions. Formula correctness does not validate the source data.
