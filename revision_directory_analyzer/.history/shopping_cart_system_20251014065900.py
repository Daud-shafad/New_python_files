# Challenge 2: Shopping Cart System
# Combine: lists, tuples, sets, if/else, while, match

# Products as tuples: (name, price, category)

# Cart as list of products

# Menu: Add item, Remove item, View cart, Checkout

# Use sets to track categories

products_tuple = ("laptop", 340, "electronic", "shirt", 14, "clothes",
                  "rice", 40, "food", "watch", 25, "electronic", "chair", 60, "furniture")

print("Available products: ", products_tuple)

products_cart_list = []

while True:
    print("\n-----Available Cart Options:-----")
    print("1.Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. checkout")
    print("5. Exit")
    
    user_choice = input("Enter Your choice: ")
    
    if user_choice == '5':
        print("Good bye, you stopped the App")
        break
    
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        
        match user_choice:
            
            case '1':
                user_choice = input("Enter the name of the item: ")
                if user_choice not in products_cart_list:
                    products_cart_list.append(user_choice)
                    print(f"You purchased {user_choice} & you Added to your cart")
                else:
                    print("Item is Already exist")
            
            case '2':
                user_choice = input("Enter the name of the item: ")
                if user_choice in products_cart_list:
                    products_cart_list.remove(user_choice)
                    print(f"You Removed {user_choice} to Your cart")
                else:
                    print("Item not found")
            
            case '3':
                print(f"Your cart items are: {products_cart_list}")                    
                    
            case '4':
                user_name = input("Enter Your name: ")
                user_payment = input("Enter the way of payment (1. cash 2. card 3. E-mobile): ")
                
                match user_payment:
                    case '1': 
                         print("Put the cash on the desk")
                    case '2':
                         print("Go that way to use Your card")
                    case '3':
                         print("Enter this number to send it")
                    case _:
                         print("Invalid payment, try again")
                         
                my_products = set(products_cart_list)
                print(f"You purchased these items: {my_products}")
                
            case _:
                print("Invalid choice, Try again")
    else:
        print("Invalid option type (1-5)")
                    
            