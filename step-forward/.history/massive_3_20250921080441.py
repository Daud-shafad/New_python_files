# Challenge 3: Inventory Checker

# Maintain a dictionary of items and their quantities.

# Keep asking the user (while loop) to input an item name and amount to add/remove.

# Store all transactions in a list.

# Track unique items in a set.

# Use casting for amounts to integers.

# Use if/else to check: item exists → update quantity, else → add new item.

# Use operators to update quantity.

# At the end, print full inventory (dictionary) and all unique items (set/tuple).

inventory_dict = {"laptop" : 340, "headset" : 178, "shirts" : 700, "mobiles" : 940}
print("Available items & quantities: ", inventory_dict)
while True:
    user_item_name = input("Enter the item name: ").lower()
    user_item_quantity = int(input("Enter the quantity: "))
    user_list_transaction = []
    user_list_transaction.append(user_item_name)
    user_list_transaction.append(user_item_quantity)
    