class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return self._orders

    def coffees(self):
        return list({order.coffee for order in self._orders})

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        max_spent = 0
        top_customer = None
        for customer in set(order.customer for order in coffee.orders()):
            total_spent = sum(o.price for o in customer.orders() if o.coffee == coffee)
            if total_spent > max_spent:
                max_spent = total_spent
                top_customer = customer
        return top_customer
