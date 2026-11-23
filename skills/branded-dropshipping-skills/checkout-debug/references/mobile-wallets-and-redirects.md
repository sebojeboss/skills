# Mobile wallets and redirects

## When to read

A wallet is missing or unresponsive, behavior differs in an iframe or in-app browser, the wallet sheet rejects an address, or the bank-app return lands on the wrong page.

## How to do the work

Start with the affected physical device: operating system and browser version, wallet setup, exact entry surface, origin and environment. Desktop responsive mode tests layout; it does not establish wallet eligibility. Compare the same phone through a normal browser and through the reported in-app route, keeping amount, currency and account constant. A different device's success does not isolate the cause.

Name the failed stage precisely; each has different causes:

- button missing;
- button unresponsive;
- the sheet rejects the address;
- payment stays processing;
- the return page is wrong;
- the order is missing.

**Missing wallet.** Before changing configuration, open the payment provider's own wallet demo on the same phone and browser. If the wallet is missing there too, look first at the device, browser, wallet setup and region; changing store code is unlikely to be the first fix. That does not clear the store. The demo runs on a different domain, account and payment-method setup, so once the device is shown to be eligible, your own domain registration and wallet enablement still need their own check. If the wallet shows in the demo but not in the store, the integration is the stronger suspect.

Then separate eligibility, domain association, registration, frame permissions and script readiness. A reachable association file is not proof that registration completed in the right account and environment. Re-run only the documented registration and readback path through the existing authorized integration. Check each wallet separately. If a configuration toggle and an address setting both changed before success, record the confounding rather than crediting either.

**In-app browsers.** These are their own case. Some host apps inject script into pages they display, and on some platforms that alone can disable a wallet. A top-level navigation to checkout may restore it, at the cost of leaving the app. Treat this as a hypothesis to test on the actual app and version, not a census of current app behavior.

**Unresponsive launch.** Some wallets must open synchronously from the user's tap, so integrations pre-calculate the cart before the click. That pre-calculation can trigger cart hooks or replace cart state: doubled quantities or a swapped variant only when the wallet is enabled is a clue. Moving to a top-level checkout may be a useful workaround with a navigation cost. It does not prove the embedded route is repaired. Disabling the wallet removes a buying route; label it a workaround.

**Returns and cancels.** Distinguish back/dismiss, subscription cancellation, order cancellation and refund; one "cancel" setting can serve a different one of these than the merchant intended. A successful paid state can coexist with a broken return page; that needs navigation repair, not another payment attempt. On cancel or back, read current provider state before offering a retry. Do not read a wallet sheet's cancel or dismiss event as "unpaid": in some integrations it can arrive after the payment method was already authorized. Closing a wallet sheet does not itself refund, cancel an order or end a subscription.

## Worked decisions

Illustrative: the store's domain verification file loads from a subdirectory, but registration expects the documented root path. Moving the file alone is insufficient if registration must then be repeated. Verify each wallet separately; one repaired wallet does not establish the other.
