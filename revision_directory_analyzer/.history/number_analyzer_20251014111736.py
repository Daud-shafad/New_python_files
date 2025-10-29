# Challenge 3: Number Analyzer
# Combine: numbers, casting, if/else, while, match, strings

# Take number input, analyze: even/odd, prime, positive/negative

# Menu options for different analyses

# Cast between strings/numbers

while True:
    print("\n------Available menu options:------")
    print("1.Even/Odd")
    print("2. Prime/Composite")
    print("3. Positive/Negative")
    print("4. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '4':
        print("Good bye, Program stopped.")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3':
        match user_choice:
            case '1':
                user_number = int(input("Enter a number: "))
                if user_number % 2 == 0:
                    print(f"Your number {user_number} is Even")
                else:
                    print(f"Your number {user_number} is Odd")
            case '2':
                user_number = int(input("Enter a number: "))
                if user_number > 1 and user_number / 1 == user_number: 
                   if user_number / user_number == 1:
                    print(f"Your number {user_number} is Prime")
                else:
                    print("Your number {user_number} is Composite")
            case '3':
                user_number = int(input("Enter a number: "))
                if user_number > 0:
                    print(f"Your number {user_number} is Positive")
                else:
                    print(f"Your number {user_number} is Negative")
            case _:
                    print("Invalid Option menu, Try again")
    else:
        print("Invalid choice, type (1-4)")
