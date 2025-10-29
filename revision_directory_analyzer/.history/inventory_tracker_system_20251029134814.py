# Challenge 5: Inventory Tracker
# Combine: dictionaries, lists, if/else, while, match, numbers

# Items: {id: [name, quantity, price]}

# Menu: Add item, Sell item, Restock, View inventory

# Update quantities with conditions

inventory_dict = {}

while True:
    print("\n-------AVAILABLE MENU INVENTORY:-------")
    print("1. Add Item")
    print("2. Sell Item")
    print("3. Restock Item")
    print("4. Update Quantities Inventory")
    print("5. View Inventory")
    print("6. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '6':
        print("Bye, You stopped the system!")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5':
    
        match user_choice:
          case '1':
              item_id = int(input("Enter the ID of the Item: "))
              item_name = input("Enter Item name: ")
              item_quantity = int(input("Enter Quantity of the item: "))
              item_price = float(input("Enter Item price: "))
              if item_id not in inventory_dict:
                inventory_dict[item_id] = [item_name, item_quantity, item_price]
                print(f"You added {item_id}, New item Successfully")
              else:
                  print("Item is Already exist")
          case '2':
              user_name = input("Enter Your name: ")
              user_phone = int(input("Enter Your phone number: "))
              user_item = input("Enter Item You want: ")
              user_quantity = int(input("Enter the Quantity you want: "))
              if user_item in inventory_dict:
                print(f"You sold {user_quantity} Quantities of {user_item}")
              else:
                print("Item not Found")
          case '3':
               
              
              
              