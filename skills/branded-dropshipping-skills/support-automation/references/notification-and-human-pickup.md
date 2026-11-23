# Notification and human pickup

## When to read

Use when the buyer did not hear back, replies disappeared, bots conflict, or escalation appears complete only because the ticket changed status.

## How to do the work

Track the strongest communication evidence available: draft, submitted, provider accepted, delivered, read or buyer-confirmed. Not every channel exposes each level. Keep unsupported levels unknown. A message rendered inside a helpdesk can be an internal event that never reached the external channel.

Inspect sender identity, connector direction, event result and destination. Check whether a generic email rule includes an SMS connector, whether bot-generated events are suppressed to prevent loops, and whether closing ends the external conversation. Then inspect whether a subsequent buyer reply still reopens/syncs the ticket. Snoozing can preserve continuation where closing does not; use actual channel behavior rather than applying this universally. Avoid sending another message solely to test a live customer path without authorization.

A human handoff needs an eligible queue, sufficient context, staffed coverage, accepted ownership and a follow-up rule if pickup fails. Preserve the customer’s request, relevant order, policy decision, actions already completed and remaining obligation. Assign one substantive response owner and suppress competing automation after handoff. An exclusion that ignores a ticket may not escalate it. Confirm which behavior is configured.

## Worked decisions

Illustrative: a bot posts “Refund complete” in the helpdesk, but the connector did not forward bot messages. First reconcile the refund itself; then repair the notification path. Sending a second refund does not fix delivery. A buyer’s silence can reflect failed delivery, abandonment or satisfaction, so silence-triggered closure must retain its limited meaning.

Illustrative: a complex complaint is tagged for specialists outside working hours. An honest acknowledgment describes the staffed follow-up; a fabricated “a specialist is now reviewing” falsely implies pickup. If no staffed destination exists, show the merchant the unresolved ownership rather than claiming successful escalation.

## Deliverable and checks

Use the [handoff](../references/handoff.md) when context must transfer. Record notification state and pickup state separately from remedy state. Audit real receipt semantics before promising delivery, and use [adapter contract](helpdesk-store-contract.md) for required surfaces.
