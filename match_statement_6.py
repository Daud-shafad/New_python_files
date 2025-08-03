# Real Coding Question 1: Directional Input Matcher

# Input: Tuple of two integers (dx, dy)
user_input = input("Enter two numbers (dx and dy) separated by a comma: ")
try:
    dx, dy = map(int, user_input.strip().split(","))
    direction = (dx, dy)

    match direction:
        case (x, 0) if x != 0:
            print("Horizontal move")
        case (0, y) if y != 0:
            print("Vertical move")
        case (0, 0):
            print("No movement")
        case (x, y) if x != 0 and y != 0:
            print("Diagonal move")
        case _:
            print("Invalid input")
except:
    print("Invalid input format. Enter like: 3,0")
