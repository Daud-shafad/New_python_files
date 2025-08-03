"""
Write a match statement that matches a tuple point = (0, y) and prints "On Y-axis" if x == 0.
"""

x = (0 , "y")
match x:
    case x if x == 0:
        print("On Y-axis")
    case y if x!= 0:
        print("X-axis")
    case _:
        print("invalid value!")
       
