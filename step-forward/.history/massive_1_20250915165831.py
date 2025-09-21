# Challenge 1: Personal Expense Tracker

# Ask the user repeatedly (while loop) to enter expenses: name of the item and cost.

# Store items and costs in a dictionary.

# Add each cost to a list of expenses and set of unique item names.

# Convert costs to float (casting), calculate total and average (operators, numbers).

# Use if/else to categorize: expense > 100 → "high", else "low".

# At the end, print: total cost, average, all items (tuple) and unique item names (set).


while True:
    user_name_item = input("Enter the name of the item: ").lower()
    user_cost_item = int(input("Enter the cost of the item: "))
    user_expenses_tracker = {}
    user_expenses_tracker.update({user_name_item : user_cost_item})
    list_of_expenses = []
    list_of_expenses.append(user_cost_item)
    unique_item_names = {()}
    unique_item_names.add(user_name_item)
    user_cost_item = float(user_cost_item)
    
    num_of_expenses = list_of_expenses[user_cost_item]
    total_expenses = user_cost_item * num_of_expenses