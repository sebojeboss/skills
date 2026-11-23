# Authorization evidence and historical matching

## When to read

Use when the cardholder denies participation, consent or recognizing the transaction, or a formal historical-evidence program is relevant.

## How to do the work

First separate recognition from authorization. A confusing statement descriptor may explain a recognition complaint, but only the actual records can link the disputed payment to an order and participant. Preserve authentication results, account events and communications with their timestamps and identifiers. Authentication shows use of credentials or a challenge; consent requires context. Address verification (AVS), card security-code match, IP address, device fingerprint and delivery each support limited propositions. None alone licenses calling the buyer fraudulent.

Construct a relation table between disputed and prior transactions: credential linkage, transaction dates, fraud-report state, recognizable login, delivery address, IP and device evidence as actually captured. Distinguish absent identifiers from mismatches. Never infer an old device observation from today's data. Shared devices, changing networks and annual purchase cadence can make an honest customer fail a history rule.

CE3 qualification is a specific network remedy, not a synonym for compelling prose. Read current official network criteria and the provider's implementation together. Check date anchors, effective version, reason/stage, matching categories, historical eligibility and permitted acquirer data. Device ID and fingerprint must not be casually counted as independent signals. If official texts disagree, retain the discrepancy and seek the applicable provider interpretation; do not pick whichever date makes the case qualify. Ordinary evidence may remain useful when program qualification fails.

## Worked decisions

Illustrative: the order account and prior purchases match, but the disputed IP differs. That can reflect a mobile network; it can also weaken a required match. Preserve both possibilities. Explain the supported account link without manufacturing CE3 eligibility. Conversely, an authentication challenge and recurring IP do not prove that a parcel arrived: if nonreceipt is also alleged, answer it separately.

## Deliverable and checks

Produce a supported narrative and a field-level qualification worksheet: observed value, source, requirement/version, match or unknown, and why it matters. Separate a dashboard eligibility banner from accepted evidence, liability shift and actual returned money. Use [provider contracts](provider-evidence-contracts.md) for current requirements.
