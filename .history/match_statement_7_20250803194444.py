# Real Coding Question 2: Triangle Type Classifier
#You are given a tuple (a, b, c) representing the lengths of three sides of a triangle.
# Use a match statement to classify the triangle:

# If all sides are equal, print "Equilateral".

# If only two sides are equal, print "Isosceles".

# If no sides are equal, print "Scalene".

# If the values do not form a valid triangle (e.g., negative or zero side), print "Invalid triangle"

sides_of_triangle = (3.5, 3.5, 7.5) 
match sides_of_triangle:
    case (a,b,c) if a==b and b==c:
        print("Equilateral")
    case (a,b,c) if a==b and b==a:
        print("Isosceles")
    case (a,b,c) if a!=b and b!=c:
        print("Scalene")
    case (a,b,c) if a <= 0 and b <= 0 and c <= 0:
        print("Invalid triangle")
    case _:
        print("Something went wrong on your triangle sides!")