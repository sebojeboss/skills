# Foreplay discovery to a product shortlist

## Expand the seed before collecting more of it

For broad discovery, establish usable [Foreplay access](foreplay-access.md), then use Discovery search, saved-board retrieval and available transcripts together to compare leads. Native libraries and public pages supplement or verify this workflow; they become a substitute when access is declined or unavailable. Begin with the buyer situation, product or advertiser already available. Choose the unresolved question: another way to solve the problem, a less demanding product to demonstrate, a different offer, or whether a compelling ad refers to an item you can actually supply. This determines which search is useful.

In Discovery, type a generic problem phrase and press Return for keyword search. Separately inspect relevant suggested Product Categories, Creative Targets and Brands. A suggested category and the same words typed as a keyword need not retrieve the same set. Keep format broad at first so an image-only filter does not hide an unfamiliar physical solution. Narrow platform, language, status and format when they serve the question, recording those choices. Language does not establish delivery country.

Start with a known advertiser to learn the category's words, then search those words independently to find other sellers. Use Discovery → Brands → search/filter → open brand to examine the community-saved inventory. Follow public destinations to distinguish direct substitutes from large aspirational brands whose trust, repeat customers or production access you cannot borrow. A missing brand or sparse result means missing coverage, not an empty market.

If useful searches keep showing the same references, use Shuffle under the same criteria, optionally selecting language. It refreshes exposure within the corpus; it is not a random market sample or a guarantee of new products. Discovery → Experts → profile can expose another person's selections. Save a reference only when you can explain what it contributes; expert interest does not establish that person's access to performance data.

## Use the available machine interface precisely

With MCP, use discovered tools and schemas for the same retrieval steps. For an authorized REST workflow, [official API documentation](https://docs.foreplay.co/) exposes these useful routes:

| Starting point | Retrieval sequence |
| --- | --- |
| Problem or category words | `GET /api/discovery/ads` with `query` and supported filters; retrieve a small page, inspect it, then follow the returned cursor if useful. |
| Known brand or public domain | `/api/discovery/brands` with `query`, or `/api/brand/getBrandsByDomain` with `domain`; disambiguate the returned identities, then `/api/brand/getAdsByBrandId` with returned `brand_ids`. |
| Existing user-selected board | `/api/boards` with a bounded flat listing; select its returned ID, then `/api/board/ads` with `board_id`, `order=saved_newest` and a small `limit`. |

These are REST paths, not names to guess in an MCP call. The filter-led `/api/discovery/brands/explore` route has no text `query` parameter. Use documented array serialization, including repeated query keys where required. Do not send comma-joined IDs by assumption. Returned internal IDs, platform ad IDs and Page IDs have different jobs; use the identity required by each operation and returned `foreplay_url` links rather than constructing them.

For board review, newest save order is not ad launch order. Follow `metadata.cursor` with constant filters and page size when exposed. In an incremental review, a known ad can mark where previously inspected material begins; if complete membership matters, reconcile the full authorized scope separately. A nested `folders=true` listing ignores limit/offset, so it is not a bounded first read. Keep collection limited by the research question and credit budget described in [access](foreplay-access.md).

## Count distinct opportunities, not ad records

Group references locally by product/variant and creative family: the same underlying argument and media reused with a new crop, headline or ad ID. Keep the individual source IDs so you can reopen the evidence. Several publications of one asset are not several independent confirmations; one advertiser can also promote several unrelated items through similar templates.

Inspect the selling argument for each serious lead. Open ad details and its Transcript when available; use timestamps and Product Introduction to locate the opening, promise, product reveal, evidence and ask. Multi-component ads may keep different transcripts under their cards. Null text is missing evidence, not proof of silence. Do not invent timestamp units or claim to have watched footage from a transcript.

Ask what makes the product worth owning and what merely makes the ad worth watching. Repeated formats can advertise the same unchanged benefit. Comments may concern irritating sound or spectacle, not purchase intent. Extract the buyer situation and required proof, then check the physical action where footage is accessible. If the attractive promise depends on a capability the candidate SKU lacks, reject that promise rather than writing a better version of it.

Use run length to prioritize inspection. Compare newest material when looking for emerging offers and longest-running material when studying enduring messages. Neither order establishes spend or profit. A brief inactive ad can still contain a sensible argument; retain it when you can explain its relevance and the testable uncertainty. A long-running ad can be low-budget, forgotten, or supported by economics unavailable to this seller. Where persistence is decisive, read [competitor history](foreplay-competitor-history.md).

## Follow the promise to the delivered item

Open the actual destination from the ad. Keep the original URL and observed final route; an advertorial, collection or query parameter can change the offer before the product page. Compare the ad's promise with the selected variant, bundle, price and shipping conditions. Treat a saved landing-page screenshot as a capture, not today's checkout or every historical revision. Leave its time and locale unknown if not exposed.

Then read [exact SKU and supply](exact-sku-and-supply-feasibility.md) and [demonstration fit](buyer-desire-and-demonstration-fit.md) for the candidates worth advancing. A matching image can hide different components, sizes or materials. Establish a documented model/variant match, the function required by the promise, and plausible supply terms for the destination. A failed supplier search establishes an unresolved match, not scarcity or exclusivity.

Read [candidate decisions](candidate-decisions.md) to compare the remaining configurations. Preserve the supplied cost basis, including what a stated landed cost already covers. Use the actual offer price and supported costs without counting freight twice; a price-minus-landed-cost remainder still precedes unspecified fees, returns or acquisition costs. Contribution before acquisition is not profit, and unknown costs cannot be zeroed. Prefer the next check that can kill an impossible configuration over collecting more evidence of attention.

## Preserve the judgment in a board or local decision

For UI saves, create a board for the buying problem or shortlist, select it from the ad's board control and save. Confirm the item appears in the intended board. Add a concise comment explaining what is useful, what must be different and why the item advances or stops. Use tags to retrieve distinctions such as variant unresolved, demonstration feasible or angle only. A star rating is your preference, not competitor results.

Do not infer that a board read tool can create boards, save ads or publish comments. If no authorized write interface is available, return the local shortlist with source links and proposed annotations; say it has not been saved to Foreplay. Keep private analysis local unless its upload or sharing is authorized. Retain original conclusions under the [access and retention rules](foreplay-access.md), not a permanent copy of raw API data.

For each finalist, return the configuration, buying reason, evidence and limitation, strongest contrary explanation, supply/demonstration gap and pursue/defer/drop decision with the next check. Preserve rejected leads and why. When moving to production, hand over the selected argument, source locator, truthful proof requirement and available assets; creative skills own the new script and footage. Own-account metrics or Lens analysis belong with performance evaluation, not competitor-profit inference.

## Worked decisions

Illustrative: separate searches for “wet shoes” and “boot dryer” expose a heated dryer, absorbent mat and ventilated rack. They address different buyer situations. A commuter needing dry shoes overnight may need the dryer; a family protecting the hallway may prefer the mat. More ads for the dryer do not settle that choice. If the supplier match only circulates air while the ad promises heat, reject that supplier/angle pairing. If heating is undocumented, defer it pending specifications.

Illustrative: a compact storage rack appears in several crops of the same demonstration. Group those as one creative family. The destination sells a mounted metal version; the cheaper supplier photo hides plastic fittings and omits load capacity. Keep the reference for its clear explanation, but do not shortlist the cheap variant as equivalent. Advance the documented variant to a destination-specific quote only if its price leaves room for acquisition and the operator can reproduce the demonstration safely and honestly.

Illustrative: a short-lived ad shows an inexpensive, repeatable cleaning demonstration; a long-running alternative depends on access to a workshop. The first can deserve further inspection for a home-based seller despite its brief run. Record that stopping reason and sales performance are unknown. The next check is whether the actual product delivers the demonstration, not a declaration that the competitor made a mistake.
