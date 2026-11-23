# Partial failure and reconciliation

## When to read

Use when an action errors, a response is lost, two tickets request the same remedy, or a record appears closed despite an unresolved obligation.

## How to do the work

Stop automatic replay of the whole workflow. Preserve the request identity and inspect each step and item: intended outcome, destination, request time, provider result, authoritative current state and remaining obligation. An action may stop after an earlier step succeeded. “Failed” at the workflow level is too coarse to decide what to repeat.

Read payment refunds, store credits, gift cards, replacement orders and return history where relevant. Keep amounts in their explicit currencies and units. A zero-dollar bookkeeping entry is not another cash refund. A pending refund is not a failed refund; a closed RMA may still allow credit creation. Compare like outcomes without treating credits as proof of cash returned.

Join by scoped provider/account/order/item/remedy identity. Duplicate webhook delivery is different from two tickets requesting one remedy. Conversely two valid partial refunds on one order must not be collapsed by order ID alone. A local journal can record intent and observations but cannot lock another operator’s dashboard or guarantee remote exactly-once behavior.

When a write times out, retain unknown state and use the provider’s supported lookup/recovery contract. Do not generate a new idempotency key or use another payment path just to make the error disappear. If current state cannot distinguish completion from absence, escalate with the operation details and avoid another monetary effect. Record the remaining customer obligation even while execution is unresolved.

A refund that is still pending when a chargeback opens can fail or be blocked, and the store may then see both a dispute debit and a refund that never completed. Read the dispute state and the provider's refund record together before issuing any replacement remedy; the answer may be to respond to the dispute rather than to refund again.

## Worked decisions

Illustrative: refund step succeeds, notification step fails. Re-read the refund record; if confirmed, repair only the missing communication. Repeating the refund-plus-reply macro can issue a second remedy. If the provider only accepted the refund asynchronously, say “submitted/pending” rather than “received by your bank.”

Illustrative: a multi-item exchange completes one replacement but another is out of stock. A provider-specific “process outstanding items” command may be safe only within its documented contract. Do not generalize that behavior to a full workflow retry or another return platform. Offer the affected customer a supported alternative for the unresolved line.

## Deliverable and checks

Deliver a table of each effect: proposed, attempted, pending, confirmed, failed or unknown, with its evidence and time. Those are local descriptive labels; preserve the provider’s actual status too. Name only the recovery steps justified by the observations. Use a local table plus the native records. See [notification](notification-and-human-pickup.md).
