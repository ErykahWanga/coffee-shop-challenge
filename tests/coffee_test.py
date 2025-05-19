import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order._all = []
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Coffee(123)
        with self.assertRaises(ValueError):
            Coffee("Ab")

    def test_orders(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.orders(), [order])

    def test_customers(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.customers(), [self.customer])

    def test_num_orders(self):
        Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        Order(self.customer, self.coffee, 5.0)
        Order(self.customer, self.coffee, 7.0)
        self.assertEqual(self.coffee.average_price(), 6.0)

import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):
    def setUp(self):
        Order._all = []
        self.customer = Customer("Alice")
        self.coffee = Coffee("Espresso")

    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Coffee(123)
        with self.assertRaises(ValueError):
            Coffee("Ab")

    def test_orders(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.orders(), [order])

    def test_customers(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.customers(), [self.customer])

    def test_num_orders(self):
        Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.coffee.num_orders(), 1)

    def test_average_price(self):
        Order(self.customer, self.coffee, 5.0)
        Order(self.customer, self.coffee, 7.0)
        self.assertEqual(self.coffee.average_price(), 6.0)

if __name__ == "__main__":
    unittest.main()