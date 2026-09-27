# bloom_utils

A small Python utility library for small-business operations — built for
managing pricing, discounts, and stock for **Bloom Eatery** and **Bloom Luxe**.

## Features

- **Pricing** (`bloom_utils.pricing`)
  - `apply_discount(price, percent)` — apply a percentage discount to a price
  - `bulk_price(unit_price, quantity, bulk_threshold, bulk_discount_percent)` —
    calculate total price with an automatic bulk discount
  - `format_cedis(amount)` — format a number as a Ghanaian cedi string

- **Inventory** (`bloom_utils.inventory`)
  - `Inventory` class — track stock levels per item
    - `add_stock(item, quantity)`
    - `remove_stock(item, quantity)`
    - `get_stock(item)`
    - `low_stock_items()`
    - `all_stock()`

## Installation

Clone the repo and install locally:

```bash
git clone https://github.com/<your-username>/bloom_utils.git
cd bloom_utils
pip install -e .
```

## Usage

```python
from bloom_utils import apply_discount, bulk_price, format_cedis
from bloom_utils.inventory import Inventory

# Pricing
price = apply_discount(200, 15)          # 170.0
total = bulk_price(20, 12)               # bulk discount applied automatically
print(format_cedis(total))               # GH₵ 216.00

# Inventory
inv = Inventory(low_stock_threshold=5)
inv.add_stock("bikini-top-M", 20)
inv.remove_stock("bikini-top-M", 17)
print(inv.low_stock_items())             # ['bikini-top-M']
```

## Running tests

```bash
python -m unittest discover -v tests
```

## Author

Dorcas Agyenim Boateng (Dee) — BIT student, KNUST School of Business.

## License

MIT
