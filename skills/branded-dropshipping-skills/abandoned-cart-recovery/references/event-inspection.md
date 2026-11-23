# Inspect the event behind the flow

## When to read

Missing entrants, mismatched counts, custom tracking or a flow called cart that actually listens to checkout.

## How to do the work

Name the shopper action first: item addition, checkout start, payment attempt or completed order. Locate one event's exact metric ID/origin in the integration and the sender. Follow its provider/account-scoped ID, profile identity, occurrence time and receipt time. Preserve both clocks: a backfilled event may appear in reports without being eligible to trigger a timely flow.

Inspect an actual permitted payload: variant, quantity, currency, visible items and return URL. Compare that payload with the flow's bound metric and template fields. A script loading proves neither event receipt nor identified/contactable profile. An email captured at checkout may not identify an earlier anonymous cart. Do not manufacture a cross-device join from similar names or amounts.

For a count discrepancy, align account, time zone, cutoff, unique profiles versus event occurrences and duplicate-event treatment. Compare event receipt with entry decisions, not aggregate revenue dashboards. A successful integration toggle is not a default repair; first isolate tracking settings, origin mismatch, stale events or flow status.

## Worked decisions

Illustrative: two metrics share a display name. The custom metric receives events while the flow still binds the native metric. Fix the binding or event route, then test the matching payload. Copy changes would not repair this boundary. Another shopper adds three items: three events can represent one episode rather than three eligible people.

## Deliverable and checks

Produce a scoped event map and discrepancy table using the native event view or supplied export. Retain provider/account, event identity, metric, profile identity, occurrence time and receipt time with timezone. Check missing fields, repeated/conflicting identities and receipt delays. Preserve original rows; do not invent a platform lateness threshold or join missing identities by guesswork.

Use provider-native recipient/activity evidence to establish entry into the actual flow. Compare the event map with eligibility and the selected platform configuration; a matching event name alone does not establish entry.
