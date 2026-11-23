# Render the actual event and return path

## When to read

Dynamic blocks, imported designs, blank products, wrong currency/variant or broken return links.

## How to do the work

Start from a native template for the actual trigger or a documented field map. Reusing words and layout between cart and checkout is reasonable; reusing event property paths without checking is not. Native preview must bind the same event type used in the flow.

Build fixtures for one item, multiple variants/quantities, missing name, service-only lines, excluded item, unavailable product and absent offer. Match product image, title, variant, quantity and price to the same item. Apply exclusion logic consistently to image and text blocks, then explicitly handle the zero-visible-item result. An empty but syntactically valid email is a failed product reminder.

Inspect HTML and text output, image-blocked layout, mobile widths and CTA accessibility. Image slices can preserve design but hide text, increase loading burden and fail when images are blocked. Keep essential product/offer meaning and action available as readable text. Currency and units must match the event; do not format every amount as dollars.

Inspect every destination including logo and product images. Distinguish a homepage link from a cart/checkout restoration link. Preserve signed or personalized query strings; do not decorate recovery links with pack referrals. Test expired/changed carts only under appropriate authorized conditions, without buying. Verify the selected items and current price after return; previewing a product image does not establish restored checkout contents.

## Worked decisions

Illustrative: shipping protection is hidden from the image but remains in text. Align both filters. Then test a protection-only payload: either show a truthful generic assistance message or suppress through a documented rule. Do not fabricate a replacement product. A first-name subject repeats across episodes; product-specific subjects can distinguish episodes, but long names may clip.

## Deliverable and checks

Use the provider’s native preview with representative eligible profiles/carts. Check unresolved merge expressions, actual currency and variant text, item count, empty-cart fallback and every actionable link. Compare the rendered result with the intended message and authorized destination; literal text presence alone does not prove context, visual layout or a functioning return route.

Deliver the corrected draft, field/link map and preview matrix with native/local/inbox observations distinguished. Native render and authorized recipient tests remain necessary for those claims.
