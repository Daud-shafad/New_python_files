# in here i'm going to make or write the concept and the code of 
# cafeteria place system
# i will store the info of customers, and i will display them the menu 
# also i will calculate the total of what they ordered
# also they will get the receipt of what they order
# and lastly they will make paying amount of what they ordered

cafeteria_dict = {}

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
                print("Espresso price is: ${4.5}")
                user_name = input("Enter Your name: ")
                