import unittest
from customer import Customer
from coffee import Coffee

class TestCustomer(unittest.TestCase):

    def test_valid_name(self):
        c = Customer("Alice")
        self.assertEqual(c.name, "Alice")

    def test_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("")
        with self.assertRaises(ValueError):
            Customer("a" * 16)

    def test_create_order_and_coffees(self):
        c = Customer("Bob")
        latte = Coffee("Latte")
        c.create_order(latte, 3.5)
        c.create_order(latte, 4.5)
        self.assertEqual(len(c.orders()), 2)
        self.assertIn(latte, c.coffees())
        self.assertEqual(len(c.coffees()), 1)

if __name__ == '__main__':
    unittest.main()
