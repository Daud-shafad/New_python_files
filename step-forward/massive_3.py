# Challenge 3: Inventory Checker

# Maintain a dictionary of items and their quantities.

# Keep asking the user (while loop) to input an item name and amount to add/remove.

# Store all transactions in a list.

# Track unique items in a set.

# Use casting for amounts to integers.

# Use if/else to check: item exists → update quantity, else → add new item.

# Use operators to update quantity.

# At the end, print full inventory (dictionary) and all unique items (set/tuple).

# Challenge 13: Inventory Checker
inventory = {}
transactions = []
unique_items = set()

while True:
    action = input("Enter item (or 'stop'): ")
    if action == "stop":
        break
    qty = int(input("Enter quantity (+ to add, - to remove): "))
    transactions.append((action, qty))
    unique_items.add(action)

    if action in inventory:
        inventory[action] = inventory[action] + qty
    else:
        inventory[action] = qty

print("Final Inventory:", inventory)
print("Transactions List:", transactions)
print("Unique Items (set):", unique_items)

    