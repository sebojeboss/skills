# Tracking and delivery exceptions

## When to read

Deciding when to attach tracking; importing or reconciling tracking; diagnosing label-only, "not found" or stale movement; a buyer contradicting delivery status; or retrying a tracking operation with an uncertain outcome.

## A number is not a shipment

Cross-border suppliers often issue a tracking number when they print a label or pre-advise a consolidator, days before the parcel moves. At that point:

- the carrier shows "info received" or "pre-transit";
- a tracking aggregator may say "not found";
- a store platform may not recognize the carrier at all.

What attaching that number does depends on the platform or connector. It can mark the order fulfilled or shipped, send the buyer a shipping notification, and start delivery or dispute timers that key off shipment. Read what the actual adapter does before attaching: the status change, the notification setting, and any customer-visible tracking link. Whatever those effects are, anyone who later asks for proof of shipment will see a parcel that never moved. That includes a buyer, a dispute reviewer or a payout review.

Before attaching, check two things:

- the carrier's own page shows an acceptance or first-movement scan;
- the destination platform recognizes the carrier.

When the platform or the task requires a number earlier, attach it for what it is, and keep the order's internal status at "label issued". When numbers stay unmoving past the supplier's stated preparation time, press the supplier on dispatch instead of uploading more numbers. Never offer another order's moving parcel as evidence.

## Read the chronology

Build a chronology from the carrier event time, the source observation time and the raw status. Then identify the last evidenced holder and the missing next handoff:

- **label created** suggests a number exists;
- **a pickup manifest or carrier acceptance** supports custody;
- **movement** supports transit;
- **final delivery** may still conflict with buyer evidence.

A status word alone cannot settle that conflict.

**Collection versus custody.** If collection never happened, compare the original booking or cancellation with a possible reassignment to another pickup provider. If custody already transferred, ask the holding carrier for an investigation or routing action instead of creating another pickup. A signed manifest is valuable precisely when a parcel disappears before its first scan, because it shows who took it. For a claimed attempted delivery, retain the actual buyer response and the attempt evidence. Never paste a generic buyer-ready statement as if a call occurred.

**Tracking batches.** Read the existing destination records first, preserving account, order and parcel identity. Compare each proposed value with the actual current value, and mark it unchanged, conflicting, absent or unresolved. Propose an addition only after establishing coverage and reconciling any unknown earlier write. A tracking-number match does not infer delivery or resolve carrier chronology. Use the operation's supported idempotency, and reconcile a timeout before retrying.

## Worked decisions (illustrative)

Nine orders have numbers. Four show only "info received", three belong to a carrier the destination platform does not recognize, and two show an acceptance scan. A buyer is asking where their parcel is, and a reviewer wants tracking that shows movement. Produce a parcel-state table: 2 moving, 4 label issued, 3 carrier unrecognized. Attach the two moving numbers through the supported path after checking what the adapter will send the buyer. Ask the supplier to dispatch the four label-only orders, oldest first. For the three unrecognized numbers, find out which carrier holds them and whether a recognized carrier or tracking page exists. Present only the two moving parcels as shipment evidence. Hand payment-network the counts if a payout review depends on them.

An upload succeeds for one parcel, times out for another, and a third already has conflicting tracking. Re-read the destination state: skip the identical match, reconcile the uncertain row, and hold the conflict.

## Deliverable and checks

- a tracking reconciliation table, with a proposed update only if needed;
- unresolved joins;
- the current event chronology;
- the next-action owner and a truthful operational status.

Customer communication routes to `support-automation`. Bank dispute evidence routes to `chargeback-fighter`. Payout and reserve consequences route to payment-network.
