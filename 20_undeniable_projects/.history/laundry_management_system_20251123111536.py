#In here i am going to make a Laundry management system
# which contains saving the data, like customers, clothes E.T.C
# also calculating how many shirts, trousers or something like that we are preparing
# and also calculating how many shirts trousers still pending & not fully prepared
# also paying the money and give it the customer to the receipt
# So, Let's get started!

order_creation_list = []
available_item_pricing = {"shirt" : f"${2.3}", "trouser" : f"${3.1}", "coat" : f"${4.2}", "jacket" : f"${3.7}", "t-shirt, socks & pants" : f"${1.2}"}
customers_management_dict = {}

while True:
    print("\n-------Available Laundry Menu Options:-------")
    print("1. Order Creation")
    print("2. Customer Management")
    print("3. Workflow Tracking")
    print("4. Billing & Payment")
    print("5. Communication & Reporting")
    print("6. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '6':
       print("You stopped the system, See you later!")
       break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5':
        
        match user_choice:
            
            case '1':
                print("available item orders & their price: ", available_item_pricing)
                user_order = input("Enter Your order(wash OR dry cleaning): ")
                order_creation_list.append(user_order)
                print(f"You make a Laundry order of {user_order}, have a patience")
            
            case '2':
                user_name = input("Enter Your name: ")
                user_phone = input("Enter Your phone: ")
                user_items = input("Enter Your items: ")
                if user_name not in customers_management_dict:
                   customers_management_dict[user_name] = [user_phone, [user_items]]
                   print(f"You added {user_name} Successfully")
                elif user_name in customers_management_dict:
                   user_name = input("Enter Your name: ")
                   customers_management_dict.get(user_name)
                   print(f"You have this data")
                else:
                   print("Customer name is not found")
            
            case '3':
                user_phone = input("Enter Your phone: ")
                user_order = input("Enter Your order(wash OR dry cleaning): ")
                if user_order in order_creation_list and user_order == 'wash':
                   print("Your item is In-Process..............!")
                elif user_order in order_creation_list and user_order == 'dry cleaning':
                   print("Ready for Pickup! Thanks ")
                else:
                   print("You don't make an order Yet, have an order firstly!")
            
            case '4':
                user_name = input("Enter Your name: ")
                user_phone = input("Enter Your phone: ")
                user_items = input("Enter Your items: ")
                if user_items in available_item_pricing:
                   total = available_item_pricing[user_items]
                   print(f"You have a total of {total}")
                else:
                   print("Item is not found")
                
                user_payment = input("Enter the payment type (1. cash 2. card 3. mobile): ")
                
                match user_payment:
                    
                    case '1':
                        user_name = input("Enter Your name: ")
                        user_cash = float(input("Enter the amount: $"))
                        print(f"You payout a Total cash of ${user_cash} Thanks.")
                        
                    case '2':
                        user_name = input("Enter Your name: ")
                        user_card_type = input("Enter the card Type (Debit/credit): ")
                        user_card_num = input("Enter the card number: ")
                        user_card_amount = float(input("Enter the Amount: $"))
                        print(f"You payout an amount of ${user_card_amount}")
                    
                    case '3':
                        user_name = input("Enter Your name: ")
                        user_mobile = input("Enter Your mobile: ")
                        user_mobile_amount = float(input("Enter the amount: $"))
                        print(f"You payout an amount of ${user_mobile_amount}")
                        
                    case _:
                        print("Payment method is not Available")
            
            case '5':
                user_name = input("Enter Your name: ")
                user_phone = input("Enter Your phone: ")
                if user_name in customers_management_dict and user_payment == '1' or user_payment == '2' or user_payment == '3':
                   print(f"Dear customer {user_name} You got a honor for the business thanks for your order.")
                   print("\n------Your Final report is:------")
                   print(f"Your order is: {user_order}")
                   print(f"Your name is: {user_name}")
                   print(f"Your phone is: {user_phone}")
                   print(f"Your items are: {user_items}")
                   print(f"Your payment method is: {user_payment}")
                   print(f"You Payout a total of: ${total:.2f}")
            
            case _:
                print("Invalid option, Try again")        
    else:
        print("Invalid choice, Type (1-6)") 
                