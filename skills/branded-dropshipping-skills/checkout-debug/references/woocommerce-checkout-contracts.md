# WooCommerce checkout contracts

## When to read

The merchant uses WooCommerce and its checkout or gateway extensions.

## How to do the work

First record what is installed:

- WooCommerce, gateway and extension versions;
- the theme;
- block or shortcode checkout.

Identify the hooks that compute totals, create or patch the payment, handle capture and process return navigation. Use the installed plugin documentation and the official developer documentation at https://developer.woocommerce.com/. An old support thread marked "resolved" may only have been closed for inactivity; it does not prove the installed version is fixed.

**Amounts.** A correct displayed total can coexist with a wrong gateway payload. Build a stage-specific amount table from local authorized evidence, comparing the displayed total with the payment create, patch and capture amounts. Compare line rounding with subtotal rounding, the discount basis and fractional quantities before touching the payment API. Keep explicit currency precision. A live-only report is not resolved by a sandbox success. Record the differing contracts and environments without attempting a live charge.

**Extensions.** Isolate suspected extensions in an authorized staging copy, preserving the merchant's active production stack, and keep a passing control. Disabling an express wallet button may remove the trigger, but it also removes a buying route. Label it a workaround and inspect the button's pre-calculation hooks.

**Return pages.** For wrong return pages, compare payment and order state before changing redirect handlers. An order that is already paid needs navigation repair, not another payment attempt.

## Worked decisions

Illustrative: the UI total is correct but the gateway order is created one cent lower, because net, discount and tax are rounded separately. Trace amount construction instead of hiding the difference with a tolerance. A later amount update can trip the provider's approval, and a sandbox pass alone does not resolve a reported live-only failure.
