# Offer placement and configuration

## When to read

Read when writing offer UI or copy, choosing between pre- and post-purchase placement, configuring an app or diagnosing missed renders.

## Choose where the offer appears

Place the offer at the earliest point where the buyer can make the relevant decision without undermining the original purchase. That point changes what the offer may ask for.

**Before payment** (product page, cart, checkout add-on), the offer competes with the main purchase. Every extra decision is a chance for the visitor to stall, so judge it by what it does to front-end conversion and revenue or contribution per visitor, not by its own take rate. Keep it small, clearly optional and easy to ignore. A compatibility question that must be answered belongs here, inside the offer.

**After payment** (post-purchase page, one-time offer, thank-you page), the original checkout has already completed, so the offer can't stop that purchase from happening. That is why operators run bolder offers here, sometimes priced well above the front-end product. It isn't free of risk to the order. A pushy or confusing offer can prompt cancellations, refund requests or chargebacks, and buyers who feel squeezed are less likely to return. Track cancellations and refunds for both accepting and declining buyers, not just take rate. A large post-purchase offer is a high bar. It needs a product this buyer would want and copy that earns the price. A 10% take rate on a $400 offer adds $40 of gross revenue per exposed buyer, not $40 of profit. Price it from the buyer's job and your real costs, not from a multiple of the front-end price.

Wherever it sits, show the item and quantity, the incremental price, a genuine savings basis, optionality and any recurring obligation, with a clear accept and decline. Resolve compatibility and variants where the offer is shown. Exclude items already owned or already in the cart where appropriate. Check whether a new widget displaces useful existing information.

A digital addition earns its place by helping the buyer use the physical product: instructions, practice or continuing help. Price the content and support work too. On Whop, map membership access and compatible billing terms before combining items; one-time goods and a recurring membership do not automatically fit one cart. If affiliates bring the sale, verify that the proposed basket still qualifies for their commission. Place a later member offer when use of the first product creates the need.

## Trace the actual route

Use an available browser to trace the product → cart → checkout → confirmation route on desktop and mobile. Inspect eligible and ineligible selections, choose compatible variants, add and remove ordinary cart items where the inspection permits, decline the offer, and check visible totals and the confirmation. An offer that never renders for a payment method or device changes exposure, not demand.

Map the selected offer to the existing app or verified platform objects; capture the previous state and produce a field-level diff. Apply only supported, authorized changes, then read the persisted settings back. If a save response is lost, reconcile the object or version before retrying; a local operation log is not remote idempotency. Hand actual payment and confirmation behavior to checkout-debug while keeping the offer rationale and measurement here. No screenshot or toast alone proves a working purchase.

**Illustrative contrasts:** a selector resolves fit; an unavailable payment route never shows the offer; a new modal removes a useful cart widget. For a Whop add-on, prepare the compatible cart before mounting checkout and remount on cart changes under the documented Elements contract. That supports a pre-payment add-on design, not an assumed one-click post-payment charge.

**Output:** a concise offer specification, original copy, placement decision, relevant capability checks and any actual configuration readback. Existing Shopify/app workflows remain supported. For a new destination, evaluate the supported Whop route with its documented physical primitives and explicit unverified dependencies. Load only the applicable platform contract; don't preload every provider.
