import string
from typing import Optional
from pydantic import BaseModel, validator, root_validator
from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    email: str

class Order(BaseModel):
    product_name: str
    quantity: int
    customer_email: str

class ShoppingCart:
    def __init__(self):
        self.customers = []
        self.orders = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def add_order(self, order: Order):
        self.orders.append(order)

    def process_orders(self):
        for order in self.orders:
            self.process_order(order)

    def process_order(self, order: Order):
        # Processa l'ordine
        customer = self.find_customer_by_email(order.customer_email)
        if customer:
            print(f"Ordine per il cliente: {customer.name}, Prodotto: {order.product_name}, Quantità: {order.quantity}")
        else:
            print("Cliente non trovato.")

    def find_customer_by_email(self, email: str):
        # Trova il cliente corrispondente all'email
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None

# Utilizzo della classe ShoppingCart
shopping_cart = ShoppingCart()

customer1 = Customer(name="Alice", email="alice@example.com")
customer2 = Customer(name="Bob", email="bob@example.com")
shopping_cart.add_customer(customer1)
shopping_cart.add_customer(customer2)

order1 = Order(product_name="Prodotto 1", quantity=2, customer_email="alice@example.com")
order2 = Order(product_name="Prodotto 2", quantity=1, customer_email="bob@example.com")
shopping_cart.add_order(order1)
shopping_cart.add_order(order2)

shopping_cart.process_orders()
