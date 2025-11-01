# Challenge 5: Inventory Tracker
# Combine: dictionaries, lists, if/else, while, match, numbers

# Items: {id: [name, quantity, price]}

# Menu: Add item, Sell item, Restock, View inventory

# Update quantities with conditions

inventory_dict = {}
restock_dict = {}


while True:
    print("\n-------AVAILABLE MENU OPTION (INVENTORY):-------")
    print("1. Add Item")
    print("2. Sell Item")
    print("3. Restock Item")
    print("4. View Inventory")
    print("5. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '5':
        print("Bye, You stopped the system!")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
    
        match user_choice:
            
          case '1':
              item_id = int(input("Enter the ID of the Item: "))
              item_name = input("Enter Item name: ")
              item_quantity = int(input("Enter Quantity of the item: "))
              item_price = float(input("Enter Item price: $ "))
              if item_id not in inventory_dict:
                 inventory_dict[item_id] = [item_name, item_quantity, f"${item_price:.1f}"]
                 print(f"You added {item_id}, {item_name} Successfully")
              else:
                  print("Item is Already exist")
          
          case '2':
              user_name = input("Enter Your name: ")
              user_phone = input("Enter Your phone number: ")
              print(inventory_dict)
              item_id = int(input("Enter the ID of the item you want: "))
              if item_id in inventory_dict:
                  current_quantity = inventory_dict[item_id][1]
                  item_name = input("Enter the name of the item you want: ")
                  sold_quantity = int(input("Enter the Quantity you want: "))
                  if sold_quantity <= current_quantity: 
                     new_qty = current_quantity - sold_quantity
                     inventory_dict[item_id][1] = new_qty
                     print("Sale is happen successfully")
                     print(f"You sold {sold_quantity} Quantities of {item_name}")
                     print(f"The quantities left for {item_name} is {new_qty}")
                  else:
                      print(f"Insufficient stock only {current_quantity} of {inventory_dict[item_id]} are available")
              else:
                print("Item not Found")
          
          case '3':
               user_order = input("Enter the item you want to buy: ")
               user_quantity = int(input("Enter the quantity: "))
               user_phone = input("Enter Your phone number: ")
               restock_dict[user_phone] = [user_order, user_quantity]
               print(f"The Restock items you made {restock_dict}")
               user_payout = input("Enter the payout (1. cash,  2. card,  3. mobile): ")
               match user_payout:
                    case '1':
                       cash_money = float(input("Enter the Amount in USD: "))
                       print(f"You Spend {cash_money} USD and you buy {user_order}, Thanks.")
                    case '2':
                       card_number = int(input("Enter Your card number: "))
                       card_type = input("Enter the type Debit/credit: ")
                       amount_money = int(input("Enter The amount: "))
                       print(f"You Spend {amount_money} USD in {user_order}, Thanks.")
                    case '3':
                       mobile_money = float(input("Enter the amount: ")) 
                       print(f"You Spend {mobile_money} USD in {user_order}, Thanks.")
                    case _:
                       print("Invalid Payout option, try again")
             
               print(f"You made Restock {user_order} item, Thanks for your connection")
               
          case '4':
               print(f"Your Inventory has these Items: {inventory_dict}, and you restock these items: {restock_dict}")
             
          case _:
               print("Invalid Option Menu, Try again")
    
    else:
        print("Invalid Input")            
              
              