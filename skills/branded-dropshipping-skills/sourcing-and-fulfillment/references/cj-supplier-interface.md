# CJ supplier interface

## When to read

The selected source is CJ, a CJ connection exists/is requested, or product, variant, freight and warehouse facts need its interface.

## How to do the work

When CJ is the selected supplier, discover the available tools and effective account before relying on the connection. Documented reads include search_products, query_sku_details, calculate_freight, get_logistics_timeliness and list_shops. Query an exact variant and destination; record freight inclusion, warehouse/service and observation date. A warehouse list is not a reserved-stock acknowledgment.

Check shop authorization separately from exact product mapping, then supplier order acceptance and tracking return. No generic serum, accessory or image match substitutes for the actual SKU. If the variant or destination service is absent, return a conditional candidate and a precise gap instead of substituting silently.

CJ tools can also create orders, add carts, merge orders or open disputes. Select only the operation authorized by the task. Inspect actual outbound data and logging before adopting a local server. Keep token-bearing remote configuration in the intended credential mechanism, never in report text. After an uncertain supplier-order write, query by the original reference before retrying. If no connection exists, finish public catalog discovery and local comparison from supplied evidence; account stock/order facts remain unknown.

Official dependency: https://developers.cjdropshipping.com/en/api/api2/mcp.html. Verify access to the required operation in the selected CJ account and inspect the actual order mapping before relying on synchronization.

## Deliverable and checks

Exact supplier-SKU/route quote snapshot, connection-state diagnosis and mapping gap list. Do not imply CJ is the universal required supplier or that its published tool list has been executed here.
