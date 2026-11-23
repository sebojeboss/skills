# Bundle quantities and allocation

## When to read

Quantity two, bundles plus loose units, split price rows, or a valid line disappearing near a stock boundary.

## How to do the work

Write the component table before touching the theme. For each parent, record:

- the parent identity and the selected parent quantity;
- each component variant and its units per parent;
- any separately added loose units.

Multiply parent quantity by each component multiplier, then add loose units. Keep a second table of relations. Matching totals for one component cannot disguise allocation to the wrong parent: two rows can sum correctly while belonging to different bundles. Compare these expectations through cart, checkout and order artifacts as far as access permits. Never suppress a loose unit just because its variant also appears inside a bundle.

Choose the bundle model before blaming the widget. Adding several independent items is different from expanding one parent into components. Ask where quantities and prices originate and where they are transformed. A raw configuration field that duplicates a displayed total is a maintenance trap: when one changes and the other does not, they diverge.

Use a contrast relevant to the suspected mechanism:

- a bundle alone versus a bundle plus a loose component;
- two distinct bundles sharing a component;
- available quantity versus the stock boundary;
- the affected channel or checkout layout versus another.

These isolate hypotheses; they do not prove universal platform defects. When one bundle becomes unavailable and a valid neighboring bundle disappears with it, read the full returned cart, not just the visible error. When a quantity just over the stock limit silently returns fewer bundles than requested, parent and component inventory are separate constraints; check which one bound.

Price fragments can be correct. A bundle total that cannot divide evenly into currency precision may spread units across two adjacent prices. Sum units and exact amounts before declaring duplication. Do not filter every row with a component variant out of an email, because that erases loose units. Prefer the relationships the actual order contract provides. If they are absent, report the ambiguity rather than inventing a bundle group. Changing the offer price to avoid allocation is an offer decision, not a debugging fix.

## Worked decisions

Illustrative: a kit contains A×2 and B×1. Two kits plus one loose A imply A×5 and B×2. Correct aggregate units can still have wrong parent links. Cent allocation can split rows without losing merchandise, and hiding duplicate-looking rows can conceal the loose A.
