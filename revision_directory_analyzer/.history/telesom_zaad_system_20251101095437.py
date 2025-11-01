#In here i am going to make a sample system that looks like ZAAD
# i will use the basic concepts of python like variables, data types, casting,
# comments, booleans, numbers, strings, lists, dictionaries, while loop,
# if/else statements, match statement, outputs, and inputs, let's get started

amount_of_money = 0
pin_number = int(input("Enter Your pin number: "))

if pin_number != 1234:
    print("Invalid pin number!")
    
else:
  while True:
    print("\n-----Dooro Adeega-----")
    print("1. Itus Hadhaaga")
    print("2. Lacag Dirid")
    print("3. Lacag Labixid")
    print("4. Ku Iibso")
    print("5. Itus Dhaqdhaqaaq")
    print("6. KaBax")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '6':
        print("You stopped the App!")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5':
        match user_choice:
            case '1':
                if amount_of_money == 0:
                   print("Ma haysatid lacag kugu filan, dhigo iminka lacag")
                   user_amount = float(input("Geli xaddiga lacagta: "))
                   amount_of_money += user_amount
                   print(f"Waxaad dhigatay lacag dhan: ${user_amount}, waad mahadsantahay")
                else:
                   print(f"Hadhaagaagu waa: {amount_of_money}")
            
            case '2':
                if amount_of_money == 0:
                   print("Ma diri kartid Lacag waayo lacag ma haysatid")
                else:
                   receiver_number = int(input("Geli numberka aad u dirayso lacagta: "))
                   amount_receiving = float(input("Geli xaddiga lacagta aad u direyso $: "))
                   print(f"Waxaad u dirtey {receiver_number}, lacag dhan: ${amount_receiving}")
            
            case '3':
                if amount_of_money == 0:
                    print("Lacag aad la baxdo kuuguma jirto, Hadhaagaagu waa 0 dollar")
                else:
                    branch_number = int(input("Geli numberka xarunta: "))
                    branch_name = input("Geli magaca xarunta: ")
                    amount_pocket = float(input("Geli xaddiga lacagta aad la baxayso: "))
                    print(f"Waxaad kala baxday laanta {branch_name}, lacag dhan: ${amount_pocket}")
            
            case '4':
                if amount_of_money == 0:
                    print("Ma haysatid lacag aad wax ku iibsato, dhigo lacag si aad wax u iibsato")
                else:
                    merchant_number = int(input("Geli numberka ganacsiga: "))
                    amount_buying =  float(input("Geli xadiga lacagta aad wax ku iibsanayso: "))
                    print(f"Waxaad wax kaga iibsatay ganacsiga: {merchant_number}, lacag dhan: ${amount_buying}")
            
            case '5':
                if amount_of_money == 0:
                    print("Maad samayn wax dhaqdhaqaaq ah")
                else:
                    new_amount = (user_amount - amount_buying - amount_pocket - amount_receiving) 
                    print(f"Waxaad haysataa lacag dhan: ${new_amount}")
                    print(f"Waxaad wax ku iibsatay lacag dhan: ${amount_buying}")
                    print(f"Waxaad la baxday lacag dhan: ${amount_pocket}")
                    print(f"Waxaad dirtay lacag dhan: ${amount_receiving}")
            case _:
                    print("Invalid option")
    else:
        print("Invalid choice, try again later")                   

