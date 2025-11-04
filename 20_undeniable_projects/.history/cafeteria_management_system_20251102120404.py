# in here i'm going to make or write the concept and the code of 
# cafeteria place system
# i will store the info of customers, and i will display them the menu 
# also i will calculate the total of what they ordered
# also they will get the receipt of what they order
# and lastly they will make paying amount of what they ordered

cafeteria_items_dict = {}

total = 0

while True:
    print("\n-----AVAILABLE MENU CAFETERIA OPTIONS-----")
    print("1. Espresso")
    print("2. Latte")
    print("3. Cappuccino")
    print("4. Americano")
    print("5. View Order")
    print("6. Checkout")
    print("7. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '7':
        print("Good Bye, You cancelled the system.")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6':
        match user_choice:
            case '1':
                print(f"Espresso price is: ${4.5}")
                user_name = input("Enter Your name: ")
                total += 4.5
                print(f"You ordered Espresso! and your current total is: {total}")
                
            case '2':
                 print(f"Latte price is: ${3.7}")
                 user_name = input("Enter Your name: ")
                 total += 3.7
                 print(f"You ordered Latte! and your current total is: {total}")
            
            case '3':
                 print(f"Cappuccino price is: ${5.4}")
                 user_name = input("Enter Your name: ")
                 total += 5.4
                 print(f"You ordered Cappuccino! and your current total is: {total}")
            
            case '4':
                 print("Americano price is: ${2.6}")
                 user_name = input("Enter Your name: ")
                 total += 2.6
                 print(f"You ordered Americano! and your current total is: {total}")
            
            case '5':
                user_name = input("Enter Your name: ")
                if user_name not in cafeteria_items_dict:
                   cafeteria_items_dict[user_name] = {user_choice, total}
                   print(f"You have an order of: {cafeteria_items_dict}")
                else:
                    print("You don't make any orders yet")
            
            case '6':
                user_name = input("Enter Your name: ")
                amount_total = float(input("Enter the amount: $ "))
                total += amount_total
                print(f"Your final receipt is: {total}, Thanks")
                
            case _:
                print("Invalid option, Try again")
    else:
        print("Invalid choice Menu, Type (1-7)")
                
                
                
                
                
                
                
                