# simple menu-driven calculator
user_entry = "calculator"
user_pass = input("Enter the word 'calculator' to start.")

if user_pass != user_entry:
    print("Thanks, write the word or skip the app")
    
else:
  while True:
    print("\n 1. Addition (+)")
    print("2. subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Module (%)")
    print("6. Quotient (**) or power")
    print("7. Floor-division (//)")
    print("8. Exit ❌")
    
    user_choice = input("Enter Your choice (1-7):")
    if user_choice == '8':
        print("Good bye, you stopped the App!")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6' or user_choice == '7':
        match user_choice:
            case '1':
                user_num_1 = float(input("Enter a number: "))
                user_num_2 = float(input("Enter a number: "))
                result = user_num_1 + user_num_2
                print(f"the result is: {result}")
            case '2':
                user_num_1 = float(input("Enter a number: "))
                user_num_2 = float(input("Enter a number: "))
                result = user_num_1 - user_num_2
                print(f"the result is: {result}")  
            case '3':
                user_num_1 = float(input("Enter a number: "))
                user_num_2 = float(input("Enter a number: "))
                result = user_num_1 * user_num_2
                print(f"the result is: {result}") 
            case '4':
                user_num_1 = float(input("Enter a number: "))
                user_num_2 = float(input("Enter a number: "))
                result = user_num_1 / user_num_2
                print(f"the result is: {result}")
            case '5':
                user_num_1 = float(input("Enter a number: "))
                user_num_2 = float(input("Enter a number: "))
                result = user_num_1 % user_num_2
                print(f"the result is: {result}")
            case '6':
                user_num_1 = float(input("Enter a number: "))
                user_num_2 = float(input("Enter a number: "))
                result = user_num_1 ** user_num_2
                print(f"the result is: {result}")
            case '7':
                user_num_1 = float(input("Enter a number: "))
                user_num_2 = float(input("Enter a number: "))
                result = user_num_1 // user_num_2
                print(f"the result is: {result}")
            case _:
                print("Invalid choice, Try again")
    else:
        print("Invalid choice Try Again (1-8)")