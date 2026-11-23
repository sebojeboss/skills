# Meta access and reporting

## When to read

Load when connecting an account, choosing a reporting source, requesting a fresh report, diagnosing access failure, or determining whether a requested mutation is supported. A question answered by an adequate local export does not require connection work.

## How to do the work

Start with the existing export or connection. For fresh inspection, use an available browser in the authorized account. In Ads Manager confirm the account ID, timezone and currency before selecting a date range. Choose one reporting level, remove overlapping breakdowns, and select spend, impressions, link clicks, the intended purchase event and purchase value. Record attribution and reporting-time settings explicitly; download the export if available. Check that all requested rows/pages arrived. An empty result is not proof of zero spend.

Inspect configured status separately from effective delivery status, the budget-owning level, bid/control settings and recent edits. If event health is a competing explanation, inspect existing Events Manager diagnostics and event/value definitions; do not install a pixel or submit test customer data as part of reading. A valid UI login can support inspection even without an API connector; it does not bypass an account restriction.

For connected reporting, discover the actual available tools and their permissions before calling them. Meta's official [Insights documentation](https://developers.facebook.com/documentation/ads-commerce/marketing-api/insights) and [authorization contract](https://developers.facebook.com/documentation/ads-commerce/marketing-api/get-started/authorization) are version-sensitive dependencies. Verify `ads_read`, asset access, app access tier and requested fields. Use the supported native tool, browser/export route or state the exact missing prerequisite. Never log tokens or credential-bearing pagination URLs.

## Worked decisions

Request the smallest report that answers the question: one level of the account → campaign → ad set → ad hierarchy, an explicit date range, currency, time zone and, for API work, version. Don't request buyer-level records, audiences or unrelated assets. When access fails, check permission, asset assignment, app access tier and token validity separately; each has a different fix. Treat pagination, asynchronous report jobs and conversion backfills as ways a report can be incomplete without saying so.

The Marketing API/Insights route provides authorized account state and performance. Public Ad Library research supplies competitor creative/context where available; it cannot substitute for private Insights, contribution or a causal performance assessment. Use `reverse-engineer-any-store` for competitor discovery. Do not promise unrestricted commercial Ad Library API coverage.

Distinguish a valid token with no assigned target asset from an expired token and from an unsupported report breakdown. Retain a partial job as incomplete instead of presenting the first page as a complete account. The artifact is a source manifest and report snapshot, with connection/access status only when relevant. Official documentation belongs here as a maintained technical dependency. Distinguish Marketing API access-tier labels from permission access levels using the current authorization contract; do not copy older setup thresholds blindly.
