import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order._all = []
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Customer(123)
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("A" * 16)

    