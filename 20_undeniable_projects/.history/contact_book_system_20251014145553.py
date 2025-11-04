# Challenge 6: Contact Book
# Combine: dictionaries, strings, if/else, while, match, lists

# Contacts: {name: [phone, email, address]}

# Menu: Add contact, Search, Update, Delete, View all

# String validation checks

contacts = {}

while True:
    print("\n-----Available Menu Options:-----")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update phone")
    print("4. Delete contact")
    print("5. View all contacts")
    print("6. Exit")
    
    user_choice = input("Enter your choice: ")
    
    if user_choice == '6':
        print("Good bye, You stopped the System")
        break
    
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5':
        
        match user_choice:
            
            case '1':
                user_name = input("Enter your name: ")
                if user_name not in contacts:
                    user_phone = int(input("Enter your Phone: "))
                    user_email = input("Enter your Email: ")
                    user_address = input("Enter your Address: ")
                    contacts[user_name] = [user_phone, user_email, user_address]
                    print(f"You added {user_name} Successfully")
                else:
                    print("the name is Already existed")
            
            case '2':
                user_name = input("Enter The name you are searching: ")
                if user_name in contacts:
                    print(f"The name {user_name} you're searching has a data of {contacts[user_name]}")
                else:
                    print("The name not found, Add it firstly")
            
            case '3':
                user_phone = int(input("Enter the old phone you're updating: "))
                user_name = input("Enter Your name: ")
                if user_phone in contacts[user_name]:
                    new_phone = int(input("Enter the new phone: "))
                    contacts[user_name][0] = new_phone
                    print(f"You updated {user_phone}, the new one is: {new_phone}")
                else:
                    print("Phone not found")
            
            case '4':
                user_name = input("Enter the name: ")
                if user_name in contacts:
                    contacts.pop(user_name)
                    print(f"You Deleted {user_name} & no longer available")
                else:
                    print("The name is not found, Sorry!")
            
            case '5':
                print(f"The Data You're Requesting is: {contacts}")
            
            case _:
                print("Invalid option, Try again")
    else:
        print("Invalid choice, type (1-6)")                    
                    