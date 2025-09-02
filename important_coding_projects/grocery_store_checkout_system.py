# Program Challenge 1: Grocery Store Checkout System

# Step 1. Create variables for store name (string), is_store_open (boolean), 
# and a running total (number).
# Step 2. Define a list of product names (strings).
# Step 3. Define a tuple of product categories (e.g., Fruits, Drinks, Snacks) just to display.
# Step 4. Define a set to hold the unique items the user purchases (to avoid duplicates).
# Step 5. Define a dictionary mapping product name → price (numbers).
# Step 6. Ask the user for their name (string) and greet them using string formatting.
# Step 7. Ask if the store is open today using a yes/no input, convert it to a boolean,
# and if/else: if closed, print a message and stop; if open, continue.
# Step 8. Start a while loop that keeps asking the user to type a product name 
# to add, or "done" to finish.
# Step 9. Inside the loop, if/else: if the product is not a dictionary key, 
# show “not found” and continue the loop.
# Step 10. If the product exists, ask for the quantity, cast to integer, 
# validate it (>0) with if/else.
# Step 11. Use operators to compute line cost = price × quantity,
# add to the running total, and add the product name to the set of purchased items.
# Step 12. After the loop ends, use if/else to apply a discount rule 
# (e.g., if total > 50, apply 10% off) and compute the final total with operators.
# Step 13. Ask for payment method as a string and use a 
# match statement: "cash", "card", "mobile" → print specific instructions; 
# anything else → “invalid method.”
# Step 14. Display a receipt showing: store name (uppercase), 
# customer name (uppercase), list of purchased items (from the set),
# subtotal, discount (if any), and final total.
# Step 15. Print a final boolean check like cart_is_empty (True if total is 0), 
# and an appropriate message using if/else.


# Program Challenge 1: Grocery Store Checkout System

# Step 1
store_name = "Maverick Grocery"
is_store_open = True
running_total = 0.0

# Step 2
products = ["apple", "banana", "juice", "chips", "water"]

# Step 3
categories = ("Fruits", "Drinks", "Snacks")

# Step 4
purchased_items = set()

# Step 5
product_prices = {
    "apple": 1.5,
    "banana": 0.8,
    "juice": 2.5,
    "chips": 3.0,
    "water": 1.0
}

# Step 6
customer_name = input("Enter your name: ")
print(f"Welcome, {customer_name}!")

# Step 7
open_input = input("Is the store open today? (yes/no): ").lower()
if open_input == "yes":
    is_store_open = True
else:
    is_store_open = False

if not is_store_open:
    print("Sorry, the store is closed today.")
else:
    # Step 8
    while True:
        product = input("Enter a product to add (or type 'done' to finish): ").lower()
        
        if product == "done":
            break

        # Step 9
        if product not in product_prices:
            print("Product not found. Try again.")
            continue

        # Step 10
        quantity = input(f"Enter quantity for {product}: ")
        quantity = int(quantity)

        if quantity <= 0:
            print("Invalid quantity. Must be greater than 0.")
            continue

        # Step 11
        line_cost = product_prices[product] * quantity
        running_total = running_total + line_cost
        purchased_items.add(product)
        print(f"Added {quantity} x {product} → ${line_cost:.2f}")

    # Step 12
    discount = 0
    if running_total > 50:
        discount = running_total * 0.1
        running_total = running_total - discount

    # Step 13
    payment_method = input("Enter payment method (cash/card/mobile): ").lower()

    match payment_method:
        case "cash":
            print("Please pay with cash at the counter.")
        case "card":
            print("Please insert or swipe your card.")
        case "mobile":
            print("Please scan the QR code for mobile payment.")
        case _:
            print("Invalid payment method.")

    # Step 14
    print("\n=== RECEIPT ===")
    print("STORE:", store_name.upper())
    print("CUSTOMER:", customer_name.upper())
    print("ITEMS PURCHASED:", purchased_items)
    print("SUBTOTAL:", f"${running_total + discount:.2f}")
    print("DISCOUNT:", f"${discount:.2f}")
    print("FINAL TOTAL:", f"${running_total:.2f}")

    # Step 15
    cart_is_empty = running_total == 0
    if cart_is_empty:
        print("Your cart is empty.")
    else:
        print("Thank you for shopping with us!")
