"""
bloom_utils
~~~~~~~~~~~

A small Python utility library for small-business operations
(pricing, discounts, currency formatting, and stock/inventory tracking).

Originally built for Bloom Eatery and Bloom Luxe.
"""

from .pricing import apply_discount, bulk_price, format_cedis
from .inventory import Inventory, StockError

__version__ = "0.1.0"

__all__ = [
    "apply_discount",
    "bulk_price",
    "format_cedis",
    "Inventory",
    "StockError",
]
