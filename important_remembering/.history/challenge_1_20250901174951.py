# Ask the user for their age. If they are under 18, print "You are a minor". 
# If they are 18 or older but under 60, 
# print "You are an adult". Otherwise print "You are a senior".

age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are a senior")