# Helpdesk and store contract

## When to read

Use when reading live support records, reviewing rules/macros or evaluating a connected action.

## Inputs and supported route

Reuse the merchant’s selected helpdesk, store, return portal and channel tools. With approved local exports, bind ticket, order, item and remedy identifiers and record source/version/observation times. With native connected tools, inspect effective operations/scopes before use. Do not infer an API operation from the presence of a dashboard button.

For an authorized inspection, select the intended account/store, open the ticket, follow its order link, and compare the customer’s item against that order. Inspect associated macro actions and rule scope. Follow return/payment records and then the channel receipt. Record the strongest actual evidence; avoid broad exports or unrelated profiles. No new confirmation is needed merely for routine reversible navigation within scope.

## Operation mapping

| Work | Required surface | Without it |
| --- | --- | --- |
| Draft | Ticket/context and relevant policy | Ask for missing facts or use approved export |
| Status explanation | Intended order/item and dated fulfillment/carrier state | State missing evidence and investigation owner |
| Remedy decision | Policy, authority, prior remedies and release event | Prepare review/exception request |
| Execute remedy | Verified write operation plus supported readback/recovery | Native manual handoff; no fictional success |
| Notify | Channel send operation and available receipt | Local draft; do not claim delivery |
| Handoff | Assignment plus staffed pickup observation | Explicit unresolved ownership |

Gorgias/Shopify, return portals and messaging integrations each have their own contracts. Verify current official documentation, actual account entitlement, scope, pagination, status meaning, sync freshness, rule precedence and side effects. A macro can execute commerce actions on send; a draft-only route must never invoke send just to preview it. A rule may span stores unless narrowed. An overall error can conceal earlier success. These are reasons to inspect the selected product’s current behavior, not guarantees about every version.

## Recovery and deliverable

Keep read and write authority separate where available. Do not broaden a 403 into a new grant or repeat an uncertain write. Use [reconciliation](partial-failure-and-reconciliation.md) and [commerce conventions](commerce-record-conventions.md). For an integration review, distinguish documented, observed and unverified capabilities and show the usable local or manual route. For a single case, state only the missing operation and next action. Credentials use supported service authentication only; no secrets in artifacts, URLs or logs. Transmit only authorized minimal fields; never upload unrelated context to a vendor’s diagnostic prompt.
