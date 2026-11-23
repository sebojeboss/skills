# Shopify checkout contracts

## When to read

The merchant uses Shopify theme Ajax, Storefront API, Cart Transform or order APIs.

## How to do the work

Theme Ajax, Storefront GraphQL and Admin order APIs have different identity and permission contracts, so identify which one is in play. Use https://shopify.dev/docs/api/ajax/reference/cart for current theme-cart operations and section rendering. Build locale-aware routes from the current store rather than hardcoding a root path. Inspect add/change/update response semantics before choosing a mutation.

**Targeting a line.** When several lines share a variant, target one with the supported current line identifier, and preserve properties and selling plans. After a mutation, take the next target from the returned cart. Keys can change when properties or discount application change. A null section or missing HTML in the response does not necessarily mean the cart write failed. Repair the renderer without blindly replaying the mutation. Pending asynchronous shipping calculation can also return empty values that are not errors.

**Bundles.** Establish whether the integration expands, merges or merely displays independent lines. Check the active Cart Transform/API version and the affected sales channel and checkout layout: web success does not prove POS equivalence, and one checkout layout can keep a valid neighbor that another drops.

**Readback.** Use the current Admin schema to read order-line and fulfillment-line quantities. Traversing from a fulfillment line back to its order line changes the question.

**Workarounds.** A historical forum workaround is not a current API guarantee. Check the workaround against the current API version and the affected cart, checkout and order records before applying it.

## Worked decisions

Illustrative: Ajax returns the changed cart while a drawer section fails. Recover the rendering and refresh line identity. Verify the next change and an unrelated line before claiming repair.
