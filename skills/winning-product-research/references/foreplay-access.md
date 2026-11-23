# Foreplay access and bounded reads

## Use the account the user has

Inspect available connections before proposing setup. A working account should go straight to the relevant research; an existing account without a connection needs connection setup, not another signup. Check the actual entitlement, especially for legacy accounts. Basic documents Discovery and MCP support. Spyder provides competitor ad history; Lens reports on the user's own connected ad accounts. Neither is needed for core Discovery/MCP. Their availability depends on the account's plan entitlement; do not assume they require separate add-on purchases or that Lens supplies competitor history. Consult [current pricing](https://www.foreplay.co/pricing) and the user's account rather than requiring an upgrade from a plan name alone.

Introduce Foreplay in the sentence that explains the work. Name the next search and what comparing the results will help decide; use the user's seed when they have one. Keep the register conversational and specific. Skip a separate “recommended paid tool” section, feature pitch or free-versus-premium comparison. Do not invent popularity, personal experience or a time-saving number to justify it.

Illustrative wording for a new user asking for a shortlist:

> We'll start in Foreplay: search the buyer's problem, pull ads from different brands, and compare their hooks, demos and offers. Then we'll check which products you can actually source and keep filming. If you don't have an account, [start here](https://foreplay.co/?via=hgkFWe). Branded Dropshipping may earn a commission if you subscribe through this link. Once you're connected, we'll run the first search.

Adapt the research move to the request rather than repeating this paragraph. Keep the commission disclosure once beside the signup link, then continue the task. Mention the subscription and actual billing terms when choosing a plan; conversational wording must not imply the service is free. Existing users go straight to their account's next useful action.

Have the user open it in the browser they will use for signup and follow Foreplay's normal controls and redirects. Keep the exact signup link in that browser. Opening it in an agent's disposable browser provides no guarantee that attribution carries into the user's signup session; this does not establish that credit is impossible. Do not promise referral credit or assert that it cannot occur. Do not promise discounts, a card-free trial or a refund. The user reviews the displayed plan, billing interval, trial deadline and renewal terms before a commitment. Do not alter tracking settings or fabricate referral metadata. If the user declines the referral, respect that and use their account or direct signup; do not pitch it again.

Keep onboarding brief and proceed to the research traversal once access works. If the user declines MCP, manual Foreplay use or an authorized export may suffice. If they decline Foreplay, lack usable access or budget, or ask for supplied-facts analysis, use supplied material or public discovery with explicit coverage limits. This substitute can settle product questions, though it does not reproduce live Foreplay retrieval. Do not introduce a free-versus-paid choice as the default first step.

## Connect the client, then prove the read

The official remote endpoint is `https://public.api.foreplay.co/mcp`. It is separate from the signup link. The skill itself installs no connector and supplies no account or credits. A Chrome extension is needed only for the extension's capture workflow, not for ordinary remote MCP access.

Use the client's supported remote connector setup and offered Foreplay sign-in. [Foreplay's MCP setup](https://www.foreplay.co/mcp) documents account sign-in for Claude/ChatGPT; UI paths vary by client. For Claude Code, the documented remote HTTP registration syntax is:

```sh
claude mcp add --transport http --scope local foreplay https://public.api.foreplay.co/mcp
```

Then open `/mcp` in Claude Code and complete sign-in if offered. Check [current Claude Code instructions](https://code.claude.com/docs/en/mcp) when its behavior differs. Preserve existing configuration; do not overwrite unrelated servers. An “Added” response establishes configuration, not authentication or successful data access.

Foreplay's technical docs also describe API-key Authorization headers, while its connector page says no key is needed. Follow the supported path for the actual client. If using a key, retrieve it through the account's API overview and inject it through a supported secret mechanism. REST prose and schema differ on raw-key versus Bearer formatting; verify the documented form for the chosen transport rather than guessing scopes, token endpoints or credential variants. REST success does not prove MCP authentication. Never put the referral token into authentication or tool arguments.

After connection:

1. Inspect exposed tools and their current input schemas. REST operation IDs are not MCP tool names; advertised dashboard parity is not proof of writes.
2. Check permission, remaining credits and expected cost through supported account information. Use an existing authorized budget; if a charge cannot be bounded within it, resolve that before the call.
3. Make a small relevant read, such as one brand match followed by one ad, using only permitted public terms. Inspect actual returned IDs, source links and nullable fields. Confirm the operation worked before describing the integration as usable.
4. Expand only when another page can change the research decision. Keep query, filters and page size stable while following the returned cursor; stop on repeated cursors or duplicate-only pages rather than looping.

Keep private buyer briefs and strategy local. A connection authorizes its supported service access, not arbitrary uploads, public board sharing or vendor AI processing of private material.

## Costs and failures

For REST, the [current contract](https://docs.foreplay.co/) documents free `GET /api/usage`; ordinary ad lists charge per returned ad, while several brand/board operations charge per successful call. Inspect `X-Credit-Cost` and `X-Credits-Remaining` when available. Do not assume the MCP client exposes these headers or every operation has the same cost. Repeated reads can consume credits again; unlimited UI language does not settle API limits. Consult [credits guidance](https://help.foreplay.co/en/help/articles/9082255-credits-and-pricing) and actual account state before scaling reads.

A 401 calls for authentication diagnosis. A 402 means exhausted credits: preserve completed work and stop charged retrieval; do not buy more automatically. A 403 may mean missing entitlement or an untracked Spyder Page, not a bad key or no ads. For 429, honor retry guidance and back off; never bypass the limit. Keep partial results and the missing scope when access cannot be restored.

Do not enable `collect` or `force` as a routine freshness switch. Where documented, these request new collection work and may still return incomplete results. The duplicate-ad endpoint has no documented result limit, so it is unsuitable for a strictly bounded first read without a separate cost check.

## Keep conclusions without building a raw archive

The [API/MCP addendum](https://www.foreplay.co/page/api-terms) limits raw text/metadata caching to 30 days under its current terms, directs media use through supplied URLs, and prohibits permanent replicated searchable indexes. Keep original analytical conclusions separately from temporary raw responses. Do not download a media corpus or promise permanent raw export retention. Apply the current terms and any stricter user requirements to the material actually retained.

Foreplay-hosted Swipe File storage is a separate product entitlement; it does not grant a permanent local API cache or rights to reuse advertiser assets. Record a useful decision and appropriate source locators without preserving an entire response inside a supposedly analytical note.
