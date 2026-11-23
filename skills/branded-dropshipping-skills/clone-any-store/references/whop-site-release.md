# Whop site release

## When to read

Read before creating or linking a site, choosing CLI setup, packaging source, uploading a preview, promoting a build or recovering an uncertain release.

## How to do the work

Reuse the project stack or current official Whop scaffold, implement locally, run its reviewed build, inspect the actual source/build archive, upload the candidate when authorized, inspect that candidate, and promote the reviewed build when publication is authorized. Default deploy and preview upload have different effects. Local preview has no Whop upload; production preview uploads without promotion; publication changes the live build. API/Elements sandbox is a fourth, separate test environment.

Use the scaffold to remove setup work, then keep the project reproducible with its lockfile. Attach recoverable source to the candidate so another machine or agent can continue from that version. Promote the reviewed build rather than rebuilding a different version for launch.

Record app/build/domain identity and source recovery. Read actual package entries rather than trusting ignore rules; exclude private notes, credentials and provenance. After response loss, reconcile the named resource using the supported operation contract before retrying. A local journal cannot create remote idempotency. Promoting an earlier build rolls back code, not catalog/payment/customer changes.

Read [connection readiness](whop-connection-and-readiness.md#install-and-sign-in-to-the-whop-cli) for the official CLI install commands, sign-in and account access. Use the installed CLI's version/help/schema and current [CLI documentation](https://docs.whop.com/cli/overview.md) to establish the scaffold/dev command for the selected stack. Reuse the project lockfile; review package scripts before installing/building. Do not add unrelated plugins or replace a working framework for convenience.

The documented release operations are:

```sh
whop apps deploy --preview
whop apps builds promote BUILD_ID
```

These are external operations, not commands to run just because this reference loaded. The preview command uploads a production build without promoting it. Default `whop apps deploy` also promotes. Confirm the linked app and business before either. [Hosting documentation](https://docs.whop.com/developer/websites/hosting) defines current source/build handling and older-build promotion as rollback. Verify the installed version and actual returned identity. Do not infer a sandbox switch.

Before packing a release, inspect the exact file list and source root. Include the files needed to recover and edit the site, and exclude credentials, local caches, research and unrelated files. Check symlink targets and paths for unintended inclusion. If comparing versions, compute local hashes or use the existing version-control diff, then compare the actual archive contents with the intended list. A hash establishes byte identity, not privacy or editability.

After upload, inspect the exact candidate, recover its source to a fresh directory using the supported interface, and make a harmless edit locally. Verify source availability separately from a successful build. On a lost response retain the app/build identifiers and supported idempotency key, read state and classify confirmed/not applied/unknown. Do not mint a new retry identity merely to get an answer.

## Worked decisions

Illustrative example: the candidate renders but recoverable source is absent. Preserve the accepted live build, repair packaging and recover source into a fresh directory for a harmless edit/build/preview check. If promotion acknowledgement is lost, read back the pointer rather than create another app.

## Deliverable and checks

Deliver the reviewed source/build manifest, the actual preview or live-build receipt, and precise recovery limits. Treat marketplace review, Blueprint distribution and notices as additional actions rather than assumed effects of deployment.
