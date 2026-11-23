# Compare checkout observations

## When to read

Read when a supplied payload, browser observation or export needs exact comparison with the intended checkout result. Use direct inspection for a few fields and the user's spreadsheet or local data tools for larger records. Preserve originals and keep selected customer data in approved storage.

## Compare the failing boundary

Identify the provider, account, environment, object and source version before joining records. Establish expected values from the selected merchandise, configuration or an independently specified passing control. Copying the faulty payload into the expectation proves nothing.

Build a short table: field and source locator, intended value, rendered value, submitted value, persisted value, and discrepancy. Include only the columns that the task actually exposes. Keep strings, booleans, quantities and money distinct. The string “true” is not a boolean; an ID with leading zeros must retain them. Preserve array order unless the platform contract makes it immaterial. Missing, explicit null, false and zero are different observations.

For money, establish the provider's units and precision before calculation. Compare exact decimal values or correctly scaled minor units, not rounded binary floating-point approximations. An amount of 1200 can mean twelve units of a two-decimal currency or twelve hundred major units; the field contract decides. Keep quantity, unit price, discounts, line total and payable total separate.

## Worked decisions

Illustrative: the selected variant and quantity are correct, but the personalization property is submitted as a string instead of a boolean. Repair that serialization at the request boundary and repeat the same case plus a relevant passing neighbor. If quantity is absent from the inspected payload, record “not observed”; absence is not a zero or a pass.

For a bundle, multiply parent count by units per parent, then add loose units. Compare each component and its parent relationship before trusting the total. Two rows can sum correctly while belonging to different bundles. Preserve price fragments and reconcile their sum with the payable total rather than replacing them with a guessed single row.

## Close at the supported level

Record which selected fields match, disagree or remain unobserved. A match for those fields does not establish the whole checkout, real-wallet behavior or fulfillment. Obtain the missing authorized readback when needed; do not resubmit a purchase to fill a gap. A scope or version mismatch makes the comparison inconclusive.

For callback and recovery faults, use the existing isolated harness or a minimal event timeline described in [payment state](payment-state-and-recovery.md). Keep the original operation identity. A comparison table neither authorizes a payment nor supplies provider idempotency.
