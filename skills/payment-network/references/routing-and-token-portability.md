# Routing and token portability

## When to read

Read when running multiple processors or a fallback, testing a routing change, or migrating or orchestrating tokens.

## How to do the work

Separate route eligibility from route preference. For each eligible route, specify what happens on a known refusal, timeout and delayed original success; unknown outcomes require original-route reconciliation. Evaluate eventual unique orders as well as attempt rates across comparable issuer/country/method cohorts. Test token provisioning, chargeability and lifecycle/fallback independently, and include already-enrolled users in rollback rather than only stopping new allocation.

Count fees and operating cost alongside any approval uplift, and note where every route depends on one credential source: an outage there takes all of them down together.

## Worked decisions

Illustrative: a token provisions successfully but its charge fails on both available routes because the problem is issuer/token capability. A second processor does not necessarily remove that dependency. Check provisioning, merchant/processor scope, cryptogram requirements, lifecycle updates and forwarding separately; a portable customer identifier is not portable credentials.

When testing routing, retain the original route eligibility and distinct intended orders. One order with three attempts cannot be treated as three independent buyers. Compare comparable issuer, country, method and time cohorts; a model's allocation share can reflect cost guardrails or an outage artifact rather than intrinsic provider quality. A fallback experiment must define both new enrollment and existing participants' experience. Stopping new allocation while leaving existing customers in a failing token path is an incomplete rollback. Sacrifice some apparent failover speed when original-outcome reconciliation is necessary to avoid duplicate money movement.

## Deliverable and checks

Return a routing decision table and the comparison needed to evaluate it.

## Related work

Read [payment state and safe recovery](payment-state-and-safe-recovery.md) when that adjacent decision is unresolved.
