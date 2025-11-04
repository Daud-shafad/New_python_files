# simple menu-driven calculator

while True:
    print("\n 1. Addition (+)")
    print("2. subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Module (%)")
    print("6. Quotient (**)")
    print("7. Floor-division (//)")
    print("8. Exit ❌")
    
    user_choice = input("Enter Your choice (1-7):")
    if user_choice == '8':
        print("Good bye, you stopped the App!")
    else:
        match user_choice:
            case '1':
                user_num_1 = float(input("Enter a number: "))
                user_num_2 = float(input("Enter a number: "))
                