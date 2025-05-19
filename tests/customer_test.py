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

    def test_orders(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.customer.orders(), [order])

    def test_coffees(self):
        order = Order(self.customer, self.coffee, 5.0)
        self.assertEqual(self.customer.coffees(), [self.coffee])

    def test_create_order(self):
        order = self.customer.create_order(self.coffee, 5.0)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 5.0)

    def test_most_aficionado(self):
        customer2 = Customer("Bob")
        Order(self.customer, self.coffee, 5.0)
        Order(customer2, self.coffee, 7.0)
        self.assertEqual(Customer.most_aficionado(self.coffee), customer2)

if __name__ == "__main__":
    unittest.main()