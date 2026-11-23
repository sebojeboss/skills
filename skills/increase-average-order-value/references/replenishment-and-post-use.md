# Replenishment and post use

## When to read

Read when the offer is recurring, delayed or depends on successful use. Distinguish a tool that helps first use from stock the customer cannot consume yet. Map payment, delivery, use, depletion and renewal; an elapsed-day timer does not prove delivery or readiness. Segment a willing subscriber from a gift/trial buyer rather than forcing everyone through a better-value subscription.

Build trigger and suppression rules using available events, consumption evidence and the existing stack. State the one-time option and recurring terms plainly. A taste complaint, preparation problem or surplus stock can require different action; a price reduction does not repair every use problem. A skip may prevent cancellation or replace a paid renewal. Keep later paid orders, refunds and costs in the comparison; active subscriber counts are insufficient. Required notices remain required even when optional reminder experiments disappoint.

**Illustrative worked decisions:** a preparation tool helps first use while three extra bags create surplus; a delayed shipment invalidates a purchase-date check-in; a sample can replace the next flavor rather than expand consumption. **Output:** recurring terms, trigger/suppression table, message drafts, quantities and observation horizon. A drafted flow is not scheduled. Physical replenishment additionally needs stock, current address and a per-cycle fulfillment owner; recurring billing alone supplies none of those guarantees.

## Write the actual trigger table

Use columns: event/source, earliest eligible time, customer/product conditions, suppressions, message/action, owning tool, deduplication key, and evidence of completion. For example, a delivered first order can invite preparation help; suppress that message when delivery is disputed or the customer has an open product complaint. A depletion estimate can suggest a reorder, but an unconfirmed delivery timestamp must not silently become successful use.

Draft the relevant message, not a generic cadence: “How is the first batch working? If it is too strong, here is the measured preparation guide.” Only include preparation claims supported by the product instructions. A separate reorder message can say what will ship, quantity, next charge and how to change it. Do not fabricate health benefits or hide cancellation behind a discount.

If required delivery/use events are unavailable, produce a conditional flow specification and name the missing event. Use the existing lifecycle tool's supported preview, trigger exclusions and audience inspection. Check actual schedule, customer consent and recurrence controls before an authorized enablement. A flow draft is complete as a draft and should never be reported as sent.
