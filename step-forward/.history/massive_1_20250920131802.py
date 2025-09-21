# Challenge 1: Personal Expense Tracker

# Ask the user repeatedly (while loop) to enter expenses: name of the item and cost.

# Store items and costs in a dictionary.

# Add each cost to a list of expenses and set of unique item names.

# Convert costs to float (casting), calculate total and average (operators, numbers).

# Use if/else to categorize: expense > 100 → "high", else "low".

# At the end, print: total cost, average, all items (tuple) and unique item names (set).

total = 0
average = 0
while True:
    user_name_item = input("Enter the name of the item type 'exit' to finish: ").lower()
    user_cost_item = int(input("Enter the cost of the item: "))
    if user_name_item == "exit" and user_cost_item == "exit":
        break
    else: 
        user_expenses_tracker = {}
        user_expenses_tracker.update({user_name_item : user_cost_item})
        list_of_expenses = []
        list_of_expenses.append(user_cost_item)
        unique_item_names = {()}
        unique_item_names.add(user_name_item)
        user_cost_item = float(user_cost_item)
total += user_cost_item
average = total / user_cost_item
    
if total > 100:
        print("High")
else: 
        print("Low")
        
print(total)
print(average)
print(tuple(list_of_expenses))
print(unique_item_names)