#Challenge 8: Calculator
# Ask for an operator (+, -, *, /) and two numbers. Use match to calculate.
operator = input("Enter operator (+, -, *, /): ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match operator:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    case _:
        print("Invalid operator")

        
    
