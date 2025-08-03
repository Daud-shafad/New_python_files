"""
Write a match statement that matches a tuple point = (0, y) and prints "On Y-axis" if x == 0.
"""

x = 0
match x:
    case 0 if x == 0:
        print("On Y-axis")
    case 1 if x!= 0:
        print("X-axis")
    case _:
        print("invalid value!")
       
