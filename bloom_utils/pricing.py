"""
pricing.py

Helpers for working out prices, discounts and cedi-formatted amounts.
"""


def apply_discount(price: float, percent: float) -> float:
    """
    Apply a percentage discount to a price.

    Args:
        price: The original price (must be >= 0).
        percent: The discount percentage, e.g. 15 for 15% off.

    Returns:
        The discounted price, rounded to 2 decimal places.

    Raises:
        ValueError: If price is negative, or percent is not between 0 and 100.
    """
    if price < 0:
        raise ValueError("price cannot be negative")
    if not (0 <= percent <= 100):
        raise ValueError("percent must be between 0 and 100")

    discounted = price * (1 - percent / 100)
    return round(discounted, 2)


def bulk_price(unit_price: float, quantity: int, bulk_threshold: int = 10,
                bulk_discount_percent: float = 10) -> float:
    """
    Calculate the total price for a quantity of items, applying a bulk
    discount automatically once the quantity meets the threshold.

    Args:
        unit_price: Price per single item.
        quantity: Number of items being bought.
        bulk_threshold: Minimum quantity to qualify for the bulk discount.
        bulk_discount_percent: Discount percentage applied when the
            threshold is met.

    Returns:
        The total price, rounded to 2 decimal places.

    Raises:
        ValueError: If unit_price is negative or quantity is not positive.
    """
    if unit_price < 0:
        raise ValueError("unit_price cannot be negative")
    if quantity <= 0:
        raise ValueError("quantity must be a positive integer")

    total = unit_price * quantity

    if quantity >= bulk_threshold:
        total = apply_discount(total, bulk_discount_percent)

    return round(total, 2)


def format_cedis(amount: float) -> str:
    """
    Format a numeric amount as a Ghanaian cedi string.

    Args:
        amount: The amount to format.

    Returns:
        A string like "GH₵ 150.00".
    """
    return f"GH\u20b5 {amount:,.2f}"
