# Public Meta investigation

## When to read

Load when entering Meta Ad Library, resolving which Pages belong to a competitor, changing search scope, or recovering from zero or blocked results. This reference owns the browser procedure and the distinction between public UI and API access.

## How to do the work

Open the [Meta Ad Library](https://www.facebook.com/ads/library/) in an available browser. Select country and ad category before querying. A keyword search discovers candidates; choosing the right advertiser scopes the investigation.

**Qualify the advertiser before studying it.** Is this a store testing products the way the user would, or an established brand with repeat customers and trust the user can't borrow? Both can be worth studying, for different reasons. Record which you're looking at.

**Find all the Pages.** The library shows Pages, not ad accounts, and one business often advertises from several: a store Page, regional Pages, a founder's personal Page, creators running ads that send traffic to the store. Record the selected Page URL and ID and the domains its ads link to, then search for other Pages sending traffic to those domains. Two Pages with the same shop name can belong to different businesses, and a shared domain is a clue, not proof of a shared ad account. Inspect similar-name Pages separately rather than merging them on the name. A count or estimate built on one Page undercounts any business that uses several.

**Choose filters to answer the question.** For current messaging, active records in the target country are the useful view. For changes over time, keep the filters and collection times comparable. Keyword search matches the ad text, so in a non-English market search in the local language as well. Record language, platform, media and date controls exactly as displayed; if a filter isn't shown, it isn't available. The displayed start date, a delivery-date filter, your first observation and a tool's "last seen" are four different dates.

**Scroll in bounded increments and record coverage.** Pick ads that differ in argument, opening, offer, destination or start date. Open details, keep the public ID or permalink, the displayed status and dates, and the actual copy. Open destinations in separate tabs and re-snapshot. Stop collecting when the requested contrast is supported, and don't describe the loaded cards as every ad. If loading stalls, record partial status.

Inspect the link destination. Record the initial and final public URL; intermediate redirects you didn't safely inspect stay unobserved. Never put HAR files, cookies or signed transport URLs in the report.

## Spy tools and lookup privacy

Third-party ad tools combine public records with estimates; see [ad signals](ad-signals-and-estimation-limits.md). Before submitting a domain, check whether the tool turns lookups into public, indexed pages. If it does, use another permitted route. Native-library and store visits still disclose ordinary request metadata; inspect outbound data under the [browser contract](browser-runtime-and-sessions.md).

## Worked decisions

Illustrative: two Pages with the same shop name point to different domains. Keep two candidates, inspect identity clues such as domains, contact pages and shared creatives, and don't merge them until something supports it.

Illustrative: a country-specific search returns zero, while a broader permitted search returns records. Report both scopes. That isn't evidence the advertiser resumed or stopped spending.

Illustrative: a competitor's store Page shows six active ads, but its domain also receives traffic from ads on a founder Page and two creator Pages. Report the activity as four Pages sending traffic to one domain, not "six ads."

## Recovery and API distinction

A stale ref needs a fresh snapshot. A login wall, CAPTCHA or access denial is an access limit: use supplied public artifacts or report the blocked branch. No bypass, borrowed profiles or repeated doomed retries. The official [Ads Archive documentation](https://developers.facebook.com/docs/graph-api/reference/ads_archive/) is a separate integration contract. Verify current eligibility, token permissions, geography, field set and version before any API work, and don't describe public UI access as unrestricted commercial API access.

## Deliverable

A reproducible search and identity record: Pages and domains, filters, collection time, loaded count, stopping reason and selected public ad permalinks.
