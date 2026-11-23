# Design system adaptation

## When to read

Read when deciding what should transfer from a reference or changing palette, type, copy length, language or media.

## Map the construction before extracting tokens

Sketch the component tree and connect each important region to the relationship controlling it. Include the governing rule or state, the original replacement component, and the width/content/interaction that would expose a wrong interpretation. Keep this compact enough to build from.

Illustrative construction map:

| Region | Governing relationship | Build decision and check |
| --- | --- | --- |
| Product stage | In-flow image ratio sets height; copy anchors to that stage | Preserve the sizing basis; change the product crop and test long copy before setting section height |
| Purchase drawer | Selected variant owns price, availability and buy action | Use one selection state; change the variant while the drawer is open and read back all three consumers |
| Inverse footer | Ink, translucent edges and shadows resolve against the surface | Adapt the paired roles; inspect alpha effects over the new background |

Find which face serves the actual heading before choosing its replacement. A loaded font can belong to a badge or another route; the computed family list can include unused fallbacks. Inspect rendered fonts when the browser supports it, plus weight and variable axes. Otherwise compare loaded-face metrics and wrapping while keeping the inference explicit. For media, use the selected responsive resource and its crop, not just the filename in the markup.

Font width changes wrapping; wrapping changes section height; section height can change an anchored panel's percentage size. Keep those dependencies together. They explain what must be rechecked when the owner changes copy or imagery.

## Extract roles from their consumers

Promote observations into semantic tokens by job, not by value. Two elements can share a hex value while doing different work, such as display ink and reading ink. Keep them as separate roles that happen to share a value. Near-equal values need a deliberate decision: merge them or keep them apart. Do not merge them by accident. Keep units, states and breakpoint context with each value, and keep foreground/background pairs together.

Start a role map with:

- canvas, surface and inverse surface;
- display, reading and muted ink;
- action and focus;
- selected and disabled states;
- success, warning and error.

For each role, note where it appears. Then work down the whole page through the footer before calling a recolor complete. Leftover source color hides in footers, gradient stops, button shadows, tinted near-blacks and hover states. Treat gradients and translucent layers as combinations over a background, not isolated swatches. A functional warning color may intentionally stay outside the brand palette.

For each candidate token, decide whether it is a reusable role, a component-local exception or an unused source observation. Trace aliases to their values and to the components and edit controls that consume them. A complete token list does not establish taste or originality; inspect the rendered result.

Transfer coupled relationships rather than the source's combined identity:

- line pitch and inline media height;
- image aspect and container size;
- font width, cap height, stroke mass and wrapping.

Choose permitted fonts against the actual longest useful text. Measure the loaded font, line count and occupied width, then look at stroke mass and rhythm. A width match alone is not a substitution. Never squash a face horizontally to force the old silhouette. If new words make the display treatment fragile, change the layout rather than adding forced line breaks that fail in another language. Keep reading copy independent from expressive display type. Test user text-spacing and zoom without turning a reading recommendation into a universal authored line-height. A grey box can validate geometry while leaving artwork mass unverified.

## Worked decisions

**When the inline image is a hint and when it is proof.** Illustrative case with invented starting values, not measurements:

A reference sets a two- or three-word claim large in a condensed face, with a small product image inside one line as if it were a word. The image works because it shows the product while staying subordinate to the claim. It is not a picture puzzle replacing a word.

Take an original claim for an insulated lunch tin, "STAYS / COLD", at a 360px viewport with 16px gutters, which gives a 328px measure. A starting candidate is roughly 64px type on a 56px line pitch, with an 84×56 image tile locked to that pitch so it moves with the text. Keep the supporting sentence in a reading face. Check the widest line in the loaded font, not the fallback.

Now change the product to a replacement phone case whose camera cutout must match the buyer's model. The buyer has to inspect the cutout, so the image can no longer sit inside a line of type, and a list of compatible models will not fit a two-word slogan. Keep the claim→explanation hierarchy, but move to readable mixed-case text. Give the cutout photo its own zone, with a caption naming the compatible models, and rebuild the grid around it.

What transferred was the relationship between claim and evidence. The silhouette and the inline-image trick did not. A recolor or token swap would never have surfaced this.

**Residue versus a bad choice.** Illustrative repair: a fresh palette looks right above the fold, but the old tinted near-black survives in the footer and button shadow. Map those consumers to the intended inverse and edge roles. If instead the footer already uses the new hue and simply dominates the page, fixing token coverage will not help: revise the color area or the palette choice. An audit and a design decision solve different failures.

## Deliverable and checks

Keep the token roles, component inventory, deliberate adaptations and exceptions with the construction map, including the content or viewport change that would invalidate each decision.
