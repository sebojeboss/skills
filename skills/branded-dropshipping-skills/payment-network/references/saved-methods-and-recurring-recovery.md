# Saved methods and recurring recovery

## When to read

Read when saving a method to charge later, diagnosing a failed renewal or ineffective retries, or charging after purchase with consent.

## How to do the work

Inspect consent, intended usage, customer attachment and the actual method selected by the subscription or invoice. Follow one failed renewal from scheduler to submitted attempt to provider result; do not infer that each scheduled retry reached an issuer. If the method needs buyer authentication, construct the supported buyer return path; if the wrong default is selected, repair that specific selection rather than repeatedly retrying the same unusable method.

For Whop, when the payment is recoverable and its authorized read returns a recovery link, use that existing-payment route for the buyer's authentication. Follow the final payment result before treating the obligation as paid. Check whether the platform already sent a notice so the buyer receives one coherent sequence. A stored method or recognized email alone does not authorize a new charge.

Saving without a first payment and saving during a payment are different setups with different consent records. Credit a recovered renewal to the buyer's action or to the retry only with the executed-attempt record. Use the current provider documentation for exact method and SDK names; copied tutorial syntax goes stale.

## Worked decisions

Illustrative: a customer updates the default payment method, yet a subscription still names its older method. The scheduler reports repeated retries but no new charge reaches the issuer. Inspect subscription/invoice precedence and executed attempt IDs before interpreting scheduled counts as failures. Repair the effective selection, then use the provider's allowed recovery path.

Saving credentials and consent are separate. Record the permitted future use and customer association; a setup object succeeding does not collect money. Off-session describes the buyer's absence during an attempt, not exemption from authentication. When a later attempt requires customer action, provide the supported return URL and resume the same obligation after completion. Do not loop blind attempts or send outreach without the user's authorized channel and scope. Hard/soft decline classifications and automatic retry rules are provider/product specific; the label alone is not an instruction to try a second processor.

## Related work

Read [payment state and safe recovery](payment-state-and-safe-recovery.md) when that adjacent decision is unresolved.
