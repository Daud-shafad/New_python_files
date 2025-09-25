# Challenge 1: Personal Expense Tracker

# Ask the user repeatedly (while loop) to enter expenses: name of the item and cost.

# Store items and costs in a dictionary.

# Add each cost to a list of expenses and set of unique item names.

# Convert costs to float (casting), calculate total and average (operators, numbers).

# Use if/else to categorize: expense > 100 → "high", else "low".

# At the end, print: total cost, average, all items (tuple) and unique item names (set).

expenses_dict = {}
expenses_list = []
expenses_unique_set_items = set()
total = 0.0

while True:
    customer_item = input("Enter an item name 'type 'stop' to finish': ")
    if customer_item == "stop":
            break
    
    customer_cost = float(input("Enter the cost of the item: "))
  
    expenses_dict[customer_item] = customer_cost
    expenses_list.append(customer_cost)
    expenses_unique_set_items.add(customer_cost)
     
    total = total + customer_cost
    
    if total > 100:
        print("High expenses")
    else:
        print("Low expenses")
    average = total / len(expenses_list)
    print(total)
    print(average)
    print(tuple(expenses_dict.keys()))
    print(expenses_unique_set_items)
    