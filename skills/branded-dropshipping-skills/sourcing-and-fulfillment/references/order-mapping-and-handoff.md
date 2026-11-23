# Order mapping and handoff

## When to read

Transform store orders into supplier input, connect product variants, review a first handoff, or diagnose installed-but-not-fulfilling software.

## How to do the work

Start with account-scoped order and line IDs, not buyer email. Map each store variant to supplier SKU and units per sold unit. For a bundle, list components explicitly; verify whether the destination can represent multiple supplier lines and parcels. Preserve leading zeros. The same display order number can exist in several stores.

Carry the paid order's selected attributes into the supplier map: store variant ID → exact supplier SKU → physical units. Match size charts or dimensions where supplier labels differ; the same “M” is not a fit guarantee. Recheck stock and dispatch terms for that SKU and destination. A supplier's generic product link or default color cannot fill a missing mapping. If the purchased combination is unavailable, hold that line for an approved remedy rather than silently substitute.

Illustrative: two shirts share a product title, but navy/M and navy/L have different supplier SKUs. The buyer paid for L; the supplier import defaults to M. Correct the mapped line before submission, then verify the supplier acknowledgment still names L. If the supplier splits the order, keep each line's parcel allocation so one delivery scan cannot close both.

When a warehouse or 3PL fulfills bundles, check what it actually receives. A bundle sent as one line of quantity eight is still eight units to the warehouse. Whether it is picked and billed as one case depends on what the warehouse gets, and on its own case-pick rule, not on how few rows the order shows. What it gets might be a case SKU, or a parent/component mapping it actually honors. Collapsing rows to reduce picks changes nothing unless that mapping changes.

Determine readiness from the actual paid/cancelled/refunded/submitted state and user instruction. Do not send an order again merely because tracking has not arrived. Reconcile prior submission before marking a normalized line ready. Project only the shipping/contact fields the authorized recipient requires. Billing address is not a substitute for missing shipping address.

Expand the reviewed variant/component map into supplier-line drafts using the existing spreadsheet or local data tools. Verify readiness separately from field mapping. Inspect rejected rows and totals by order, supplier and physical component. Translate into the actual current supplier template after checking headers and required fields. Import acceptance, a supplier order reference and supplier payment are separate observations; retain each that exists.

## Worked decisions (illustrative)

Two orders share a buyer email, one contains two variants and one has already been sent. Exact identifiers resolve the two safely; missing line identity produces an exception rather than fuzzy matching. An installed connection with unmapped variants remains incomplete.

## Deliverable and checks

Local mapping table, recipient-minimized handoff draft, excluded/ambiguous rows and reconciliation keys. No silent order placement or substitute item selection.
