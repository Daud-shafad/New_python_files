# 📌 Challenge:
# Create a "Mini Café Ordering System" that does the following:

# Store the café name in a variable.

# Store at least three menu items and their prices using two lists (one for items, one for prices).

# Ask the user for their name.

# Show the menu using a tuple.

# Ask the user to choose a menu item by typing its name.

# Ask how many they want (cast input to integer).

# Use if/else to check if the item exists in the menu.

# If it exists, calculate and show the total cost.

# If it doesn’t exist, show an error message.

# Ask if they want to eat in or take away using a match statement.

# Show a final confirmation message.

# End program when the order is done.

cafe_name = "joy cafe"
# items_name = ["cappucino", "tea", "coffee"]
# items_price = [5.3, 2.4, 6.8]
items_dict = {"cappucino" : 5.3, "tea": 2.4, "coffee" : 6.8}

customer_name = str(input("Enter your name please: "))
items_tuple = tuple(items_dict)
print(items_tuple)

customer_choice = str(input("Enter the item you want to buy by typing it's name: "))
number_of_items = int(input("How many of this item you want: "))

if customer_choice in items_dict:
    customer_choice_price = items_dict[customer_choice]
    total_cost = customer_choice_price * number_of_items 
    print(total_cost)
else:
    print("Item not found, error.")
    exit()

customer_situation = str(input("Do you want to (1. eat in) or (2.take away) by typing it: "))
match customer_situation:
    case "eat in":
        print("Welcome, feel relax to your choice.")
    case "take away":
        print("Thanks, have a peace out.")
    case _ :
        print("Invalid option!")

        
print("\n---------Confirmation message---------")
print(f"Welcom to {cafe_name.upper()}.")
print(f"Your name is: {customer_name.upper()}.")
print(f"You ordered a {customer_choice.upper()}")
print(f"You want {number_of_items} of this item.")
print(f"Your Total cost is: ${total_cost}.")
print(f"{customer_situation.upper()}.")
    
# i code this but using a dictionary and i cancelled the requirements which are to use lists


# in here it is the right version of the code without using a dictionary

"""

# Café Name
cafe_name = "Joy Cafe"

# Menu items (two lists: items & prices)
menu_items = ["cappuccino", "tea", "coffee"]
menu_prices = [5.3, 2.4, 6.8]

# Customer name
customer_name = input("Enter your name please: ")

# Show menu as tuple
items_tuple = tuple(menu_items)
print("Menu:", items_tuple)

# Customer order
customer_choice = input("Enter the item you want to buy by typing its name: ")
number_of_items = int(input("How many of this item you want: "))

# Check if item exists
if customer_choice in menu_items:
    index = menu_items.index(customer_choice)
    price = menu_prices[index]
    total_cost = price * number_of_items
    print(f"Total cost: ${total_cost}")
else:
    print("Item not found, error.")
    exit()

# Eat in or take away
customer_situation = input("Do you want to (eat in) or (take away) by typing it: ")

match customer_situation:
    case "eat in":
        print("Welcome, feel relaxed to your choice.")
    case "take away":
        print("Thanks, have a peace out.")
    case _:
        print("Invalid option!")

# Confirmation
print("\n---------Confirmation message---------")
print(f"Welcome to {cafe_name.upper()}.")
print(f"Your name is: {customer_name.upper()}.")
print(f"You ordered a {customer_choice.upper()}")
print(f"You want {number_of_items} of this item.")
print(f"Your Total cost is: ${total_cost}.")
print(f"{customer_situation.upper()}.")


"""