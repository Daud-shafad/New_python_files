# Write a program that reads a person’s age and prints:

# "Child" if the age is less than 13

# "Teenager" if the age is between 13 and 19 (inclusive)

# "Adult" if the age is 20 or above

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
elif age >= 20:
    print("Adult")