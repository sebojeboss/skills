# Whop checkout contracts

## When to read

The actual flow is a Whop Site, hosted checkout, Elements embed or invoice.

## How to do the work

Map the actual SDK/API version and surface: product and variant (plan), checkout configuration or session, payment, access, and physical-order handoff. Inspect the entry surface and installed version before adopting any example. Use the official documentation for current inputs, then verify the deployed SDK or tool schema:

- https://docs.whop.com/elements/latest/checkout/overview
- https://docs.whop.com/api-reference/payments/create-payment

Elements uses plan, items and configuration concepts. API variant IDs and local SKU strings need explicit mapping, even when their spellings look alike.

**Variants, quantity and carts.** Follow size/color choice → submitted variant ID → checkout item → paid-order line. Compare the image, price and quantity as well as the title. Test an unavailable combination and a second option change: stale state can buy the previous selection. For quantity two, verify that the variant allows multiples. When one item works and the combined cart fails, check same-account/currency rules, stock mode, billing terms and tax/payment compatibility before changing the UI. Use the deployed contract; never turn real finite stock into unlimited inventory as a repair.

**Mounted checkout.** A mounted Elements checkout is minted from its create-time plan, items, quantity and configuration. Changing a display prop is not evidence the checkout changed. Rebuild a revised cart through the supported lifecycle, and resolve any payment-attempt uncertainty before replacing anything.

**Address.** Collect a structured address through the supported product/checkout route, and read back the actual payment or order fields. If invoice and product checkout behave differently, inspect each independently.

**Fulfillment primitives.** Documented variants, stock, compatible multi-item carts, address collection and shipment tracking are supported primitives. A shipment-tracking record attaches an existing tracking number. It is not a carrier label, a supplier order or an inventory reservation. Carrier rating, warehouse reservation, split fulfillment, exchange/restock and physical renewal remain separate contracts. Keep access and membership checks apart from physical delivery checks.

**Environments.** Use separate API/SDK and Elements sandbox resources for isolated payment tests; see https://docs.whop.com/developer/guides/sandbox for current support. Remote MCP and CLI act on production, and a preview deployment uploads code. Current documentation does not establish merchant entitlement or an executed test. Use existing authorized connection or read exports when available, and name the exact missing fields when not.

**Referral code.** The business-referral code SKILL must not be copied into a buyer-sale `affiliateCode` by assumption.

## Worked decisions

Illustrative: quantity two is refused because the selected variant disallows multiples. A different cart failure comes from changing create-only items on a mounted checkout. These are distinct eligibility and lifecycle causes; verify which one applies before proposing an initialization patch.
