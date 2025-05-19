import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def test_valid_order(self):
        c = Customer("Dan")
        coffee = Coffee("Mocha")
        o = Order(c, coffee, 4.5)
        self.assertEqual(o.customer, c)
        self.assertEqual(o.coffee, coffee)
        self.assertEqual(o.price, 4.5)

    def test_invalid_customer(self):
        with self.assertRaises(TypeError):
            Order("NotCustomer", Coffee("Latte"), 3.0)

    def test_invalid_coffee(self):
        with self.assertRaises(TypeError):
            Order(Customer("Mia"), "NotCoffee", 3.0)

    def test_invalid_price(self):
        c = Customer("Tim")
        coffee = Coffee("Flat White")
        with self.assertRaises(ValueError):
            Order(c, coffee, 0.5)
        with self.assertRaises(ValueError):
            Order(c, coffee, 11.0)
        with self.assertRaises(ValueError):
            Order(c, coffee, "ten")

if __name__ == '__main__':
    unittest.main()
