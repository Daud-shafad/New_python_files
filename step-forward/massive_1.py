# Challenge 1: Personal Expense Tracker

# Ask the user repeatedly (while loop) to enter expenses: name of the item and cost.

# Store items and costs in a dictionary.

# Add each cost to a list of expenses and set of unique item names.

# Convert costs to float (casting), calculate total and average (operators, numbers).

# Use if/else to categorize: expense > 100 → "high", else "low".

# At the end, print: total cost, average, all items (tuple) and unique item names (set).

expenses = {}
expense_list = []
unique_items = set()
total = 0.0

while True:
    item = input("Enter item (or 'stop' to finish): ")
    if item == "stop":
        break
    cost = float(input("Enter cost: "))
    expenses[item] = cost
    expense_list.append(cost)
    unique_items.add(item)
    total = total + cost
    if cost > 100:
        print("High expense recorded.")
    else:
        print("Low expense recorded.")

average = total / len(expense_list)
print("Total:", total)
print("Average:", average)
print("All items (tuple):", tuple(expenses.keys()))
print("Unique items (set):", unique_items)
