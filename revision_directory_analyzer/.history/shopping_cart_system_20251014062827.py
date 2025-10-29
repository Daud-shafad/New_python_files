# Challenge 2: Shopping Cart System
# Combine: lists, tuples, sets, if/else, while, match

# Products as tuples: (name, price, category)

# Cart as list of products

# Menu: Add item, Remove item, View cart, Checkout

# Use sets to track categories

products_tuple = ("laptop", 340, "electronic", "shirt", 14, "clothes",
                  "rice", 40, "food", "watch", 25, "electronic", "chair", 60, "furniture")

products_cart_list = ["laptop", "headset", "watch", "rice", "shirt", "shoes",
                      "trouser", "pasta", "chair", "table"]

while True:
    print("\n1.Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. checkout")
    print("5. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '5':
        