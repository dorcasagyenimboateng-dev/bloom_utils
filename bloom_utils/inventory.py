"""
inventory.py

A lightweight in-memory stock tracker for a small shop or eatery.
"""


class StockError(Exception):
    """Raised when a stock operation can't be completed (e.g. overselling)."""


class Inventory:
    """
    Tracks stock levels for named items.

    Example:
        >>> inv = Inventory()
        >>> inv.add_stock("bikini-top-M", 20)
        >>> inv.remove_stock("bikini-top-M", 5)
        >>> inv.get_stock("bikini-top-M")
        15
    """

    def __init__(self, low_stock_threshold: int = 5):
        self._stock = {}
        self.low_stock_threshold = low_stock_threshold

    def add_stock(self, item: str, quantity: int) -> None:
        """Add quantity of an item to stock. Creates the item if new."""
        if quantity <= 0:
            raise ValueError("quantity to add must be positive")
        self._stock[item] = self._stock.get(item, 0) + quantity

    def remove_stock(self, item: str, quantity: int) -> None:
        """
        Remove quantity of an item from stock (e.g. on a sale).

        Raises:
            StockError: If the item doesn't exist or there isn't enough stock.
        """
        if quantity <= 0:
            raise ValueError("quantity to remove must be positive")
        current = self._stock.get(item)
        if current is None:
            raise StockError(f"'{item}' is not tracked in inventory")
        if quantity > current:
            raise StockError(
                f"cannot remove {quantity} of '{item}'; only {current} in stock"
            )
        self._stock[item] = current - quantity

    def get_stock(self, item: str) -> int:
        """Return current stock level for an item (0 if untracked)."""
        return self._stock.get(item, 0)

    def low_stock_items(self) -> list:
        """
        Return a list of items at or below the low-stock threshold.
        """
        return [
            item for item, qty in self._stock.items()
            if qty <= self.low_stock_threshold
        ]

    def all_stock(self) -> dict:
        """Return a copy of the full stock dictionary."""
        return dict(self._stock)
