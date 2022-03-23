from demo.models.store import Store
from demo.models.person import Person
import unittest


class TestStore(unittest.TestCase):
    """Unit Test for Store Class"""

    def setUp(self):
        self.person = Person("Tester1", "Second")
        self.store = Store(self.person, "shoes", 12)

    def test_store_creation(self):
        self.assertEqual(self.person.first,
                         self.store.person.first, "Failed to create store")

    def test_store_get_product_value(self):
        value = self.store.get_product_value("shoes")
        self.assertEqual(value, 12, "Get product value function failed")

    def test_store_sell(self):
        self.store.sell("shoes", 10)
        self.assertEqual(2, self.store.get_product_value(
            "shoes"), "Sell function failed ")

    def test_store_add(self):
        self.store.add("kicks", 13)
        self.assertEqual(13, self.store.get_product_value(
            "kicks"), "Add Function failed")

    def test_store_buy(self):
        self.store.buy("shoes", 8)
        self.assertEqual(20, self.store.get_product_value(
            "shoes"), "Buy function failed")

    def test_store_show_case(self):
        show_case = {"shoes": 12, "kicks": 13}
        self.assertDictEqual(show_case, self.store.show_case,
                             "show_case function failed")

    def test_store_add_value_error(self):
        with self.assertRaises(ValueError):
            self.store.add("shoes", 13)

    def tearDown(self):
        del self.store
        del self.person
        return super().tearDown()
