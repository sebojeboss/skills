# Physical commerce readiness

## When to read

Read when selling physical goods on Whop, handing a cart to fulfillment, returns or subscriptions, or comparing those operations with Shopify.

## How to do the work

Map each sellable variant to the real SKU and supplier option, with quantity, price/currency and supported destination. Verify compatible cart construction, address handoff and the rule for reacting to a changed mounted cart. Trace a paid order to supplier acceptance, dispatch and delivery as separate states with an accountable owner. For returns, connect the monetary refund to the actual goods/restock decision without assuming either automatically completes the other.

Where the service does not enforce inventory, shipping rates or destinations, the merchant's own process has to; name who does. A webhook or automation-tool mention is not a verified supplier connector.

## Worked decisions

Current Whop contracts support variants/stock, compatible multi-item checkout, shipping-address collection and shipment tracking. Verify the current fields for the selected surface; variant IDs may retain plan naming. Enforce a unique local SKU-to-variant/supplier-option map where the service does not enforce SKU uniqueness. A mounted checkout may require remounting when selected items change. Do not silently carry an old cart into a new purchase.

Illustrative: one item ships to a fixed destination set at an inclusive price. The flow can work with an explicitly owned per-order supplier handoff. Contrast a store that needs multiwarehouse reservation, real-time carrier rates, split parcels or exchanges: those are separate integration requirements, not proved by stock and tracking endpoints. Creating a tracking record does not buy a label or place a supplier order. A recurring payment does not dispatch a physical renewal. Trace paid, supplier accepted, dispatched and delivered separately, then treat refund and goods return/restocking as separate decisions.

## Related work

Read [migration and coexistence](migration-and-coexistence.md) when that adjacent decision is unresolved.
