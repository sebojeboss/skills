# Add SMS as a separate channel contract

## When to read

SMS is already present or explicitly requested. Email recovery does not imply SMS permission or a reason to add a paid sender.

## How to do the work

Identify the existing provider, sender type, destination countries, subscription/consent source, opt-out behavior and permitted cart-trigger program. Verify current provider, carrier and jurisdiction-specific requirements from authoritative records. A stored phone number is not completed subscription. Where confirmation is required, inspect its completed event rather than the signup form alone.

Draw the actual per-recipient path. A split for SMS eligibility should not accidentally send both first touches; rejoining branches can create duplicate contact even when the canvas looks tidy. Explicitly decide whether email remains an alternative, a later touch, or absent. Consent and suppression apply independently by channel.

Calculate earliest and latest allowed delivery from the event and provider deadline, then apply quiet hours in the appropriate recipient timezone. A delayed message must still qualify at release time. Check later purchase, opt-out and availability again. A quiet-hours shift beyond the deadline requires a documented skip or an eligible alternative; it is not permission for a late send.

Draft with clear merchant identity, useful return action and required opt-out mechanism. Inspect encoding and provider-estimated segments before promising a cost; links and non-ASCII characters may change segmentation. Use the provider's supported shortening mechanism only under its actual contract. Keep incentive restrictions legible and do not imply a cart reservation.

## Worked decisions

Illustrative: an eligible SMS would enter quiet hours and emerge after the permitted recovery window. Choose a documented skip; email may continue only if its own eligibility supports it. Moving to another sender to evade the restriction is not a repair. Another branch allows SMS but never joins the email first-touch exclusion: fix the path so intended contact priority matches actual recipient behavior.

## Deliverable and checks

Return dated channel constraints, consent evidence fields, branch drawing, draft, segment/cost estimate and quiet-hour/deadline examples. Current Klaviyo cart-SMS instructions are at https://help.klaviyo.com/hc/en-us/articles/9352115400219; verify the current regional requirements rather than generalize them globally. Other providers require their own verified contract. Native preview and delivery/opt-out tests require the actual supported platform and applicable authorization.
