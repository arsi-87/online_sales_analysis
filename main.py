from product_manager import ProductManager
from product import Product

product_manager = ProductManager()

product1 =Product ("Laptop", 750, 7)
product2 = Product("Mouse", 35,12)
product3 =Product ("Tv", 550, 4)

product_manager.add_product(product1)
product_manager.add_product(product2)
product_manager.add_product(product3)


print("Products in inventory:\n")
product_manager.all_products()

product_manager.total_value()
print() 