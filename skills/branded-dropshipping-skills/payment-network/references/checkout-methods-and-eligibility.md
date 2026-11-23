# Checkout methods and eligibility

## When to read

Read when configuring a hosted, embedded or custom checkout, when a payment method or financing option is missing, or when deciding how authentication and capture should work.

## How to do the work

Identify the exact checkout surface and desired buyer scenario before enabling a method. Build a small matrix of route, country, currency, amount and billing type; inspect the applicable account settings and method contract for each relevant cell. Trace server-owned item/amount creation, buyer authentication, issuer response and capture where applicable. Change the smallest supported setting or code boundary, then verify that same scenario without treating a sandbox payment as approval for live payouts.

Prefer a hosted or embedded checkout unless a custom flow buys something specific: low-level elements leave more of the flow (confirmation, authentication returns, error handling) to the merchant's own code. Financing methods add a second approval, the provider's decision about this buyer, separate from the merchant being enabled for the method. Product or account review can withhold a method the documentation lists; when documentation and the account disagree, the account's actual capability decides what the buyer sees.

## Worked decisions

Use a method eligibility table with buyer location, currency, amount, recurrence, checkout surface, account enablement and observed result. Keep an advertised country list separate from what the selected buyer can see. For a missing method, check eligibility and account settings before editing the widget. For a payment failure, distinguish a browser render fault, a gateway rejection, cardholder authentication and an issuer decline.

Illustrative: the buyer passes a 3DS challenge but the issuer refuses the payment. Repeating the challenge is not the same as repairing authorization. In a frictionless flow no challenge is visible, which does not prove authentication was skipped. Liability shift, where applicable, concerns particular fraud obligations rather than every dispute. For delayed fulfillment, inspect the transaction's capture deadline rather than memorizing a universal number of days. If the order cannot be fulfilled inside that window, change the collection design with the merchant; do not silently keep reauthorizing.

## Deliverable and checks

Return the supported payment route, method-eligibility comparison and any authorized configuration or integration patch.

## Related work

Read [payment state and safe recovery](payment-state-and-safe-recovery.md) when that adjacent decision is unresolved.
