# You are creating a simple store management program for a small grocery shop.

# The program should do the following:

# Ask the user for their name (string) and age (integer).

# Store the name and age in variables and display a greeting like:
# "Welcome, John! You are 25 years old."

# Create a list of at least 5 grocery items (strings).

# Create a tuple containing the prices (as floats) of those items in the same order.

# Create a set containing the available payment methods (e.g., "cash", "card", "mobile").

# Create a dictionary where the keys are item names and the values are their prices.

# Ask the user which item they want to buy (string input).

# Check (using if–else) if the item exists in the dictionary:

# If it exists, display the price.

# If not, tell them "Sorry, item not found." and stop the program.

# If the item exists, ask the user how many they want to buy (integer).

# Use operators to calculate the total cost.

# If the total cost is more than 50, display "You get a discount!", otherwise "No discount for this purchase."

# Ask the user to choose a payment method and check using a match statement:

# "cash" → display "Please pay at the counter."

# "card" → display "Please insert your card."

# "mobile" → display "Please scan the QR code."

# Anything else → "Invalid payment method."

# Use a while loop to keep asking for a correct payment method until the user enters one that exists in the set.

# Cast the age to a float and display it with one decimal place.

# Use a boolean variable to check if the user is over 18; print "Adult" or "Minor" based on it.

# Step 1 & 2
customer_name = str(input("Enter your name please: "))
customer_age = int(input("Enter your age please: "))
print(f"Welcome, {customer_name}! You are {customer_age} years old.")

# Step 3, 4, 5, 6
grocery_items = ["carrots", "cabbage", "onion", "tomato", "potato"]
grocery_prices = (2.4, 3.2, 1.6, 1.8, 1.3)
grocery_payment = {"cash", "card", "mobile"}
grocery_dict = {"carrots": 2.4, "cabbage": 3.2, "onion": 1.6, "tomato": 1.8, "potato": 1.3}

# Step 7 & 8
customer_choice = str(input("Please enter the item you want to buy: "))
if customer_choice in grocery_dict:
    print(f"The price is ${grocery_dict[customer_choice]}")

    # Step 9 & 10
    num_of_items = int(input("How many of this item do you want to buy: "))
    total_cost = num_of_items * grocery_dict[customer_choice]

    # Step 11
    if total_cost > 50:
        print("You get a discount!")
    else:
        print("No discount for this purchase!")

    # Step 13 (while loop with match inside)
    while True:
        payment = input("Enter your payment method (cash, card, mobile): ")
        if payment in grocery_payment:
            match payment:
                case "cash":
                    print("Please pay at the counter.")
                case "card":
                    print("Please insert your card.")
                case "mobile":
                    print("Please scan the QR code.")
            break
        else:
            print("Invalid payment method, try again.")

    # Step 14
    age_float = float(customer_age)
    print(f"Your age as float: {age_float:.1f}")

    # Step 15
    is_adult = customer_age > 18
    if is_adult:
        print("Adult")
    else:
        print("Minor")

else:
    print("Sorry! Item not found.")
