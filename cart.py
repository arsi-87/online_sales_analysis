class Cart:
    def __init__(self):
        self.cart_items = []
        
    def add_products(self, product):
        self.cart_items.append(product)
        
    def total_value(self):
        return sum(product.price for product in self.cart_items)
    
    def display_cart(self):
        for product in self.cart_items:
            print(f"{product.name}:{product.price}")