# Shipping, tax and discounts

## When to read

A rate is missing, a coupon is refused or stacks wrong, a free-shipping message disagrees with checkout, or two stages show different payable totals.

## Missing rate

Build the smallest eligible-rate case. It needs:

- destination and postal region;
- origin and shipping profile;
- package weight in real units;
- product exceptions;
- the subtotal basis the rate rule reads;
- currency and any active discount.

Look for gaps between brackets and a missing open-ended top bracket (an "end rate"). A discount can push a cart into a gap, and a large order can fall off the top. A country listed in the shipping menu does not prove a rate exists for this region and product.

Where the platform lets you add a manual rate in a test environment, a temporary flat rate separates rate configuration from carrier calculation. If the flat rate appears and the carrier rate does not, look at carrier origin, packaging and account before blaming the cart.

Before interpreting the result, confirm the installed platform's current rules, because they differ and they change. On Shopify, check the current shipping help for three points that often decide these cases:

- which subtotal price-based rates read (it has been the discounted subtotal before tax);
- how a product with no weight is treated (as weightless, which can land it in the wrong tier, rather than blocking rates);
- whether an abandoned checkout keeps the rates it was first given. If so, test every change on a newly created checkout.

On WooCommerce, check how the installed version applies coupons relative to tax and shipping, and whether free shipping tests its minimum before or after coupons. That last point is a configuration choice. On any other stack, read its current documentation and the actual settings rather than borrowing these.

## Discount refused or stacked wrong

Learn the platform's order of operations and combination rules before calling anything a bug. Confirm the current rules on the installed stack. Shopify's discount-combination help has described this order: product discounts, then order discounts, then shipping discounts. Under it, several percentage order discounts are each taken from the relevant subtotal rather than compounded, and two discounts combine only when each permits the other's class.

Under such rules, an automatic free-shipping discount that "never shows" may simply be blocked by an order discount that does not allow combination with shipping discounts. Correcting that setting is a configuration repair, so retest with the other discount still present as a control. A refusal to combine can be the configuration working as set.

On any platform, do not swap a shipping discount for a cart discount to make something work without checking thresholds. The lower subtotal can drop a near-threshold basket below free shipping and make checkout cost more. Changing fixed-coupon economics just to pass a test is an offer decision.

## Thresholds and currencies

A free-shipping progress bar can be wrong while checkout is right. Changing checkout configuration to match the bar would damage the authoritative rule. Read the configured threshold source as well as the displayed currency. Converting the cart total and converting the threshold are different repairs, and only one matches the rule object. Compare before-discount and after-discount thresholds explicitly. Test immediately below, at and above the intended threshold, at exact currency precision.

## One cent and tax

For a one-cent discrepancy, build a stage table:

- per-line base and line discount;
- tax base;
- line or subtotal rounding;
- shipping;
- the payment-create amount and the later capture amount.

Locate the first divergence. Do not apply an arbitrary tolerance. Rounding per line and rounding the subtotal can legitimately differ; the question is which stage the provider receives.

Separate amount correctness from invoice allocation and presentation. A mixed-rate basket can compute the right tax while an invoice shows a blended effective rate for shipping. Preserve the governing tax configuration, and get jurisdiction-specific authority when legality is the question. Arithmetic is not a tax determination. Preserve failed interventions and partial closures in the record.

## Worked decisions

Illustrative: converting the subtotal fixes one currency mismatch but leaves a free-shipping bar wrong, because the bar reads another market's threshold. Repair the threshold source and keep a below/at-threshold control; changing display text is insufficient.
