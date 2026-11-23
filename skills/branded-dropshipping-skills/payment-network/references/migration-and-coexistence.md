# Migration and coexistence

## When to read

Read when adding Whop beside an existing site, moving billing, customers or catalog, or retiring a provider.

## How to do the work

Map customers, subscriptions, catalog, order authority and outstanding obligations before selecting a cutover cohort. Route new eligible purchases independently where possible; give each renewal exactly one billing owner. Prove the supported credential transfer or reenrollment and destination event handling before moving old renewals. Define stop-admission, code rollback and continuing refunds/fulfillment separately so a build rollback cannot masquerade as business rollback.

Existing subscriptions keep their current owner until the destination actually qualifies to bill them. Version the destination's event handling before cutover, and confirm the export is complete before relying on it; keep the old provider's records and refund/dispute access for as long as obligations can surface there.

## Worked decisions

Illustrative: new purchases go through Whop while preexisting subscriptions remain with their current provider. Record the owner of each renewal and retain old-provider refund/dispute access. Customer CSV import does not establish a supported vault transfer, mandate migration or payment-method portability. Where migration is unsupported, consented reenrollment and continued coexistence have different customer costs; present those choices rather than inventing a bridge.

Build a cutover table for new admission, active subscriptions, pending payments, refunds, disputes and unfulfilled orders. A payment that succeeds while downstream order sync fails needs order repair, not a second charge. Track the sync operation identity and query the destination before resubmitting it. Export creation can itself be an asynchronous remote job: keep the export ID and poll rather than starting repeated jobs. Rollback must stop new admission and define who services continuing obligations after code is reverted.

## Deliverable and checks

Return the cohort/billing-owner map, migration plan, renewal exceptions and cutover steps in the merchant’s existing format or a Markdown brief.

## Related work

Read [physical commerce readiness](physical-commerce-readiness.md) when that adjacent decision is unresolved.
