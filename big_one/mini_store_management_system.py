# You are creating a simple console-based program for a mini store. The store sells different items, offers discounts, and has different customer types.

# Steps & Requirements

# Store your store name (string), store opening year (integer), and is_store_open (boolean).

# Ask the user for the current year and calculate how many years the store has been running (use casting if needed).

# Display a welcome message using string concatenation and f-strings.

# Convert the store name to uppercase in one print statement.

# Create a list of at least 5 products sold in the store. Display them to the user.

# Create a tuple of fixed product categories (e.g., “Fruits”, “Drinks”, “Snacks”). Display them.

# Create a set of unique discount codes (e.g., {"SALE10", "VIP20", "WELCOME5"}). Display them.

# Create a dictionary of products with their prices, for example:

# Ask the user if they are a “regular” or “VIP” customer. If VIP, give them a 10% discount.

# Ask the user to choose a payment method (1: Cash, 2: Card, 3: MobilePay) and print the payment type using a match statement.

# Keep asking the user to enter products they want to buy until they type “done”.

# Add the prices to a running total.

# Calculate total cost, apply discounts if any, and display the final bill.

# Use a boolean to check if the store is open or closed before starting the shopping process.

# Final Output

# Show: store name, years in business, customer type, list of purchased items, total before discount, discount applied, and final total.


store_name = "shafad"
store_opening_year = 2015
does_store_open = True

current_year = int(input("Please! Enter the current year: "))
store_running_years = current_year - store_opening_year

print(f"Welcome to, {store_name.upper()}")
print(f"The store is running {store_running_years} years, and does store is open now? " + str(does_store_open))

products_sold = ["laptop", "headset", "shirt", "book", "bag"]
print("Available products are: ", (products_sold))

products_category = ("electronics", "clothes", "education")
print("Available product categories: ", (products_category))

products_unique_discount = {"SALE10", "TOOL20", "WELCOME7", "VIP1327"}
print("Available unique discounts are: ", (products_unique_discount))

product_dict = {"laptop" : 400, "headset" : 33, "shirt" : 18, "book" : 14, "bag" : 8}

customer_type = input("Enter if you are a 'VIP' or 'REGULAR' customer: ").lower()
discount = 0

if customer_type == "vip":
    discount = 0.10
    print("You will get a 10% discount")
else:
    print("no discount! sorry.")


payment_method = input("Enter the payment method: 1.cash 2.card 3.mobilepay: ")
match payment_method:
    case "1":
        print("Put the cash on the desk thanks.")
    case "2":
        print("Go that way to use your smartcard.")
    case "3":
        print("You have to use the QR code for your mobile.")
    case _:
        print("Invalid payment method.")
        
if does_store_open:
    print("Yes! the store is open and working now.")
else:
    print("No! the store is closed, come again.")
   

cart = []       
total_before_discount = 0

while True:
    product = input("Enter the product you want to buy, write 'done' to finish it: ").lower()
    if product == "done":
        break
    elif product in product_dict:
        cart.append(product)
        total_before_discount+=product_dict[product]
        print(f"You purchased {product}, and the current cost or price is ${total_before_discount}")
    else:
        print("Product not found.")

whole_discount_amount = total_before_discount * discount
final_total_bill = total_before_discount - whole_discount_amount



    
print("\n--------FINAL RECEIPT-------------")
print(f"Welcome, to {store_name} store.")
print(f"The store is running or working {store_running_years} years.")
print(f"You are a {customer_type} customer.")
print(f"You purchased these items {cart}.")
print(f"Your total bofore discount was ${total_before_discount}.")
print(f"You got a discount of ${whole_discount_amount}.")
print(f"Your final cost is ${final_total_bill}.")
    


