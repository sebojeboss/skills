# Settlement and reconciliation

## When to read

Read when deposits do not match sales, a refund, transfer, fee or FX line is unexplained, or a report looks incomplete.

## Trace the missing money

Check export coverage, overlap and report lag first. Trace orders and payments through provider balance entries and payout batches to bank records. Keep failed or returned payouts on separate bridge lines.

## Worked decisions

Illustrative batch: gross 100.00, fee -3.00 and refund -20.00 explain 77.00 bank cash when all belong to the same currency, cutoff and payout. If the input already supplies net 97.00, subtracting the processing fee again is wrong. A balanced batch can still conceal a duplicated sale and missing refund of equal value; reconcile intermediate identities and source completeness as well as totals.

For platform payments, a customer refund and a transfer reversal are separate effects. Inspect the charge owner, transfer and connected account balance rather than assume one undoes the other. For manual or instant payouts, automatic payout allocation reports may not provide a ready-made join. Preserve the unresolved mapping. A legitimate late reversal is a new journal, not a duplicate of the original. Report exception age, owner and next evidence; keep correction history instead of rewriting the source.

## Deliverable and checks

Return a balance bridge, unresolved exceptions and the source-to-result mapping in a readable table or existing accounting format.

## Build the payout bridge

Use the provider export and bank record for one stated provider/account/currency/period. Preserve event and payout IDs as strings, the source row locator and documented minor-unit precision. Match events to payouts using supported identities; do not join unrelated deposits because the amounts happen to match.

Map gross sales, fees, refunds, reserve movements and other journals once. If an amount is already net, do not subtract embedded fees again. Count an exact duplicate event once; investigate conflicting reuse of an identity. Keep unknown amounts and unmatched payouts as exceptions. One-to-many deposits need an explicit aggregation with source rows retained.

For each payout, show the expected amount from the mapped posted activity, the bank amount and bank-minus-expected difference. A zero difference establishes that arithmetic comparison, not complete reporting or irrevocable receipt.

Separate currencies and accounts; zero- and three-decimal currencies retain their actual precision. Document report coverage, cutoff, pending journals and delayed fees. Do not infer FX or reverse transfers to make a total agree. Repair the mapping using source evidence and create a new result; preserve originals and unresolved differences.

## Related work

Read [payouts reserves and account state](payouts-reserves-and-account-state.md) when that adjacent decision is unresolved.
