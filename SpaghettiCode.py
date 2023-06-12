import string
from typing import Optional
from pydantic import BaseModel, validator, root_validator

from pydantic import BaseModel

class Order(BaseModel):
    product_name: str
    quantity: int

class OrderProcessor:
    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def process_orders(self):
        for order in self.orders:
            self.process_order(order)

    def process_order(self, order: Order):
        self.validate_order(order)
        self.perform_order_operations(order)

    def validate_order(self, order: Order):
        # Validazione dell'ordine
        if order.quantity <= 0:
            raise ValueError("La quantità dell'ordine deve essere maggiore di zero.")
        # Altre validazioni...

    def perform_order_operations(self, order: Order):
        # Operazioni sull'ordine
        self.update_inventory(order)
        self.send_order_confirmation(order)

    def update_inventory(self, order: Order):
        # Aggiornamento dell'inventario
        pass

    def send_order_confirmation(self, order: Order):
        # Invio di una conferma dell'ordine
        print(f"Ordine confermato: {order.product_name}, Quantità: {order.quantity}")

# Utilizzo della classe OrderProcessor
order1 = Order(product_name="Prodotto 1", quantity=2)
order2 = Order(product_name="Prodotto 2", quantity=1)

processor = OrderProcessor()
processor.add_order(order1)
processor.add_order(order2)
processor.process_orders()
