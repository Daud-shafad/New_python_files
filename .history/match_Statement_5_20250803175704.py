# Write a match statement to check if a number is:
# Even and positive → print "Even Positive"

# Odd and positive → print "Odd Positive"

# Negative → print "Negative"

# Zero → print "Zero"

number = int(input("Enter a number: "))
match number:
    case 1 if number > 0 and number % 2 == 0:
        print("Even Positive")
    case 2 if number > 0 and number % 2 != 0:
        print("Odd Positive")
    case 3 if number < 0:
        print("Negative")
    case _:
        print("zero")