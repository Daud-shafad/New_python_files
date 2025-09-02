# Challenge 16: Age Group with Boolean
# Ask the user for their age. Use a boolean variable is_minor = age < 18. 
# If true, print "Minor", else print "Adult".


user_age = int(input("Enter your age: "))
is_minor = user_age < 18
if is_minor:
    print("Minor")
else:
    print("Adult")