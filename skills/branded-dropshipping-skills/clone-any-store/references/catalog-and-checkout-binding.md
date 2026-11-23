# Catalog and checkout binding

## When to read

Read when real products, variants, prices, stock, quantity, cart or buy actions are requested, or when existing commerce must survive a visual change.

## How to do the work

Use destination-owned product/variant IDs, complete pagination and approved terms; titles and source-store IDs are not reliable keys. Current Whop records document variant attributes, SKU, stock and quantity controls. Enforce uniqueness in the local SKU map because the platform does not enforce SKU uniqueness. A stock value hidden by permissions is unknown, not zero; an unlimited-stock flag changes how the numeric stock is interpreted. Preserve exact amount units, currency, cadence and source version.

Build the selected-options/cart UI locally and bind it to compatible items. Current Elements `items` supports same-seller plans and quantities; the API additionally requires compatible variants and the same currency. The mounted checkout's order inputs are fixed: remount after a cart change instead of expecting new props to replace its order. Amount authority stays with the server/catalog. Keep structured shipping address separate from billing address. Documented shipment tracking does not buy a label, reserve warehouse inventory or submit a supplier order. Native carrier rating, split fulfillment, exchanges/restock and physical-renewal control still require a supported operational contract.

When distribution is part of the brief, keep the documented several-variant buyer-affiliate exclusion beside the recommendation. It is not a SKILL business-referral rule. A browser return/callback is not authoritative fulfillment evidence; payment-network and checkout-debug own the deeper state contract.

Read [commerce conventions](commerce-record-conventions.md). Obtain authorized, complete catalog pages scoped to the destination business and environment. Normalize only the fields needed for the selected cards: ID, SKU, attributes, amount with explicit basis, currency, cadence, quantity rule, stock visibility and purchase availability. Keep the original receipt/version alongside the local mapping; missing data remains unknown.

Keep a small binding table with source item, approved destination product/variant, account/environment, price/currency/cadence, quantity and observed stock. Compare it against the current catalog and rendered buy action. Check local SKU uniqueness and actual pagination/coverage before calling the mapping complete. A binding table does not reserve stock or establish mixed-cart rules and account entitlement.

Build the option picker from actual attribute combinations. A size and a color being listed separately does not mean every combination exists. Bind the selected combination to its destination variant, image, price, quantity rules and availability; disable unavailable combinations. Changing color must not silently reset the chosen size to a different item. Preserve the selection through cart edits and use structured fields rather than hiding options in notes.

Before mounting checkout, verify the whole cart against the deployed [Elements checkout](https://docs.whop.com/elements/latest/checkout/overview.md) and [payment creation](https://docs.whop.com/api-reference/payments/create-payment.md) contracts, including stock mode and billing compatibility. Single-variant stock support does not establish finite-stock multi-item support. Never mark finite stock unlimited to make a cart pass. Follow the chosen variant through the submitted item, checkout display and authorized paid-order readback; a correct selector alone does not prove the correct item was bought.

For physical goods, establish the supported destination/address/rate/fulfillment path before calling the offer ready.  Preserve pending/failed/canceled states and route verified payment events through the actual order owner.

## Worked decisions

Illustrative example: a tray has two color variants and an optional accessory. Map each configuration to its approved SKU/variant, assemble compatible quantities and remount when the accessory changes. A monthly refill plus a one-time accessory cannot be assumed compatible; renewal variants cannot enable multiple quantity. Preserve existing source-of-truth systems when those operations are not replaced.

Illustrative delivery distinction: the UI can show the selected accessory and still submit the original single item if the mounted checkout was not recreated. Record selected IDs/quantities before and after editing, remount for the new cart, and verify the purchase surface reflects it. A server-reported price remains authoritative; do not trust a browser-calculated total as the charge request.

## Deliverable and checks

Deliver the binding map and observed noncharge behavior. Name unresolved transaction and fulfillment dependencies and hand them to their responsible owners.
