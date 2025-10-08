# in here i will make it a simple app shapes calculator,
# that is calculated all possible shapes we use, only with their areas
# you choose the shape, and then you will enter the info that the system asks you
# and then you will got the area of the shape you choose, based on the info you gave
# one more functionality:
# to calculate the area of the shape you want you have to enter a password,
# of the system firstly.
# LET'S GET STARTED !

password = "calculator"

user_password = input("Enter the password type (calculator) to enter: ")
if user_password != password:
    print("Wrong password, Start again")
else:
   while True:
      print("\n -----Available shapes (AREA ONLY)-----")
      print("1. RECTANGLE (▭)")
      print("2. SQUARE (🔳)")
      print("3. CIRCLE (🔵)")
      print("4. TRIANGLE (△)")
      print("5. TRAPEZOID (⏢)")
      print("6. PARALLELOGRAM (▰ )")
      print("7. RHOMBUS (♦️)")
      print("8. CYLINDER (🛢️)")
      print("9. CUBE (🧊)")
      print("10. RECTANGULAR PRISM (📦)")
      print("11. EXIT THE APP 🚫❌!")
    
      user_choice = input("Enter Your choice (1-11): ")
      
      if user_choice == '11':
          print("Good Bye, You stopped the App!")
          break
      elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6' or user_choice == '7' or user_choice == '8' or user_choice == '9' or user_choice == '10':
        
          match user_choice:
            
            case '1':
                user_num_1 = float(input("Enter the length: "))
                user_num_2 = float(input("Enter the width: "))
                area = user_num_1 * user_num_2
                print(f"The Area of Your shape is: {area}")
                
            case '2':
                user_num_1 = float(input("Enter the side: "))
                area = user_num_1 ** 2
                print(f"The Area of Your shape is: {area}")
                
            case '3':
                user_num_1 = float(input("Enter the radius: "))
                area = (22/7) * user_num_1 ** 2
                print(f"The Area of Your shape is: {area}")
                
            case '4':
                user_num_1 = float(input("Enter the base: "))
                user_num_2 = float(input("Enter the height: "))
                area = 0.5 * (user_num_1 * user_num_2)
                print(f"The Area of Your shape is: {area}")
                
            case '5':
                user_num_1 = float(input("Enter side 1: "))
                user_num_2 = float(input("Enter side 2: "))
                user_num_3 = float(input("Enter the height: "))
                area = 0.5 * (user_num_1 + user_num_2) * user_num_3
                print(f"The Area of Your shape is: {area}")
                
            case '6':
                user_num_1 = float(input("Enter the base: "))
                user_num_2 = float(input("Enter the height: "))
                area = user_num_1 * user_num_2
                print(f"The Area of Your shape is: {area}")
                
            case '7':
                user_num_1 = float(input("Enter the diagonal 1: "))
                user_num_2 = float(input("Enter the diagonal 2: "))
                area = 0.5 * user_num_1 * user_num_2
                print(f"The Area of Your shape is: {area}")
                
            case '8':
                user_num_1 = float(input("Enter the radius: "))
                user_num_2 = float(input("Enter the height: "))
                area = 2 * (22/7) * (user_num_1 + user_num_2)
                print(f"The Area of Your shape is: {area}")
                
            case '9':
                user_num_1 = float(input("Enter the side: "))
                area =  6 * (user_num_1 ** 2)
                print(f"The Area of Your shape is: {area}")
                
            case '10':
                user_num_1 = float(input("Enter the length: "))
                user_num_2 = float(input("Enter the width: "))
                user_num_3 = float(input("Enter the height: "))
                area = 2 *(user_num_1 * user_num_2) + (user_num_1 * user_num_3) + (user_num_2 * user_num_3)
                print(f"The Area of Your shape is: {area}")
            case _:
                print("Invalid option, try again")
      else:
        print("Invalid choice, Type (1-5)")
            