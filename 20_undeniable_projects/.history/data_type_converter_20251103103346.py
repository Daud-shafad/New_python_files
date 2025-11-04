# Challenge 10: Data Type Converter
# Combine: casting, if/else, while, match, all data types

# Input value, convert to: int, float, str, bool, list

# Handle conversion errors with conditions

# Menu-driven conversion system

while True:
    print("\n-----Available Data Type Converting Options:-----")
    print("1. Integer")
    print("2. Float")
    print("3. complex")
    print("4. String")
    print("5. Bool")
    print("6. List")
    print("7. Tuple")
    print("8. Set")
    print("9. Dictionary")
    print("10. Exit")
    
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '10':
        print("Good bye, You stopped the App")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6' or user_choice == '7' or user_choice == '8' 
    
       match user_choice:
        
        case '1':
            user_type = input("Enter the type you're converting(float/complex): ")
            if user_type == int: 
               print(int(user_type)) 
            else:
                print(You)
        
         case '2':
            user_type = input("Enter the type you're converting(float/complex): ")
            if user_type == float: 
               print(float(user_type)) 
            else:
                print(complex(user_type))