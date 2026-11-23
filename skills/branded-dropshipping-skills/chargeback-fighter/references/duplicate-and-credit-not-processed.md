# Duplicate charges and missing credits

## When to read

Use for duplicate processing, paid-by-other-means allegations, an owed credit, or a refund that appears alongside a dispute. These are different claims sharing a need for exact transaction reconciliation.

## How to do the work

Networks classify these with their own condition codes, and one code can cover both duplicate processing and "paid by other means". Read the code and complaint on the case, then answer the factual question it asks. For a duplicate, line up both alleged charges: account, payment/capture ID, authorization, date, amount/currency, order, goods and receipt. Distinguish a pending authorization from a captured debit, repeated attempts from repeated captures, and legitimate repeat orders from duplicate processing. If the buyer claims another payment satisfied the purchase, address that payment explicitly. Two equal amounts are not enough to decide either way.

For credit not processed, identify the actual promise or entitlement, conditions, amount, payment rail and timing. Then find the refund object and its state. Requested, pending, failed, completed and reversed mean different things. A reversal may remove an original debit rather than appear as a separate credit. Store credit and outside-rail transfers are not automatically equivalent to a refund on the original payment.

Use provider trace references such as ARN, STAN or RRN when available and applicable; preserve their type and original transaction linkage. They help trace an operation, not certify a final issuer outcome. If a pending refund failed because a dispute began, inspect the current supported response path before proposing another refund. Do not solve an unclear negative balance by paying twice.

## Worked decisions

Illustrative: a 120-unit purchase receives a 15-unit goodwill credit for lateness, then the buyer disputes 120 units. “Fully refunded” is false. Show the original payment, credit and their relation, then determine whether the allegation concerns the remaining goods, the credit or authorization. Do not automatically subtract 15 from the requested response amount without checking the actual disputed scope and provider treatment.

Contrast a second dispute row caused by a later stage with a second captured charge. Count distinct payment and money events, not dashboard rows.

## Deliverable and checks

Return a transaction comparison and refund chronology, with unmatched entries. [Recovery reconciliation](refund-and-recovery-reconciliation.md) determines observed cash; [checkout debugging handoff](provider-evidence-contracts.md) addresses the mechanism causing duplicates without altering the dispute.
