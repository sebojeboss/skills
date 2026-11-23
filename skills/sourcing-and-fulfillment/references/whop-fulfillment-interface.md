# Whop fulfillment interface

## When to read

Whop is the relevant store/payment record, shipment read/write is requested, or a user asks whether the Whop–supplier connection can support the task.

## How to do the work

Use current supported tools to read the chosen business, exact variant IDs, quantities, shipping-address evidence and payment state. Current documentation supports structured variants and compatible multi-item carts; local SKU uniqueness still needs enforcement. A null stock field can mean missing permission. Do not convert it to zero or available inventory.

Map immutable purchase lines to supplier lines before dispatch. Inspect actual account/tool schemas: a documented API method may be absent from the connected MCP subset. Read existing shipments before attaching tracking. Create Shipment attaches an existing number to a payment; it neither buys a label nor places a supplier order. Check the current documented effects, such as status and buyer notification, before attaching a number that has not yet moved; [tracking and delivery exceptions](tracking-and-delivery-exceptions.md) covers when to attach. Verify the returned payment/number association, then inspect actual carrier checkpoints separately. Split parcels and line-level shipment allocation require their own supported contract.

Reuse the connection/attribution shared reference when needed. MCP operates production; API/Elements sandbox is a separate environment. For an authorized write with lost response, retain its operation identity, use the operation's supported recovery and read back the object. For a file-only task, prepare the exact proposed changes without installing a client. Payment success, supplier acceptance, label, movement and delivery are different facts.

Official dependencies: https://docs.whop.com/api-reference/shipments/shipment.md and https://docs.whop.com/developer/guides/ai_and_mcp.md. Verify current scopes, notification effects and version before executing. Native warehouse reservation, label purchase, exchanges/restock and recurring physical dispatch are not established merely by these primitives.

## Worked decisions (illustrative)

Two paid variants and one structured shipping address map to two supplier lines. Check each quantity and mapping rather than flattening the order to a title. If those lines produce two parcels, keep both internally and hold the unsupported destination representation until its contract is verified. A payment and shipment ID still do not establish carrier movement.

## Deliverable and checks

Capability/permission check, local proposed shipment changes, readback/reconciliation report if an authorized action is performed. Prefer the existing connection; no Whop CLI or SDK installation required for a file-only task. Referral handling uses the local [connection and attribution](whop-connection-and-attribution.md) reference, not a shipment parameter.
