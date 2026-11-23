# Order readback and closure

## When to read

The order, email, invoice or fulfillment record differs from the cart, or a repair needs persisted-state proof.

## How to do the work

Choose the artifact that answers the question:

- **cart state** proves selected contents;
- **a payment record** proves its own provider state;
- **order lines** prove recorded merchandise;
- **fulfillment lines** describe a particular shipment.

Record the actual account, entity and mapping used between them. Name the platform and the stage before you join on any identifier. For Shopify Ajax, distinguish the variant ID from the current line-item key and 1-based line position. For Storefront GraphQL, distinguish CartLine.id from merchandise.id. Read checkout and order-line identities from their own API contracts rather than assuming a cart identifier survives between stages. Where a connector is absent, use an authorized dashboard view or local export. Do not manufacture an order to obtain a readback.

Read quantity at the object whose state you are measuring. Illustratively, a ten-unit order shipped as three and seven has fulfillment lines of three and seven. A query that traverses from each fulfillment line back to its order line reports ten twice, and that is not duplicate shipping. "Remaining to fulfill" answers yet another question.

For each expected component and loose line, compare quantity, price basis, currency and relation.

For a shipping-address fault, locate the first missing stage: input, persisted order, template variable or receiving system.

- A blank printed address with correct stored fields calls for template repair.
- A populated custom text field does not necessarily populate the structured delivery address.
- Keep shipping and billing apart in the question you ask. A shipping correction answered with billing-address rules solves a different problem; preserve the merchant's correction rather than the misdirected answer.

**Closure by behavior.** Write closure per behavior, distinguishing these labels:

- failing case reproduced;
- patch proposed or applied;
- isolated regression passed;
- deployed observation available or missing;
- partial closure;
- administrative closure.

Keep a still-broken title open even when the address now renders. A provider release note or a ticket closed for inactivity is context, not a retest. When the receiving system disagrees, hand the correct persisted units and address to fulfillment. Do not infer dispatch or delivery from payment success.

## Worked decisions

Illustrative, with invented numbers: a bundle sells a 25-unit pack for $11.86, which does not divide evenly into cents per unit. An order for two packs arrives with the component split into 22 units at $0.48 and 28 units at $0.47. Before calling it a duplicate or a loss, add it up: 50 units and $23.72, both rows under the same parent, which is exactly two packs. The split is cent allocation, not missing merchandise.

A warehouse complaint about "eight picks instead of one carton" is a different problem. Merging rows into one line of quantity eight still describes eight units. Whether the warehouse picks a carton depends on the parent/component mapping it receives and its own case-pick rule. That is a fulfillment handoff, not a checkout repair.

Illustrative: an address-template correction passes while the line titles in the same document remain wrong. Close the address behavior and keep the title behavior open.
