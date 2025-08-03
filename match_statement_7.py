# Real Coding Question 2: Triangle Type Classifier

sides = (3.5, 3.5, 7.5)
a, b, c = sides

# Triangle Inequality and Valid Side Check
if a <= 0 or b <= 0 or c <= 0 or (a + b <= c or a + c <= b or b + c <= a):
    print("Invalid triangle")
else:
    match sides:
        case (x, y, z) if x == y == z:
            print("Equilateral")
        case (x, y, z) if x == y or y == z or x == z:
            print("Isosceles")
        case _:
            print("Scalene")
