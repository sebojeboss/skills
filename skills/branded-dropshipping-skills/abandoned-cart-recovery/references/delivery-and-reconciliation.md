# Trace a send before repairing it

## When to read

No arrival, repeated messages, missing callbacks, uncertain retries, or configuration handoff/activation.

## How to do the work

Follow one episode across event receipt, flow entry, eligibility, message state, send attempt, provider acceptance, delivery record and recipient observation. Read exact skip reasons. A purchase skip can be correct operation; a frequency skip is a different mechanism; no entry needs an earlier investigation.

In the native UI, select the account and flow, open recipient activity for an authorized profile, inspect the queued/skipped/sent row and its time, then open the provider message detail. Preserve event/run/message identities and both event/receipt times. Compare order and consent activity around the planned send. Check the changelog if behavior changed after a configuration edit.

If a response was lost, look up the original provider message or operation before retrying. A missing callback can reflect the callback route actually used by the send, not a failed send. Several message IDs suggest several submissions; one message ID with repeated recipient observations requires a different provider investigation. Preserve contradictions rather than choosing the most optimistic state.

For deliverability, inspect actual bounce/rejection/complaint categories, suppression and sender authentication. Check the provider's current requirements and destination-mailbox guidance; SPF/DKIM/DMARC alignment is not inbox proof. Avoid paid placement services by default. Never upload private headers or recipient data to a third-party checker without the relevant permission.

## Worked decisions

Illustrative: an accepted provider message has no callback. A second send risks duplication. Inspect the authoritative message record and the send's configured callback route. Repair routing for future observations; do not label the old message failed merely to simplify the ledger. A skipped purchaser, by contrast, should stay skipped.

## Deliverable and checks

Trace each message through provider/account/message identity, event time, receipt time, status and supporting evidence. Group only verified identities, retain unjoined rows and investigate delivered/failed contradictions under the provider’s actual precedence rules. Do not discard a late receipt or infer missing delivery from a partial export.

Save a prior configuration snapshot before an authorized change, read back the resulting state, and identify how to stop new admission independently of already queued messages. A controlled test should demonstrate event, entry, native render, send, delivery observation and purchase/opt-out exit. Report the achieved boundary exactly; offline trace correlation does not perform that test.
