# Browser reproduction

Read when a buying path fails, local and remote results disagree, or you need a passing control.

## Reproduce the reported journey

Pin origin, build, entry path, browser/device and expected behavior. Preserve the selected offer. Follow selection → request → returned commerce state → rendered state, keeping only the relevant fields locally.

Use an available browser to open the authorized URL and inspect its current state before acting. Check tool support for extra captures; response interception may be unavailable.

Before the single action, record the selector choice, displayed price, quantity and cart contents. Follow the buyer's cart drawer or cart-page route. If the existing local harness exposes network evidence, inspect the specific request and response; avoid credential-bearing HAR exports. With DOM-only access, state that limit and identify the payload or export that would distinguish the causes.

## Choose a comparison that can disprove the cause

Compare the same build locally and in deployed preview, quantity one and two, native form and custom drawer, clean and actual ad link, or ordinary and in-app browsers on the same phone. Change one variable where possible; name remaining confounders. A native form supplies navigation and refresh that a custom drawer must implement, so its success does not certify the drawer.

Keep the actual ad query string. If attribution flows into payment or order metadata, vary value length separately from parameter count. Reduce only the outgoing data implicated by the failure, preserve full attribution locally, and retest the original long link.

Illustrative: the clean route mounts usable fields; the ad route does not. Shortening one tracking value fixes the failure while removing an unrelated parameter does not. Inspect that value's provider boundary before changing SDK initialization. Do not replace the regression input with the shortened link.

If local fields appear but deployed fields do not, match build and route, then compare script injection and readiness. A successful build does not resolve the remote failure. Distinguish absent script request, pending load, explicit rejection, mounted frame and usable fields before choosing a repair.

## Retest the affected behavior

After a narrow patch, repeat the failing journey, a passing neighbor and the next edit: the first click can succeed while the second uses a stale key. Keep the journey, environment, expected-versus-observed result and comparison with the repair. For explicit offline assertions, use [compare checkout observations](compare-checkout-observations.md).
