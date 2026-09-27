import unittest

from bloom_utils import apply_discount, bulk_price, format_cedis
from bloom_utils.inventory import Inventory, StockError


class TestPricing(unittest.TestCase):

    def test_apply_discount_basic(self):
        self.assertEqual(apply_discount(100, 10), 90.0)

    def test_apply_discount_zero_percent(self):
        self.assertEqual(apply_discount(50, 0), 50.0)

    def test_apply_discount_invalid_percent(self):
        with self.assertRaises(ValueError):
            apply_discount(50, 150)

    def test_apply_discount_negative_price(self):
        with self.assertRaises(ValueError):
            apply_discount(-10, 10)

    def test_bulk_price_under_threshold(self):
        # 5 items at 20 each, threshold is 10 -> no discount
        self.assertEqual(bulk_price(20, 5), 100.0)

    def test_bulk_price_meets_threshold(self):
        # 10 items at 20 each = 200, 10% off = 180
        self.assertEqual(bulk_price(20, 10), 180.0)

    def test_bulk_price_invalid_quantity(self):
        with self.assertRaises(ValueError):
            bulk_price(20, 0)

    def test_format_cedis(self):
        self.assertEqual(format_cedis(1500), "GH\u20b5 1,500.00")


class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inv = Inventory(low_stock_threshold=5)

    def test_add_and_get_stock(self):
        self.inv.add_stock("shea-butter-200ml", 20)
        self.assertEqual(self.inv.get_stock("shea-butter-200ml"), 20)

    def test_remove_stock(self):
        self.inv.add_stock("shea-butter-200ml", 20)
        self.inv.remove_stock("shea-butter-200ml", 8)
        self.assertEqual(self.inv.get_stock("shea-butter-200ml"), 12)

    def test_remove_stock_untracked_item(self):
        with self.assertRaises(StockError):
            self.inv.remove_stock("unknown-item", 1)

    def test_remove_stock_too_much(self):
        self.inv.add_stock("jollof-pan", 3)
        with self.assertRaises(StockError):
            self.inv.remove_stock("jollof-pan", 10)

    def test_low_stock_items(self):
        self.inv.add_stock("jollof-pan", 3)
        self.inv.add_stock("shea-butter-200ml", 20)
        self.assertIn("jollof-pan", self.inv.low_stock_items())
        self.assertNotIn("shea-butter-200ml", self.inv.low_stock_items())


if __name__ == "__main__":
    unittest.main()
