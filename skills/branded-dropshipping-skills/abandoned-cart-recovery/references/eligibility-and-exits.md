# Eligibility, re-entry and exits

## When to read

Later buyers still get reminders; multi-item carts lose messages; repeats, incentive rules, consent or overlapping flows need repair.

## How to do the work

Write separate rules for entry, continuing permission to send and reasons to exit. Attach each rule to its authoritative source and evaluation time. Entry-only evaluation cannot protect a buyer who purchases during the delay. Include orders from every relevant checkout source; a new payment integration can otherwise bypass suppression.

Separate help from incentive eligibility. “Never ordered” can reserve an acquisition discount. “No order since this episode began” can stop reminders after purchase. A repeat buyer can remain eligible for product help without receiving a first-order offer. Channel permission must be supported by actual consent/eligibility evidence, not merely a known address or phone.

Define the episode policy: keep the first cart, replace with latest, or re-enter after a documented interval. Inspect both sides of replacement: cancellation of the old run AND admission of the new run. A no-later-add rule can remove stale messages but suppress everything when re-entry blocks the replacement. A checkout-start exit serves a different purpose: moving a shopper from cart to checkout recovery without overlap.

Before every planned send, account for later purchase, opt-out/suppression, eligibility changes and relevant service escalation. A support reply can justify pausing persuasion while a person resolves the issue. State who monitors replies and how the pause is applied; a pretend personal sender with an unmonitored inbox is not assistance.

## Worked decisions

Illustrative: add A at 10:00, add B at 10:02. The old run exits, and a recent-entry guard denies the second run. Fix the combined episode/re-entry policy; deleting purchase suppression to improve send counts would be the wrong repair. Conversely, two admitted runs without cancellation can create duplicate reminders.

## Deliverable and checks

Create entry, send and exit rows with the rule, source, evaluation time, observed fact and reason it passes, fails or remains unknown. Translate the actual platform’s AND/OR groups and precedence faithfully; do not substitute a universal rule structure. Check purchase, opt-out and other applicable exits before interpreting admission or send eligibility. Missing facts and empty requirements are unresolved, not automatic permission to send.

Establish the facts from independently inspected snapshots and native recipient activity. Verify time windows, source timezone and the actual filter language. Preserve the timeline beside the result: present eligibility does not prove what the scheduler knew at a past send time.
