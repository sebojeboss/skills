# Discover the existing recovery stack

## When to read

Setup, migration questions, unknown ownership, or two systems sending reminders. Skip this intake for a supplied-copy edit.

## How to do the work

Start with existing exports, account context and the user's supplied flow. Map six owners: cart, checkout/payment, event collection, customer identity/consent, sender, and purchase/exit authority. Record exact platform and account, known metric origin, access route and evidence date. Separate observed facts from user reports, documented capability and unknowns. A payment migration need not move the email sender.

Use an available browser to inspect the selected account's integrations, flow trigger and recipient activity. Compare the native commerce recovery setting with external flows; identify which system owns each message and merchant notification. A notification to staff is not recovery to a buyer. Read-only exports are often more useful than a large screenshot of the flow canvas. Do not scan credentials or unrelated settings.

Choose the least additional system that solves the demonstrated gap. When no sender exists, first check native capability, consent capture, supported event and return-link behavior. Compare an external sender only against missing requirements, existing costs and maintenance burden. Account signup and paid plan selection are actual product decisions, not technical prerequisites to writing a flow specification.

## Worked decisions

Illustrative: a store changes its payment destination but keeps a working sender. Preserve message design and suppression rules; remap variant/cart identity, completed-order source and return links. If the new order source does not reach the sender, do not activate by assuming old purchase exits still work. The sacrifice is temporary reduced automation, in return for avoiding reminders to buyers.

Two active recovery systems require a cohort/notification map before disabling either. One might serve a different checkout source. Remove duplicate ownership only after mapping coverage and preserving the prior setting.

## Deliverable and checks

Write a short owner table: component, account, event/entity, read/write route, evidence status, unresolved contract. Select the matching adapter(s). With no access, deliver a manual-ready flow spec and precise requested artifacts; do not label unknown as unsupported. Related: event inspection, eligibility, and the selected provider contract.
