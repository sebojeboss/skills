# Editable handoff and preservation

## When to read

Read when organizing what the owner will edit, handing over source, promising editing tasks, changing an existing site, or explicitly planning migration or Blueprint portability.

## Design the editing surface the owner will use

Unless you have demonstrated an in-dashboard editor for this site, the owner's editing interface is the code. Make it easy to use:

- Put the values the owner will change most in one small, clearly named content/config module, separate from component logic. These are typically headline and subhead copy, hero and product images, palette roles, section order, and which product each card sells.
- Keep product identity (`resourceId`, plan or variant) apart from presentation overrides in that module, so changing a card title cannot change what is bought.

Prove the handoff the way the owner will use it:

1. Recover the uploaded source into a fresh directory.
2. Change one headline and one image.
3. Build and upload a preview.
4. Confirm the price and buy action did not move.

A "has source" flag on a build is weaker evidence than that round trip. Whether the dashboard offers in-UI editing is a separate observation; claim it only if you used it. Source-file editing is a valid handoff, but do not describe it as a no-code merchant interface.

Choose the smallest understandable editing surface. A fixed-placement component with editable values can beat unrestricted composition when the page depends on a tight relationship. Conversely, a growing list should not require adding `title2`/`image2` fields forever. Explain the sacrificed freedom or complexity in the owner guide.

## Trace every promised edit

For each recurring edit, write the chain: owner-facing task → persisted value → renderer → dependent asset or loader → verification.

- A label is not the stored setting ID.
- If a control exists but does nothing, trace the chain before adding another control.
- If editing one card changes both, inspect shared selectors and state ownership.

Use the recovered-source round trip above to test this chain: reload after saving, check the changed field and an unrelated price or action, then restore the intended content.

## Changing an existing site

First ask whether a formerly custom feature is now supplied by the destination. Preserve the useful behavior, not every obsolete patch.

Map what the current site depends on:

- implementation files and their inclusion points or loaders;
- saved content and settings;
- catalog state;
- external app UI and backend dependencies.

A file can survive an update while its loader line disappears, leaving a feature silently dead. A preset or starter template does not preserve the merchant's saved values. Do not overwrite one configuration file on the assumption that it contains the entire store.

When an owner may be editing during the work, keep a base/local/remote comparison before overwriting configuration. Choosing a conflict winner is not reconciling two intended changes.

A same-platform update, a cross-platform migration, a source clone and a platform business copy are different operations with different dependencies. Definitions may need to exist before values and references resolve. Inspect per-item import results and unresolved references, and do not delete source data as a shortcut. No source-code rollback can reverse a payment or recreate catalog changes.

For an explicitly requested Blueprint, verify the destination-owned source, catalog, configuration and copy behavior separately. A normal site deployment does not prove portability. Keep source recovery, build reproducibility and owner use as distinct evidence.

## Worked decisions

Illustrative: an owner changes copy during a redesign. Reconcile that field with the intended new component rather than replacing the whole configuration. A cross-business source copy must separately bind new product identities.

## Deliverable and checks

Use the [owner handoff](owner-handoff.md) to record:

- the delivered state and source location;
- the preview or live identity;
- the tested edit round trip;
- recovery limits and remaining dependencies.

Identify which changes require source editing and which were demonstrated in a merchant interface.
