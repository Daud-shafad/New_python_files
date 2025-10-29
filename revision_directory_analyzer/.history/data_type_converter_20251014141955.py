# Challenge 10: Data Type Converter
# Combine: casting, if/else, while, match, all data types

# Input value, convert to: int, float, str, bool, list

# Handle conversion errors with conditions

# Menu-driven conversion system

while True:
    print("\n-----Available Data Type Converting Options:-----")
    print("1. Integer")
    print("2. Float")
    print("3. String")
    print("4. Bool")
    print("5. List")
    print("6. Tuple")
    print("7. Set")
    print("8. Dictionary")
    print("9. Exit")
    
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '9':
        print("Good bye, You stopped the App")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6' or user_choice == '7' or user_choice == '8': 
    
       match user_choice:
        
        case '1':
            user_type = input("Enter the type you're converting: ")
            if user_type == str(user_type):
             result_type = int(user_type)
            print(result_type) 