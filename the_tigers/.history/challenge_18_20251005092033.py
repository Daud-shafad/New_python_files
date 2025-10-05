# Challenge 3: The Shape Calculator

# Use a while loop to create a persistent menu.

# The menu asks the user to choose a shape: 

# "1. Circle", "2. Rectangle", "3. Triangle", "4. Quit".

# Use if/else to check for the quit command.

# Use a match statement for the shapes.

# For 'Circle', ask for the radius and calculate the area.

# For 'Rectangle', ask for length and width and calculate the area.

# For 'Triangle', ask for base and height and calculate the area.

# After each calculation, print the result and return to the main menu.

while True:
    print("\n 1. Circle")
    print("\n 2. Rectangle")
    print("\n 3. Triangle")
    print("\n 4. Quit")
    
    user_choice = input("Enter a number (1-4): ")
    
    if user_choice == "4":
        break
    match user_choice:
        case '1':
            circle_radius = float(input("Enter the radius: "))
            area = (22 / 7) * circle_radius ** 2
            print("Your circle area is: ", area)
            
        case '2':
            rect_length = float(input("Enter the length: "))
            rect_width = float(input("Enter the width: "))
            area = rect_length * rect_width
            print("Your rectangle area is: ", area)
            
        case '3':
            tri_base = float(input("Enter the base: "))
            tri_height = float(input("Enter the height: "))
            area = (1/2) * (tri_base * tri_height)
            print("Your triangle area is: ", area)