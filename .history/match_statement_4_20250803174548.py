"""
 Match a list colors = ["red", "blue"] and print "Has red" if "red" 
 is in the list, otherwise "No red".
"""
colors = ["red", "blue"]
match colors:
    case "red":
        print("Has red")
    case _:
        print("No red")