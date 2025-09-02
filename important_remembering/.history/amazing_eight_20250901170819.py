#Challenge 8: Calculator
# Ask for an operator (+, -, *, /) and two numbers. Use match to calculate.
number_1 = int(input("Enter a number: "))
operator = input("Enter an operator like +, -, *, / : ")
number_2 = int(input("Enter a number: "))
match number_1, operator, number_2:
    case 1:
        print(number_1 + operator + number_2)
    
