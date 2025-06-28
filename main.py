from product_manager import ProductManager
from product import Product
from cart import Cart
import random

product_manager = ProductManager()

product1 = Product("Laptop", 750, 7)
product2 = Product("Mouse", 35,12)
product3 = Product("Tv", 550, 4)
product4 = Product("Headphones", 25, 12)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)
product_manager.add_product(product4)

cart = Cart()

selected_products = random.sample(product_manager.products, 3)

for product in selected_products:
    cart.add_products(product)
    
print("\nProducts in cart:")
cart.display_cart()
print(f"Total: {cart.total_value()}\n")



print("Products in inventory:\n")
product_manager.all_products()

product_manager.total_value()
print() 