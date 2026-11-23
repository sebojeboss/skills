# Whop support boundary

## When to read

Use for a support task involving a Whop order/payment or connection. Keep the merchant’s helpdesk and fulfillment tooling unless there is an actual reason to change them.

## How to do the work

Current documented physical-commerce primitives include structured variants/stock, compatible multi-item checkout, delivery-address collection and tracking. Bind the affected item to the correct business, order/payment and variant before drafting or proposing a remedy. A multi-item order needs line-level investigation; do not treat its first tracking record as proof of every item’s delivery.

For a code-built Whop store, consider [embedded delivery lookup](https://docs.whop.com/elements/latest/delivery/overview.md) on the support page. Buyers can use an order or tracking number and checkout email to see carrier updates and support links. Verify that customer tracking is enabled for the account. Keep a staffed route for missing scans, wrong addresses and missing items; the widget cannot resolve those simply by displaying tracking.

Map facts to their owners: payment state from the payment network; dispatch/physical custody from fulfillment/carrier; return eligibility from applicable merchant policy; message receipt from the channel. A saved tracking number is not a purchased label or supplier acceptance. These primitives do not establish carrier rating, warehouse reservations, split fulfillment, exchange/restock or recurring physical shipment execution. Inspect the selected integration before promising those operations.

For connection use [Whop connection and attribution](whop-connection-and-attribution.md). Remote MCP/CLI production surfaces differ from API/SDK and Elements sandbox. A permission to read payment records does not grant refund authority. Inspect the actual exposed operation and its account scope; if missing, provide a precise native/manual handoff. Do not invent a Whop-to-store bridge or use historical capability claims as current specifications.

## Worked decisions

Illustrative: two variants were purchased, a tracking number was attached and one item is reported missing. Identify the missing line, package mapping and last carrier event. Explain known payment/tracking facts separately from delivery. A full refund may not be the intended remedy, and a tracking attachment alone cannot dismiss the complaint.

Illustrative: a payment refund was accepted but no message receipt exists. Record the financial state at its actual level and prepare or verify notification through the helpdesk. Do not promise bank timing or claim Whop sent a notice without evidence.

## Deliverable and related work

Return a scoped identity map, applicable policy, proposed/observed remedy and remaining follow-up. Payment-network owns payment contract interpretation; fulfillment owns physical investigation; support retains customer explanation and pickup.

Customer replies and macros never carry referral links or promotion.
