# Component reconstruction

## When to read

Read when implementing reusable layout or behavior, diagnosing geometry, rebuilding a widget that displays store facts, or deciding how content should be edited.

## Build from rules, not offsets

Derive intrinsic sizing, grid/flex constraints and breakpoint changes before adding any offset. Build in this order:

1. The outer layout: content width, gutters, columns, intrinsic media ratio and stacking.
2. Type measures and component spacing.
3. Borders, shadows and motion.

Recheck after real content arrives. Placeholder lengths and aspect ratios are not stable requirements.

When geometry is right at one width and wrong at another, inspect the crossover. A breakpoint may change a rule, or the same rule may resolve differently because text wraps, media height changes, or a min/max constraint takes over. Identify the containing block and encode that relationship; test just above and below the crossover.

Reconstruct semantic buttons, tabs, drawers, focus return and reduced-motion behavior from observed requirements. For a layered control, separate the outer hit area, visible face and label before implementing hover or press movement. Use the [source inspection](reference-inspection.md#read-the-files-behind-the-component) route when state belongs to JavaScript. Record deliberate improvements to source faults. Do not reproduce the reference's broken focus or mid-word wrapping.

## Component contracts

Give each component explicit inputs, render consumers, defaults, optional-content behavior, placement, resource identity and per-instance values. A useful contract names `resourceId`, optional presentation fields, state and edit location.

Keep the selected catalog resource separate from title and image overrides, so an alternate title never silently changes the product being purchased. Resolve an empty override to catalog content. If both images are missing, render an intentional text layout rather than a broken image. Never render an empty link or borrow another card's image. Bind the buy action and the price from the same selected resource.

Put shared structural rules in component CSS, with per-instance custom properties on the instance wrapper. Keep one ordered list when the editor promises free reordering. If products and collections deliberately occupy separate zones, expose and explain that grouping rather than presenting a misleading single order control.

For interaction, use semantic buttons and explicit state. Initialize on mount and clean up listeners on unmount or replacement; an editor refresh may not rerun page-load code. Test two instances, then remove and reinsert one. A shared listener or selector can otherwise make one instance control its sibling. Platform-specific editor hooks need that platform's current contract.

## Native, constrained or custom

For every difference between the reference and what the destination already does, choose deliberately. Reuse a supported native behavior when it supplies the interaction and its future maintenance. Accept a native constraint, such as a named spacing scale or a stock icon set, when exact fidelity is worth less than an easy update path. Build custom only when the user's actual requirement outweighs the maintenance cost: every custom control the owner will edit is code someone must keep working.

A one-store modal can rely on a known theme. A portable component must either remove that dependency or declare and verify it. Exact visual fidelity is not a reason to hide an unmaintainable dependency.

### Choose the shopping interaction

Use a quick-selection panel only when it can supply real option, availability and quantity states; otherwise keep the product-detail route. [Reference inspection](reference-inspection.md#critique-the-reference-before-you-measure-it) explains the shopping tradeoff.

A theme's existing product modal might supply those states cheaply on one known site. Depending on it in a portable component creates a hidden requirement: markup, events, cart counter and overlay behavior may all belong to that theme. Either declare and test the dependency, or build a small explicit panel. An opening animation that works does not prove independence. Check the selected variant, close/focus behavior, cart update and owner editing separately.

## Components that make claims

Some reference widgets assert facts about the store:

- rating stars and review counts;
- "bought recently" lines;
- ship-by or delivery dates;
- stock and reservation countdowns;
- compare-at prices;
- delivery and guarantee badges.

Rebuilding them as layout copies a statement along with the pixels. Rebuild the layout, and bind each one to its real owner:

- ratings and counts come from actual reviews;
- a ship-by date comes from the supplier's evidenced preparation time and cutoff, not a fixed number of days added to today;
- compare-at needs a real reference price;
- delivery wording comes from the route actually used.

Render these components only from real store records. A countdown that restarts on every visit, or a date computed without dispatch evidence, turns a faithful reconstruction into a false statement. That is an offer and support problem, and a visual task has no authority to create it. Supply dates and delivery promises from sourcing-and-fulfillment evidence; the offer owner decides whether the claim belongs on the page at all.

## Worked decisions

Illustrative: a two-card section has three problems. Its heading control is never rendered. It uses two loops that defeat sidebar order. A shared CSS rule repaints both cards. Connect the field to its consumer, render the declared order and scope the instance styling. Then exercise a missing image and long content.

Illustrative, with invented numbers: a product-card caption band was rebuilt at a fixed 220px because that is what the reference measured at 1280px. Below about 960px the band started covering the product. The reference actually used the smaller of 220px or 38% of the card's height, and card height followed the image's aspect ratio as the grid dropped from four columns to three. Checking just above and below the column change, at say 1000, 940 and 900px, exposes the crossover. Encode `min(220px, 38%)` against the aspect-ratio-driven card height, not a new offset tuned for one width.

## Deliverable and checks

Deliver the original editable components and their content and state contracts, including the data owner of every claim-bearing widget. Verify the promised order, resource fallbacks and per-instance edits. Use Shopify sections, blocks and presets to understand a Shopify source's structure; do not assume Whop supplies the same editor API.
