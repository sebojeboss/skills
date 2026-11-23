# Payouts, reserves and account state

## When to read

Read when proceeds are late, a reserve or hold notice has arrived, withdrawals are paused, or the merchant is weighing a processor switch to get cash moving.

## Read the situation

Start from the notice and the balance buckets, not the dashboard headline. For each amount, write down its currency, the bucket it sits in (pending, available, reserved, held for review, in transit to the bank), the notice or rule that controls it, the date you expect it to move and the date it actually moved. Ordinary settlement delay, a reserve, a compliance or verification review and a failed bank destination can all be true at once, and a different party fixes each one. Do not add overlapping dashboard totals together.

A processor sizes a reserve against the refunds and disputes it expects to inherit if the store stops delivering. Dropshipping builds that exposure in: money arrives days after the sale, goods arrive weeks later, and complaints arrive after that. Fast growth on a young account, long or unreliable delivery, and rising refunds all read as risk from the processor's side, even before any chargeback. A low chargeback count does not settle the question. If dispute alerts are automatically refunding buyers, the chargeback ratio can look clean while refunds climb, and the reserve has every reason to stay.

Reserve shapes differ. [Stripe's fixed and rolling plans](https://support.stripe.com/topics/reserves) distinguish a common scheduled release date from portions that release as each transaction ages. Other providers may use the same labels for different arrangements. Read the actual plan: what is withheld, what can consume it, and what date or condition releases each amount? A review can change the percentage, the holding period, or neither. A missed expected date calls for checking the notice and restriction; it does not by itself establish what the merchant is entitled to withdraw.

## Decisions that change the outcome

- **Keep fulfilling from cash you control.** A hold turns into a crisis when supplier payments depend on the held money. If suppliers can't be paid without it, slow new orders to what accessible cash can fulfill, before late deliveries generate the next round of disputes.
- **Fix the cause before asking for release.** A release request is strongest when it shows delivered orders, falling refunds, and the change that removed the complaint driver: an honest delivery promise, clear bundle contents, a cancellation path that works. Releasing funds does not remove the reason for the hold; if the offer, delivery times and refund drivers are unchanged, the same exposure is still there at the next review.
- **A new processor is not a cash remedy.** Moving volume elsewhere can keep new sales flowing, but the old balance stays under the old terms, and the new provider may review the business within days and ask for the same supplier, inventory and fulfillment evidence.
- **Release and withdrawal are separate events.** A reserve ending, money appearing in a balance, permission to transfer, a payout being sent and the bank receiving it are five different events. Check each one. Changing a payout schedule can change when available funds are sent without shortening settlement or releasing a reserve.

## Use proceeds without waiting for a bank payout

For an approved Whop Card, check what is already spendable or eligible to load. Paying an accepted business expense directly can remove the wait for bank receipt. Eligible pending-funds access can also bridge part of settlement, but read the quoted amount, advance fee and remaining allowance first. Reserved funds and a top-up still in transit cannot pay today's bill. Keep the bank route for payees that require it or when earlier access costs more than it earns.

Separate incoming sales awaiting settlement, a card load in transit and outgoing card authorizations. The same proceeds cannot fund both the card and a future bank payout. Earlier access changes timing, not product margin or CAC payback.

Be wary of advice that promises a hold can never exceed a fixed percentage, that ageing a test store prevents future holds, or that a wrongful ban is always reversed quickly. Work from the notice in front of you.

## Worked decisions

Illustrative: held funds total 4,000 units, but dated unlock tranches explain only 2,500. Show 1,500 as undated rather than distributing it across the visible schedule. If the first tranche releases while withdrawals remain restricted, investigate destination/account state separately. A review date is not guaranteed bank receipt. Prepare an unsent escalation with the exact missing statement or restriction reference; do not promise an appeal tactic or universal release period.

Illustrative: a store selling one imported product has grown quickly on a new account and has just received a notice withholding part of each day's sales on a rolling basis. Its next supplier payment is due before the first tranche ages out. The useful plan is not an appeal letter first: it is a cash schedule that shows how many orders accessible cash can fulfill, a slower order intake until that schedule balances, and a release request once delivery confirmations and refund figures show the exposure falling. Switching processors mid-hold would leave the withheld money where it is.

## Deliverable and checks

Return a payout-state brief (amount, currency, bucket, controlling notice, expected and observed dates, next evidence), dated availability scenarios and an unsent escalation draft when needed. Name what was actually inspected and the missing notice or record that could change the conclusion.

## Related work

Read [settlement and reconciliation](settlement-and-reconciliation.md) when deposits and balance movements need a bridge.
