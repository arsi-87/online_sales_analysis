class ProductManager:
    def __init__(self):
        self.products = []
        
    def add_product(self, product):
        self.products.append(product)
        
    def all_products(self):
        if not self.products:
            print("No products.")
        else:    
            for product in self.products:
                product.display_product_info()
                
    def total_value(self):
        total = sum(product.price * product.quantity for product in self.products )
        print(f"Total value of products is: {total}")