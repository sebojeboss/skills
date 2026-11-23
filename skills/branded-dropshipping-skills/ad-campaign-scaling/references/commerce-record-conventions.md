# Commerce record conventions

## When to read

Read when comparing or exchanging commerce observations, especially across cart, payment, order and fulfillment systems. Use the fields needed for the question.

## How to do the work

Scope identifiers by provider, account and entity. Keep their exact string spelling, including case and leading zeros. A variant identifies purchasable merchandise; a cart line may additionally depend on properties, selling plan and cart revision. Do not join a fulfillment line to an order line merely because both have a field called `id`.

Preserve exact decimal amounts and fractional quantities; avoid binary floating-point rounding in financial calculations. Record currency, units and basis: unit price, line total, discount allocation, payable total and settled amount answer different questions. Preserve the provider's precision; do not round to two decimals by habit. A reserve is not automatically a fee. Never sum across currencies or stages without an explicit conversion or reconciliation policy.

Distinguish missing, explicit null, zero, empty, unavailable and contradictory observations. Retain raw provider status and version; a common label must not erase authorization versus capture or pending versus failed. Preserve parent/component relations, loose units and per-item outcomes even when aggregate totals agree.

Keep event time, observation time and receipt time separate, with timezone and source precision. Do not infer ordering across clocks more precisely than the evidence supports. Record source version, environment and field locator. Mark local proposals separately from remote observations. An intended operation and an observed result are different records; a lost response remains uncertain until reconciled using the provider's supported contract.

## Worked decisions

Illustrative: a cart line and an order line both carry `007`. They remain different identities until the adapter supplies a verified relation. Two component rows may sum to the right merchandise quantity while one belongs to the wrong bundle. Preserve both the aggregate and relation check.

Illustrative: a quote has no tax field. Record it as missing; do not compare it as zero against an order tax amount. A refund followed by an older payment-success event does not automatically reverse the refund. Status transitions belong to the provider-specific recovery contract.

## Deliverable and checks

A useful observation has scoped identity, source/version/environment, necessary typed values, field locators and unresolved fields. Minimize customer information; normalization is not anonymization. Source records stay immutable and local unless disclosure to a named recipient is authorized.

Use the user’s existing spreadsheet, calculator or local data tools for comparisons. Check ID types, decimal precision and timezones explicitly before joining or summing records. A representable amount does not establish source authenticity, tax treatment, remote idempotency or merchant eligibility.

## Related work

Adapters own SKU mappings, statuses, supported retry windows and event authority. Offer economics, consent, disputes and supplier policy remain domain-specific.
