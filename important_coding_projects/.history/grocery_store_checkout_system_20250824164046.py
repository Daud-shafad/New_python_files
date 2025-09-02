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


store_name = "shafad"
is_store_open = True
store_running_years = 8