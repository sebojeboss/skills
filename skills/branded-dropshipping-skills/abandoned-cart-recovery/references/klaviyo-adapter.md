# Work with the existing Klaviyo account

## When to read

Klaviyo is the selected sender. This is an operation-specific native UI/export route, not a connected API implementation.

## How to do the work

Open the authorized account in an available browser. Open the relevant flow, inspect its exact trigger metric/integration and filters, then recipient activity for a permitted profile. Compare Added to Cart with Started Checkout; the label “abandoned cart” may cover either. Inspect the actual order source used for continuing suppression, including additional checkout sources. Check whether native commerce recovery is also active.

Open the message status and recipient reason: Draft, Manual and Live have different queue/send behavior. Inspect event occurrence and receipt time when a metric is populated but no flow entry occurs. Verify current metric-trigger lateness and transactional distinctions in official documentation; do not assume historical delays remain current limits.

Use native event preview for dynamic blocks and checkout/cart return fields. Reuse creative only after rebinding to the actual trigger. Export or record a configuration diff where the account supports it; no generic draft-write or flow-export API is assumed.

Smart Sending is a proprietary frequency feature. Its skipped messages are not automatically rescheduled, and channel windows must not be treated as one cross-channel cap. Disabling it prioritizes recovery over a contact-frequency guard; decide based on the complete contact program, not a tutorial default. Read recipient activity to distinguish this skip from purchase suppression.

## Worked decisions

Illustrative: a campaign precedes a recovery email, which is skipped. Extending the delay might change relevance; disabling the guard may increase contact. Preserve the merchant's chosen priority, then compare actual outcomes rather than calling every skip a bug. A later buyer failing continuing eligibility should remain excluded.

## Deliverable and checks

Provide before/after settings, exact metric identity, sample recipient decisions, native previews and remaining tests. Saving drafts, test sends and activation disclose different data and have different effects. On response loss, inspect the existing resource before repeating a write.

Current contract routes: https://help.klaviyo.com/hc/en-us/articles/115002779411 (cart setup), https://help.klaviyo.com/hc/en-us/articles/12278373016603 (metric flows), https://help.klaviyo.com/hc/en-us/articles/115002779311 (Smart Sending). Verify effective account/version behavior before implementation. SMS additionally loads its own contract. With no account access, supplied exports and a manual-ready change table remain useful.
