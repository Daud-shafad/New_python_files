#  Day 2: If/Else + Match + While → menu-driven calculator.

while True:
    user_choice_1 = int(input("Enter a number 1: "))
    
    user_choice_2 = int(input("Enter a number 2: "))
    user_sign = input("Enter your sign: '+', '-', '*','/', '**', '%' ")
    
    match user_choice_1, user_choice_2:
        case "+":
            print(user_choice_1 + user_choice_2)
        case "-":
            print(user_choice_1 - user_choice_2)
        case "*":
            print(user_choice_1 * user_choice_2)
        case "/":
            print(user_choice_1 / user_choice_2)
        case "**":
            print(user_choice_1 ** user_choice_2)
        case "%":
            print(user_choice_1 % user_choice_2)
        case _:
            print("input error, try again")
    