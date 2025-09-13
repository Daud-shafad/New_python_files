# Challenge 3: Shopping Cart

# Create a list: ["apple", "banana", "milk", "bread"].

# Ask the user to input an item.

# Use if/else:

# If the item is in the list → print "Item available".

# Else → print "Item not available".

items_cart_list = ["apple", "banana", "milk", "bread"]

user_item = input("Enter an item: ").lower()

if user_item in items_cart_list:
    print("Item available")
else:
    print("Item not available")
    