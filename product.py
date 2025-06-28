class Product:
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def display_product_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def update_quantity(self, quantity):
        self.quantity = quantity
        print(f"Updated quantity for {self.name}: {self.quantity}")