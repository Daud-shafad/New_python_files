"""
Write a match statement that matches a tuple point = (0, y) and prints "On Y-axis" if x == 0.
"""

tuple_point = (0, "y")
match tuple_point:
    case 0 if x == 0:
        print("Y-axis")
    case "y":
        print("X-axis")
    case _:
        print("invalid value!")
       
