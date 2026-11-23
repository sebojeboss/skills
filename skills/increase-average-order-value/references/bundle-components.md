# Bundle components

## When to read

Read when physical sets, quantity breaks, variants, stock, warehouse representation or partial returns matter. Resolve marketed parent, sellable variant, cart line and physical component separately. Expand ordered sets into units before checking shared stock. Record reservation subtraction, location constraints, stock freshness and unavailable selections. Available-for-sale stock does not establish warehouse custody or a reservation guarantee.

Map components and paid-value allocation across catalog, order, fulfillment and return records. When a return system recognizes components but cannot exchange a parent variant, repair the representation rather than simply adding another parent SKU. Decide whether an unavailable set should pause, expose a permitted standalone option, or offer an expressly accepted substitution. Preserve the sacrifice in each choice.

**Illustrative worked decisions:** two A×2+B×1 sets plus standalone A require A×5+B×2. Stock A=10/B=8 supports five sets before other demand; do not pool warehouses unless split fulfillment is supported. Contrast a locally correct map with an unsupported remote component-stock mechanism. **Output:** a component table, static capacity, unresolved identity/stock constraints, source timestamp and return/fulfillment mapping. Stock calculation does not reserve or dispatch anything.

For Whop, current documented variant stock and attributes are usable starting points. SKU uniqueness must be checked locally; a null stock value can reflect missing permission, and unlimited-stock semantics must be preserved. Component inventory, reservations and location pooling remain separate contracts. Recurring-variant quantity restrictions require an explicit representation decision, not an arbitrary quantity override.

## Check physical requirements

For each sold line, expand parent quantity into physical units and add loose units separately. Resolve IDs in the actual provider/account context. Keep location, finite or unlimited stock, reservations and observation time explicit; a permission-null value is not a stock count. Nested bundles require expansion through each level with a check against double counting.

For a finite stock scope, subtract applicable reservations, sum requirements across all lines and report shortages. A single bundle's capacity is limited by the scarcest required component after accounting for units per bundle. Two bundles sharing that component cannot both consume their entire standalone capacity. A calculation does not reserve those units. Compare stock freshness with supplier updates and demand before promising availability.

For returns, map order line, parent, physical component, units returned, paid-value allocation, condition, restock decision and exchange shipment. Resolve an unrecognized returned SKU before declaring the stock repair complete. A parent-level refund does not prove all components were returned. Refund amounts and remote catalog restrictions still follow the actual merchant/provider contract.
