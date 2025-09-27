# Match a tuple (0, y) or (x, 0) or (x, y) and print its position.

tuple = (2 , 9)

match tuple:
    case (0, y):
        print(f"{y} is pointed to that position on y axis")
    case (x, 0):
        print(f"{x} is pointed to that position on x axis")
    case (x, y):
        print(f"{x} and {y}, both are that pointed to that position on their axises")
    case _ :
        print("Un-known points, try again")   
