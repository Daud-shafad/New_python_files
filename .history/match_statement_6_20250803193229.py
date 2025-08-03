# Real Coding Question 1: Directional Input Matcher
# You’re given a tuple input (dx, dy) that represents movement on a 2D plane. 

# Write a Python match statement that does the following:

# If the movement is strictly horizontal (dy == 0 and dx != 0), print "Horizontal move".

# If the movement is strictly vertical (dx == 0 and dy != 0), print "Vertical move".

# If both dx and dy are zero, print "No movement".

# For any diagonal move (dx != 0 and dy != 0), print "Diagonal move".


tuple = int(input("enter two numbers representing x-axis and y-axis: "))
match tuple:
    case (x_axis , y_axis) if x_axis != 0 and y_axis == 0:
        print("Horizontal move")
    case (x_axis, y_axis) if x_axis == 0 and y_axis != 0:
        print("Vertical move")
    case (x_axis, y_axis) if x_axis == 0 and y_axis == 0:
        print("No movement")
    case (x_axis, y_axis) if x_axis != 0 and y_axis != 0:
        print("Diagonal move")
    case _:
        print("Sorry, What you entered is not a a valid number bro!")