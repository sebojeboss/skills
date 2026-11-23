# Reconcile outcome and cash separately

## When to read

Use for negative balances, partial refunds, provisional credits, reported wins or final recovery claims.

## How to do the work

Build the money timeline from account-scoped event IDs and actual source records. Use signed balance deltas in explicit minor units and currency. Mark requested/ordered/pending amounts separately from posted movements. Identify principal, dispute debit/return, provisional credit/reversal, refund, fees and independent reimbursement. Keep provider and bank receipt distinct where both matter.

Ask what event created a credit. Depending on network and stage, a merchant can be credited when a first-cycle response goes in and debited again if the issuer rejects it, or submission can return nothing until a decision. The case result and the money can disagree for weeks. A provisional credit can be reversed; a won case may retain fees; a seller-protection or carrier reimbursement can coexist with a lost chargeback. An order to reimburse is not a ledger entry. Do not infer settled money from a status label. Do not net currencies without a documented conversion event, or treat missing cost as zero.

Follow [reconciliation checks](evidence-files-and-checks.md) using the provider’s actual export. Count identical event identities once, investigate conflicting duplicates and keep unknown/unmatched records visible. Total posted changes by currency and category, then compare with statement boundaries, export coverage and later fees. Do not infer completeness or final recovery from a balanced subset.

## Worked decisions

Illustrative: a 75-unit dispute debit is followed by a 75-unit provisional credit and its 75-unit reversal. A separate 75-unit reimbursement has been approved but is not posted. Net observed movement is still minus 75 before fees; the approval is a pending remedy, not recovered cash. Once the reimbursement posts, the balance trace changes, while the original chargeback result need not change.

For contest economics, exclude already-paid fees from the incremental choice but include them in final net recovery. If expected recovery needs a probability, use an explicit uncertain scenario; do not borrow a vendor-wide win rate for this case.

## Deliverable and checks

Return observed principal and fees, unmatched/unknown entries, time coverage and separate case result. Do not call a balanced subset a complete account reconciliation. Reserves, whole-account payouts and treasury decisions belong to the payment/account workflow.
