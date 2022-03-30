from demo.models.store import Store
from demo.models.person import Person
import unittest


class TestIntegration(unittest.TestCase):
    """Integration Test of Workflow"""

    def setUp(self):
        self.tester = Person("Tester", "Integration")
        self.store_workflow = Store(self.tester)

    def test_worflow(self):
        self.store_workflow.add("soap", 23)
        self.assertEqual(23, self.store_workflow.get_product_value("soap"))

        self.store_workflow.buy("soap", 10)
        self.assertEqual(33, self.store_workflow.get_product_value("soap"))

        self.store_workflow.sell("soap", 7)
        self.assertEqual(26, self.store_workflow.get_product_value("soap"))

        self.store_workflow.add("water", 11)
        store_workflow_products = dict([("soap", 26), ("water", 11)])
        self.assertDictEqual(store_workflow_products,
                             self.store_workflow.show_case)

    def tearDown(self):
        del self.store_workflow
        del self.tester
        return super().tearDown()
