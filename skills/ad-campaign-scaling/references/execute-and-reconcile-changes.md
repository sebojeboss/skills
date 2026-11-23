# Execute and reconcile changes

## When to read

Load before any account mutation, recovery from an uncertain response, or restoration of prior settings. Also load when preparing a machine-readable proposal for later execution. Reporting-only work does not load the full mutation procedure.

## How to do the work

Prepare a per-object diff with account/entity identity, current settings, desired values, economic bounds, review condition and scope of authorization. Daily-budget and status changes are the simplest to propose and verify; bid/ROAS edits need the current interface contract inspected first.

Before applying through an available authorized native tool or browser, re-read the object and confirm budget ownership, currency/units, compatibility and effective status. Carry forward existing explicit authorization; ask only for missing scope after preparing the exact change. Apply dependent operations sequentially and preserve each response. Reopen/read the object after saving; distinguish request acceptance from settings observed, delivery observed and economic outcome.

If the response is lost, retain unknown state and read before retrying. If only part succeeds, stop dependent operations and reconcile each object. If another operator changed state, revise the plan rather than overwrite their work. For rollback, compare current values with the post-change expected values and restore only the authorized compatible fields; pause for a new decision if those preconditions no longer hold. Keep incurred spend in the result.

## Worked decisions

Most failed edits come from editing the wrong thing: the ad set when the campaign owns the budget, a value entered in the wrong currency unit, a field the current objective or bid strategy doesn't accept, or an object another person or an automated account rule changed since you last read it. Re-read state immediately before writing. The main execution path here changes budgets, bids and status on existing campaigns or ad sets. Creating or duplicating them is a separate requested operation: use an available supported interface, inspect the current required fields, prepare new objects paused at the applicable hierarchy levels, and reconcile creation before activation. Activation enables spend and stays within the user's authorized scope.

Prepare the concrete plan before asking for genuinely missing authorization. Do not repeatedly ask when the existing instruction already authorizes the bounded action. Conversely, analysis approval, authentication and a profitable-looking report are not authority to spend. If automatic execution is requested, specify bounds, account, allowed operations, review/stop conditions and duration rather than infer an open-ended mandate.

A preflight fingerprint reduces stale edits but is not an atomic compare-and-set guarantee. A rollback returns supported fields to an agreed prior state; it cannot refund spend, restore auction conditions or recreate prior learning.

Worked example: a budget update times out. Reading the object shows the desired budget; record observed reconciliation without sending the same mutation again. In a second example, another operator changes the bid before rollback, so the old inverse plan is stale and needs a revised decision.
