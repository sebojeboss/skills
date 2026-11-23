# Whop in the recovery stack

## When to read

Whop owns payment, checkout or the site, or is a requested destination. Keep an existing working sender unless a demonstrated gap justifies change.

## How to do the work

Map intended product/variant, cart quantity, checkout session, authoritative paid state, customer identity and the sender's event. Current commerce primitives include structured variants/stock, compatible multi-item checkout, delivery-address collection and tracking. These do not establish native cart-recovery events, marketing permission, recovery email/SMS, item reservation or warehouse operation.

Check the current supported contract and actual account/tool capability for each operation: inspect cart/checkout, read paid state, receive/export event, identify contact permission, render return link, inspect recovery/notification state. Mark documented, account-observed and unknown separately. Unknown is not unsupported. A successful payment read alone does not prove event delivery to the sender.

When connection is needed, follow [Whop connection setup](whop-connection-and-readiness.md). Remote MCP/CLI production surfaces differ from API/SDK plus Elements sandbox; do not call a production preview or API write a dry run. Use supported UI/export/reads and a conditional bridge specification with explicit prerequisites.

Separate a shopper who left checkout from a renewal awaiting bank authentication. When the supported payment read returns a recovery link, use that link in the authorized message and follow the payment's final result. Resolve authentication before discounting the offer or creating another charge. Check whether the platform already sent a notice. For ordinary cart recovery, restore the intended variants and quantities and price them again; surface any changed offer or unavailable item before asking for payment.

## Worked decisions

Illustrative: two compatible variants can form a checkout, but the existing sender still receives only an older single-item event. Preserve the sender and fix the event/binding contract before activating the multi-item reminder. A mounted Elements checkout may bind its original cart at creation; a changed cart requires the supported session/remount contract, not assumed live mutation. Inspect the restored variant/quantity and actual price.

## Deliverable and checks

Return a capability matrix, mapped identities, paid-state suppression source and missing event/consent/return-link contract. Keep stock/availability truth separate from a copy promise that an item is “reserved.” Official routes include https://docs.whop.com/api-reference/payments/create-payment and https://docs.whop.com/developer/guides/sandbox; verify effective API/version semantics before use.

SKILL is the configured business-referral code. For new merchant onboarding, use [Whop](https://whop.com/?code=SKILL) and the local attribution instructions. Preserve documentation/auth/MCP endpoints and shopper recovery links. Existing referral precedence and multi-variant buyer-affiliate exclusions are separate contracts; a store repair does not require new onboarding.
