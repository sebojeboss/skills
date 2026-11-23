# Offer measurement

## When to read

Read when choosing denominators, interpreting results, planning a comparison or deciding stop/repair/retain.

Operators usually rank offers by revenue per visitor (or per offer view) and profit per visitor; some say earnings per view. Use the user's word, then define the visitor: everyone eligible for the offer, counted before anyone was put off by it. For a product-page add-on that is everyone who landed on the page. For a post-purchase offer, count both eligible buyers and those who actually reached the offer page; a rendering or payment-method gap shrinks the second without saying anything about demand. Take rate is acceptances divided by a stated base: exposed or eligible.

Define assignment, technical eligibility, exposure, acceptance, paid order and retained outcome separately. Pre-purchase changes must retain deterred entrants; a primary causal comparison must not condition on a treatment-affected event. Post-payment take rate needs both eligible and actually exposed counts, alongside separately defined broader outcomes.

Join by provider/account-scoped identity, preserve zero-order entrants, reconcile purchases and later refunds and compare equal follow-up ages. Distinguish concurrent test traffic from dashboards that continue accumulating after one arm stops. Historical comparisons remain descriptive unless their design warrants more. Preserve mature renewal revenue and costs rather than comparing an older cohort's lifetime with a young cohort's entry revenue. Do not turn a diagnostic segment into a confirmed subgroup or a no-detected-difference result into equivalence.

**Illustrative worked decisions:** 80 acceptances from 800 exposed and 1,000 predefined eligible buyers produce 10% exposed and 8% eligible take rates, neither storewide CVR. Higher first-order subscription share may coexist with lower entry conversion and later parity. Short-window entry results and later cohort results answer different questions; do not pool them into one winner. A stalled comparison may be stopped for opportunity cost without declaring the offer universally ineffective.

## Build an analysis from local exports

Use the existing experiment/reporting system or a local spreadsheet/query with explicit joins. Start with the assignment/eligible-entrant table, one row per defined unit. Left-join outcomes so nonbuyers remain. Aggregate repeated exposure events separately before joining orders; otherwise one purchase can multiply across several views. Keep original order and post-purchase additions associated without counting the original order twice.

Use the actual assignment and order exports. Retain the experiment/offer version, assignment unit and time, eligible cohort, order identity and time, currency, retained revenue, relevant costs, refunds/returns and observation cutoff. Exclude names, emails and street addresses from this analysis. Preserve source totals, exclusions and reasons. Resolve duplicate assignment, cross-arm customers, missing currency and ambiguous timestamps before interpreting results. Compare equal-aged cohorts for mature outcomes and show how many original entrants remain eligible for that analysis.

Report a compact funnel: assigned/eligible → exposed → accepted → paid → retained. A rendering failure changes exposure, not necessarily demand. Diagnose eligibility by payment method and device before replacing the offer. Report contribution per original entrant alongside take rate and basket mix; a size menu can keep take rate steady while reducing revenue per exposure.

For subscription offers, show initial conversion and contribution separately from paid renewals, skips, canceled future orders, refunds and variable costs. Keep a holdout if the existing system supports a valid comparison. Do not suppress required billing notices for an experiment. Use uncertainty estimates appropriate to the experiment's assignment design. A historical before/after table can be useful but remains descriptive when assignment and concurrent demand differ.
