# Shopify cart and native recovery

## When to read

Shopify owns the cart/checkout or native recovery. An external sender may still own messages.

## How to do the work

Identify whether the task concerns native recovery or events forwarded to another provider. In the authorized admin, inspect the abandoned checkout's contact, items, shipping/payment state and recovery history, then the relevant automation/notification configuration. Match the completed order separately; a dashboard total is not an individual exit.

Inspect the current eligibility/non-send explanation before changing copy or filters. Later purchase, missing usable email, unavailable items, unsupported destinations or payment risk/failure can have different remedies. Check the current native mechanism in https://help.shopify.com/en/manual/promoting-marketing/create-marketing/abandoned-checkouts; do not transfer every native rule to an external provider.

For an external sender, inspect the integration's actual cart/checkout and completed-order metrics and identity behavior. Compare event fields with template bindings and the intended return path. Keep both the native and external flow owners visible. A historical CSV export suggestion does not establish current automatic sync or permission to market to imported contacts.

## Worked decisions

Illustrative: an abandoned checkout cannot ship to the entered destination. A stronger subject line does not make that order fulfillable. Route the shipping defect to checkout/fulfillment work and keep recovery truthful. Conversely, a later completed order explains a proper native non-send and should not trigger a workaround.

A second sender can expand event coverage but also duplicate reminders. Map cohorts and existing send ownership before enabling it. Disabling native recovery without checking what the external flow covers can create a gap.

## Deliverable and checks

Return native status/evidence or an external-event mapping, notification ownership and a bounded change table. Render the actual variants/quantities and inspect current return-link state under authorized conditions. Provider access/plan/export contracts must be verified for the account. Use supplied exports if live inspection is unavailable; label absent UI and delivery verification.
