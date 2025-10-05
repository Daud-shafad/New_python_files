#  Day 2: If/Else + Match + While → menu-driven calculator.

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract") 
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '5':
        print("Goodbye!")
        break
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        match choice:
            case '1':
                result = num1 + num2
                print(f"Result: {result}")
            case '2':
                result = num1 - num2
                print(f"Result: {result}")
            case '3':
                result = num1 * num2
                print(f"Result: {result}")
            case '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"Result: {result}")
                else:
                    print("Error: Cannot divide by zero!")
    else:
        print("Invalid choice! Please enter 1-5")
    