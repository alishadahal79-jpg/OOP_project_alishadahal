from electronics import Electronics
from clothing import Clothing
from cart import ShoppingCart
from file_manager import FileManager

# Products
laptop = Electronics(1, "Laptop", 900, 2)
phone = Electronics(2, "Phone", 700, 1)
shirt = Clothing(3, "Shirt", 50, "L")
jeans = Clothing(4, "Jeans", 80, "32")

# Polymorphism
products = [laptop, phone, shirt, jeans]

print("Available Products")
print("------------------")

for product in products:
    product.display_details()
    print()

# Shopping Cart
cart = ShoppingCart()

cart.add_product(laptop, 1)
cart.add_product(shirt, 2)
cart.add_product(jeans, 1)

subtotal, discount, tax, total = cart.checkout()

print("====== BILL ======")
print(f"Subtotal : ${subtotal:.2f}")
print(f"Discount : ${discount:.2f}")
print(f"Tax : ${tax:.2f}")
print(f"Total : ${total:.2f}")

# Save order
FileManager.save_order(cart)

print("\nOrder saved successfully to orders.txt")