#  Day 2: If/Else + Match + While → menu-driven calculator.

while True:
    print("Menu: ")
    print("1. addition: ")
    print("2. subtraction: ")
    print("3. multiplication: ")
    print("4. division: ")
    print("5. exit: ")
    
    choice = '1' | '2' | '3' | '4' | '5'
    if choice == '5':
        print("complete")
        break
    user_choice_1 = int(input("enter number 1: "))
    user_choice_2 = int(input("enter a number 2: "))
    
    match user_choice_1, user_choice_2:
        case '1':
            print("the result is: " , user_choice_1 + user_choice_2) 
        case '2':
            print("the result is: " , user_choice_1 - user_choice_2)
        case '3':
            print("the result is: " , user_choice_1 * user_choice_2)
        case '4':
            if user_choice_1 != 0:
             print("the result is: " , user_choice_1 / user_choice_2)
        case _:
            print("invalid input: ")
