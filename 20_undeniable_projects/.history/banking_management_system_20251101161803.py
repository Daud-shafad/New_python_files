# in here i am going to make a simple or text based banking system
# i will use the core concepts of the python
# let's get started

banking_registration = {}
while True:
    print("\n-----AVAILABLE MENU BANKING OPTIONS-----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. History")
    print("5. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '5':
        print("Good bye! You cancelled the system")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        
        match user_choice:
            case '1':
                user_name = input("Enter Your name: ")
                deposit_amount = float(input("Enter the amount: "))
                if user_name not in banking_registration:
                   banking_registration[user_name] = [deposit_amount]
                   print(f"You made a deposit of: {deposit_amount}")
                else:
                    print("The person is already has a registered account")
            
            case '2':
                user_name = input("Enter Your name: ")
                withdraw_amount = float(input("Enter the amount: "))