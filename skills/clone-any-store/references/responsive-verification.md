# Responsive verification

## When to read

Read when repairing a visual discrepancy, changing tokens or content, or checking whether a reconstruction is complete.

## How to do the work

A comparison means something only when both sides match on route, interaction state, viewport and DPR, scroll position, and font and asset readiness. Establish that first, and resolve any ambiguous element selection before interpreting a geometry difference.

Then compare the same semantic regions in source and target: position, dimensions, text wrapping and overflow, alongside overlays or pixel differences. Choose narrow, intermediate and wide widths, plus both sides of observed breakpoints and intrinsic/min/max crossovers. Inspect both screenshots directly. Use a local image-diff tool only when it answers the question. A zero delta can hide the wrong artwork, font, color or behavior; a nonzero delta may be an intentional adaptation. Disclose intentional changes and masks, and never hide a required control behind a dynamic-content mask.

Check that the probe measured the quantity you intend to repair. A transformed bounding rectangle is a painted box; an SVG wrapper can be wider than its fitted artwork; inline spans can produce several text rectangles on one visual line. Inspect the node structure before treating those readings as layout width or line count. No page-level overflow does not rule out a clipped child panel.

Repair in causal order:

- **The whole lower page shifts:** look for a wrapping or intrinsic-height change above it.
- **Boxes align but the text feels denser:** check the font that actually loaded, its weight, tracking and cap height.
- **Only the hover state shifts:** inspect borders, padding and transforms separately.
- **A fixed header hides an anchor:** test the destination's scroll position and focus rather than adjusting unrelated section gaps.

Fix layout, type and media causes before reaching for cosmetic offsets.

Use the construction map to predict what should change, then test it. If a percentage minimum explains a taller panel, increasing its containing block should reproduce the growth. If a module explains a hover or scroll effect, exercise that trigger and check the target and reset. Check reduced motion separately; removing animation must leave the intended static composition intact.

After a fix, replay the smallest meaningful affected set. Include long content, an empty image and two component instances where those states can occur. Test keyboard and menu behavior separately from visual snapshots. State the exact widths, browser and version, and the final artifact tested; keep the accepted baseline identified. A desktop browser at a phone width is not a physical-device run. Keep screenshots temporary and carry the useful measurements into the handoff.

## Worked decisions

Illustrative: wide and narrow views pass, but an intermediate width clips the CTA beside a long price label. Repair the row constraint and replay the affected states.

A matching closed-drawer image does not demonstrate opening, Escape, focus return or correct product content.

## Deliverable and checks

Add each checked state and its pass, fail or unknown result to the handoff. These observations do not establish universal fidelity, physical-device certification or conversion effects.
