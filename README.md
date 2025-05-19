# coffee-shop-challenge
Coffee Shop Challenge
A Python-based implementation of a coffee shop domain model, featuring Customer, Coffee, and Order classes with relationships and aggregates.
Setup

Clone the repository:
git clone git@github.com:<your-username>/coffee-shop-challenge.git
cd coffee-shop-challenge


Set up the Python environment:
pipenv install
pipenv shell


Run tests:
python -m unittest discover tests


Run the debug script:
python debug.py



Models

Customer: Manages customer name (1–15 chars) and orders.
Coffee: Manages coffee name (≥3 chars) and orders.
Order: Links customers to coffees with a price (1.0–10.0).

Features

Relationships: Customer.orders(), Customer.coffees(), Coffee.orders(), Coffee.customers().
Aggregates: Customer.create_order(), Coffee.num_orders(), Coffee.average_price().
Bonus: Customer.most_aficionado(coffee) to find the highest spender on a coffee.

Running Tests
Tests are located in the tests/ directory and cover all functionality, including edge cases.
python -m unittest discover tests

