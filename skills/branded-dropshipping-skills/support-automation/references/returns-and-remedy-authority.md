# Returns and remedy authority

## When to read

Use for cancellation, return, exchange, replacement, cash/credit refund and exceptions. RMA is the return authorization or work record, not a payment receipt.

## How to do the work

Answer four questions separately: is this order/item eligible; who may grant an exception; which processing event releases the remedy; and what prior remedy changes the remaining obligation? Capture product, condition, purchase channel, market and relevant dates. Distinguish merchant error, faulty goods and buyer preference rather than placing every size problem in one policy bucket: a warehouse picking error, a missing size chart and a buyer who changed their mind call for different fixes.

Ask only for evidence needed to make the decision. Photos can inform review; a required upload does not automatically verify authenticity or establish fault. Offer the policy-supported choices in plain language, including conditions that matter to the buyer. Explain where an exception request goes instead of inventing keep-item permission.

The merchant defines action limits: currency, amount, item scope, permitted remedy types, exception role and release conditions. A cap alone is insufficient. Do not assume cash, gift cards, store credit and replacements share a platform-wide ceiling. Read previous remedies across systems before proposing another. Keep financial authority separate from a support agent's ability to edit a ticket.

Cancellation needs current fulfillment evidence. "Unfulfilled" in a store can lag warehouse or supplier processing; check whether the parcel can still be intercepted. If it cannot, offer the applicable post-dispatch route rather than promise cancellation. Refund and cancellation can be separate effects; confirm each.

## Check the payment before money moves

Before proposing a refund, replacement or credit, look at the payment itself: is there an open bank inquiry, chargeback, dispute alert or platform resolution case? Each changes which route is safe.

- **Open bank chargeback.** Check the disputed amount and its actual debit in the payment records. A separate goodwill refund can return money twice, can fail or stay pending, and can leave the order looking unrefunded while the dispute debits the store. [Stripe's dispute process](https://docs.stripe.com/disputes/how-disputes-work) debits the disputed amount and prevents an outside refund while the dispute is open; read the provider's rule for this payment before choosing a route. Pass the case to whoever answers the dispute.
- **Dispute alert or pre-dispute refund service.** The alert may already have refunded the buyer automatically. Check before adding a second refund.
- **Platform resolution or buyer-protection case.** The platform may expect the refund to be issued inside the case, where it also closes the case. Use that route when the provider supports it, rather than a separate refund that leaves the case open.

If a customer offers to withdraw a chargeback in exchange for a refund, record the offer and pass it on. A withdrawal request is not a closed case, and the refund route then depends on the provider's dispute rules, not on the support macro. The customer still deserves a plain answer about what you can see and who will reply.

## Support can take the reason for a dispute away

A buyer who knows what is happening, recognizes the charge on their statement and can see a remedy has less reason to go to their bank. When a buyer is unhappy, say plainly what happens next, which name will appear on their card statement, and every remedy the policy actually allows.

If the store is already close to its processor's tolerance for disputes, requiring a buyer to ship back a low-value item can cost more than the item if the disagreement ends in a chargeback; a returnless or partial refund may be the smaller exposure. That call belongs to whoever holds refund authority. It is not a default the support agent may grant.

## Worked decisions

Illustrative: ordinary returns release a refund after warehouse validation, while a documented faulty-item exception releases it after a carrier acceptance scan on the return. Waiting for the warehouse in both cases defeats the exception; refunding every ordinary return at label creation bypasses the policy. Preserve the tradeoff: faster release accepts a different exposure and needs explicit authority.

Illustrative: a returnless replacement is allowed only after team-lead approval. Prepare the facts and proposed remedy for that lead. Warm wording or a previous unrelated exception does not extend the permission to this order.

## Deliverable and checks

Produce the eligibility decision, policy/version, authority, release evidence, prior remedies, payment dispute state and the proposed next step. In draft-only mode call it proposed. After an authorized native action, record the provider result and customer communication separately. Follow [partial failure](partial-failure-and-reconciliation.md) on any uncertainty; physical inspection/restocking belongs with fulfillment and is not proved by a refund.
