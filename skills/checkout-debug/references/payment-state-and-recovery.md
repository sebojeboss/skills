# Payment state and recovery

## When to read

A payment form stays pending or blank, callback and return race each other, a retry has an uncertain outcome, or a stale tab still offers payment.

## How to do the work

Map the visible state to the actual lifecycle:

1. script requested;
2. SDK promise settled;
3. element mounted;
4. required fields usable;
5. submission started;
6. provider result observed;
7. server verification received;
8. order read back.

Record each failure at its actual boundary. A spinner can mean any of the first four stages.

**Pending is not rejected.** A timer expiring while the first load is still pending does not prove the load failed. Reusing a cached loader promise may simply wait on the same request rather than start a retry, so "retry" may change nothing. A truly rejected loader, by contrast, needs supported recovery rather than a permanent spinner. To tell them apart, use a controlled harness that can:

- hold the first load pending and then let it succeed (the control against treating delay as rejection);
- reject it explicitly;
- deliver a late response after an account switch. The old response must not mutate the new owner's state.

**Verification failure is not an unhealthy SDK.** A verification error should not destroy a healthy payment handle unless the contract requires teardown. Keep the known attempt and its configuration attached to the rightful account through error rendering, remount, reload and recovery.

**Callback, return and server state are three observations.** A paid buyer might never reach the return page; a return parameter is not payment proof. Record transport events and authoritative current state separately, with clock uncertainty. Never fulfill from a browser return parameter, and never create a new payment merely because verification timed out. Retain exact provider statuses. Ask payment-network to resolve provider retry identity, request equivalence and event authority when those contracts are uncertain.

UI repair can remove stale affordances. Backend duplicate-safe processing needs separate source and controlled-execution evidence; disabling a button and keeping a local ledger cannot enforce remote duplicate safety. Use the existing test runner or a minimal local event table.

## Worked decisions

Illustrative: a second tab succeeds while the first still offers payment. Refreshing the first tab on focus can fix the UI. Backend evidence is still needed to show that repeated submission cannot create another charge, so close the UI repair and the duplicate-safety question separately.
