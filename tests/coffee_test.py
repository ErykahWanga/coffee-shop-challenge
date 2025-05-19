import unittest
from coffee import Coffee
from customer import Customer

class TestCoffee(unittest.TestCase):

    def test_valid_name(self):
        c = Coffee("Espresso")
        self.assertEqual(c.name, "Espresso")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("ab")

    def test_num_orders_and_average_price(self):
        c = Coffee("Cappuccino")
        cust = Customer("Emma")
        cust.create_order(c, 5.0)
        cust.create_order(c, 7.0)
        self.assertEqual(c.num_orders(), 2)
        self.assertEqual(c.average_price(), 6.0)

if __name__ == '__main__':
    unittest.main()
