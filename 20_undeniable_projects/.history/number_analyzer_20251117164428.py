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
                is_prime = 1
                divisor = 2
                if user_number <= 1:
                    print(f"Your number {user_number} is not Prime/Composite")
                elif user_number == 2:
                    print(f"Your number {user_number} is Prime")
                else:
                    while divisor * divisor <= user_number:
                        if user_number % divisor == 0:
                            is_prime = 0
                            break
                        divisor = divisor + 1
                    if is_prime == 1:
                        print("Your number is Prime")
                    else:
                        print("Your number is Composite")
                
            case '3':
                user_number = int(input("Enter a number: "))
                if user_number > 0:
                    print(f"Your number {user_number} is Positive")
                elif user_number < 0:
                    print(f"Your number {user_number} is Negative")
                else:
                    print("Your number is Zero")
            case _:
                    print("Invalid Option menu, Try again")
    else:
        print("Invalid choice, type (1-4)")
