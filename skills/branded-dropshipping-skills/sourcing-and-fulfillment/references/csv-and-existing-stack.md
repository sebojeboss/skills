# Prepare order files in the existing stack

## When to read

Read when supplier, store or carrier exports are supplied, a direct adapter is unavailable, or the current stack uses Shopify, DSers or manual files.

## How to do the work

Start with the actual export and destination template. Preserve the raw file locally. Record source headers, grouping rule, destination fields, unit conversions and excluded private fields. Shopify extra line-item rows may omit repeated order fields; fill them only inside a verified order group. Never use a buyer email as the group identity.

For DSers, map product/SKU records before order imports. Use the current product and import_orders templates, review imported orders, then treat supplier submission and payment separately. Read the per-row import/error report before resubmitting; partial success can otherwise duplicate orders. Keep returned tracking joined to the source order rather than assuming native sync to every sales platform.

Use the merchant’s existing spreadsheet or local data tools to transform only the required fields. Review the destination template and a sample row before producing a batch. Missing required recipient fields belong in a rejected-row report; do not fabricate a phone/address or strip valid characters just to pass validation. Verify country-specific identity/customs requirements from applicable records.

Official dependencies: https://help.shopify.com/en/manual/fulfillment/managing-orders/exporting-orders and https://help.dsers.com/place-csv-orders/. Verify actual templates; older help tables may contain inconsistent country descriptions.

## Worked decisions (illustrative)

A store export contains payment and marketing fields the supplier does not need; create a minimum supplier file, preserving the untouched original locally. An import error report does not prove every row failed: reconcile partial results before resubmission.

## Deliverable and checks

Source-to-destination field map, validated draft product/order files, rejected-row report and tracking reconciliation. The merchant can retain the existing platform; unsupported direct synchronization does not force a migration.

## Compare quotes on the same basis

Group by exact specification, quantity, currency, destination and service. Record goods, freight, packing and other charges with their unit basis: per item, pack, parcel or shipment. Convert to comparable sale units explicitly. A quote for two units is not automatically a per-unit price. Record included/absent fees as zero only when verified; a known subtotal with unresolved charges is not an all-in total.

Keep the dated quote, deviations, validity and inclusion evidence beside the comparison. A supplier's matching spec label does not establish equivalence. Do not rank stale or noncomparable quotes as cheapest. Use actual dimensional weight, packing and service terms when computing costs; no generic exchange rate or weight rule repairs missing information.

## Prepare supplier lines

Establish whether each order is ready from payment, cancellation, prior-submission and merchant instructions. Preserve provider/account/order/line identities. Map each sold variant to the exact supplier SKU and physical units, then multiply by ordered quantity.

Illustrative: three sold bundles each contain two units of supplier SKU `0007`; the draft requires six units. Keep the leading zeros, source order line and recipient fields required by that supplier. Omit marketing and payment fields that are not needed. Missing mappings, contradictory identities and invalid quantities stay rejected or unresolved; never silently substitute another SKU.

Do not collapse same-SKU lines across customers or assume one parcel per supplier line. Preserve the source-to-destination mapping when converting to the actual import template. Check row counts, total physical quantities and selected records before upload. A local draft, successful import, supplier acceptance and payment are separate states.

## Reconcile tracking before a write

Match account, order and stable parcel identity; a tracking number is a value attached to that parcel, not its permanent identity. Inspect all relevant destination records and pagination before treating absence as established. Compare the candidate with existing tracking:

- Same parcel and same tracking: retain the existing state.
- Same parcel and different tracking: investigate a correction, replacement or conflict.
- Multiple matching rows: resolve ambiguity before writing.
- No destination row and complete evidence: prepare the intended update.
- Incomplete evidence or an unknown earlier write: reconcile the original operation first.

Existing records absent from a new import are not deletion instructions. Preserve split shipments and quantities. Carrier attachment, carrier movement and delivery need their own observations; a tracking reconciliation does not establish them.

Write transformed files to a new destination and preserve the originals. Treat imported spreadsheet cells as data; review formula-like text rather than activating it. Inspect partial-success reports before retrying. No proposed row by itself authorizes supplier submission or a live tracking update.
