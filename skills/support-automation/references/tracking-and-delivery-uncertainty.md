# Tracking and delivery uncertainty

## When to read

WISMO means “where is my order?” It includes unfulfilled orders, stalled tracking, split shipments and delivered-but-missing reports. These require different next evidence.

## How to do the work

Join the customer’s intended order and item to the fulfillment record and carrier tracking identifier. Build a short timeline: paid/accepted order, promised dispatch, fulfillment creation, label, first carrier acceptance, latest scan and delivery event. Include observation time, event time and timezone; a freshly fetched stale scan is still stale evidence. Mark missing data instead of guessing.

Choose the next discriminator:

- No fulfillment record: identify the dispatch owner and applicable promise; investigate release/stock/payment hold with that owner.
- Label without acceptance: ask fulfillment for evidence of physical handover. A saved tracking field proves an attachment, not movement.
- Movement then silence: inspect carrier status and service-specific investigation process. Do not create a universal “lost after X days” policy.
- Split shipment: map each item to its own package and show what remains outstanding. One delivered parcel does not complete the order.
- Cross-border parcel stops updating after an export or destination-arrival scan: the destination carrier may be carrying it under its own number. Ask the supplier or forwarder for the handover number before calling the parcel lost.
- Late against the window shown at checkout, not against carrier norms: the customer is right that the promise was missed even if the parcel is moving normally. Answer the missed promise with an acknowledgment, an honest new estimate and the remedy the policy allows, and send the window itself to whoever owns the delivery copy on the product page.
- Delivered scan but buyer has no parcel: acknowledge the discrepancy and use the applicable delivery-investigation path. A carrier event does not establish customer possession; neither does a complaint alone establish loss.

Draft an explanation grounded in the last confirmed event, the next investigation and available policy remedy. If the next update time is unknown, do not invent one; arrange an owned check and communicate it once accepted. Keep supplier investigation with fulfillment while support retains the customer follow-up.

## Worked decisions

Illustrative: a bundle has one delivered parcel and a second label with no collection scan. A generic “delivered” macro would dismiss half the request. Explain the split, investigate the uncollected portion and evaluate remedies per affected item. Refunding the full order may exceed the actual obligation; insisting everything arrived ignores the split.

A customer asking only for the tracking link may need a concise answer. Do not launch a carrier dispute if current movement and the requested link resolve the question. Conversely, a late-gift complaint is a request about the missed promise, not merely a need for the same link again.

## Deliverable and checks

Return the relevant timeline, a useful response draft and an internal handoff containing the missing evidence, owner and next check. Use [remedy authority](returns-and-remedy-authority.md) when the customer requests compensation; do not equate an investigation with a refund authorization.
