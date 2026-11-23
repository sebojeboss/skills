# Other senders and custom event bridges

## When to read

A different sender, headless checkout or custom integration owns a relevant operation. Do not assume similar UI words imply equivalent semantics.

## How to do the work

Verify the operations this task needs in the existing tool, UI or export: event, order, consent and flow reads; native rendering; recipient/message inspection; draft save, controlled test or activation. For each needed operation, record its route, account/version/scope, required fields, pagination, timestamps, result identity and recovery after an uncertain write. Leave an unverified operation as a manual step or specification.

Normalize only fields with a known meaning. Preserve raw provider states alongside domain interpretation. Keep event ID, flow run ID, send attempt ID and provider message ID distinct. Explicitly map cart versus checkout variable paths and return links; do not implement a universal template engine to paper over missing documentation.

For SMS investigate the actual sending route: a service-level callback may not apply when the request uses only a sender number. Inspect the request contract and provider message record before inferring failure from absent callbacks. Carrier filtering, opt-out and delivery failure require their own documented responses; retries or sender rotation are not general remedies.

## Worked decisions

Illustrative: the integration records an HTTP timeout but the provider has a message ID with an accepted state. Reconcile that record. Do not emit another message under a new local ID merely because the bridge lacks a callback. If the provider offers no suitable lookup, preserve uncertain state and escalate the specific message evidence rather than treating uncertainty as failure.

A provider preview may require uploading an event fixture. Prefer synthetic fixtures and necessary fields; authentication is not permission to upload private research or unrelated customer context. Existing authorized merchant data use remains scoped to that recipient and purpose.

## Deliverable and checks

Return operation/field mappings and a manual-ready configuration or supported patch plan. Native Postscript, Attentive, Twilio and other systems each need current contracts; this file is not a claim of verified feature parity. With supplied files, use local event/template/trace checks and label missing account behavior. For a later authorized integration, validate duplicate/out-of-order events, delayed purchase, revocation, missing callbacks, lost write response and status readback at the actual provider boundary.
