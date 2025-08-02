# Ask for a user's age. If under 13, print "Child", if under 20, print "Teen", otherwise print "Adult".
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 20:
    print("Teen")
else:
    print("Adult")