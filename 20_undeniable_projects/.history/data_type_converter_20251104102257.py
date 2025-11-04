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
    print("9. Exit")
    
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '9':
        print("Good bye, You stopped the App")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6' or user_choice == '7' or user_choice == '8': 
    
       match user_choice:
        
        case '1':
            user_type = float(input("Enter the type you're converting(float/complex): "))
            if user_type == float or user_type == complex: 
               print(int(user_type)) 
            else:
                print("You Already have an integer type")
        
        case '2':
            user_type = int(input("Enter the type you're converting(int/complex): "))
            if user_type == int or user_type == complex: 
               print(float(user_type)) 
            else:
                print("You already have a float type")
        
        case '3':
            user_type = int(input("Enter the type you're converting(int/float): "))
            if user_type == int or user_type == float: 
               print(complex(user_type)) 
            else:
                print("You already have a complex type")
        
        case '4':
            user_type = input("Enter the type you're converting: ")
            if user_type != str: 
               print(str(user_type)) 
            else:
                print("You already have a string data type")
        
        case '5':
            user_type = input("Enter the type you're converting: ")
            if user_type != bool: 
               print(bool(user_type)) 
            else:
                print("You already have a bool data type")
        
        case '6':
            user_type = input("Enter the type you're converting: ")
            if user_type != list: 
               print(list(user_type)) 
            else:
                print("You already have a list data type")
        
        case '7':
            user_type = input("Enter the type you're converting: ")
            if user_type != tuple: 
               print(tuple(user_type)) 
            else:
                print("You already have a tuple data type")
        
        case '8':
            user_type = input("Enter the type you're converting: ")
            if user_type != set: 
               print(set(user_type)) 
            else:
                print("You already have a set data type")
        
        case _:
                print("Invalid choice, Try again")
                
    
    else:
           print("Invalid option Menu, type (1-10)")