# Payment state and safe recovery

## When to read

Read for a timeout, duplicate or unknown payment outcome, a webhook that disagrees with stored state, or a consequential payment configuration write.

## How to do the work

Anchor the trace on one logical purchase and its original request identity. Gather the provider resource, response/receipt, signed events and local order effects with timestamps; distinguish a known decline from a lost response. Recover the original outcome using the supported read/retry contract before deciding whether another attempt is admissible. Repair missing order work without charging again, and make duplicate or older event delivery harmless at the business-effect boundary.

Record the provider account, API version and key scope with each trace; a retry under a different version or key can behave differently. A 2xx acknowledgment to a webhook proves receipt, not fulfillment. Authentication can be skipped by the issuer or happen on a later buyer return, so read the provider status rather than assuming one ordered state machine.

## Worked decisions

Illustrative trace: the server submits one purchase, loses the response, receives an in-progress result on its supported retry, then sees a delayed successful event. Starting a new request with a new key during that interval can create a second charge. Retain the original account, environment, operation identity, request fingerprint and provider resource. Poll or recover through the documented contract. A database rollback cannot reverse a remote charge that already succeeded.

Separate the durable event inbox from business effects. Verify webhook signatures over the supported raw payload before accepting events; acknowledge only after durable acceptance appropriate to the integration. Track event identity for repeated delivery and purchase identity for fulfillment. Reconcile an older success notification against current authoritative state if a refund already occurred. Do not infer ordering from arrival time. Deployments must still understand unfinished recovery points created by the previous version. Test this across a deployment boundary, not only with duplicate callbacks in one process.

## Deliverable and checks

Return the payment timeline, original-operation observations and repair plan or authorized patch.

## Related work

Read [saved methods and recurring recovery](saved-methods-and-recurring-recovery.md) when that adjacent decision is unresolved.
