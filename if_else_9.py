# Ask for a number between 1 and 7 and print the corresponding day of the week.
number = int(input("Enter a number between 1 and 7: "))
if number == 1:
    print("Saturday!")
elif number == 2:
    print("Sunday!")
elif number == 3:
    print("Monday!")
elif number == 4:
    print("Tuesday!")
elif number == 5:
    print("Wednesday!")
elif number == 6:
    print("Thursday!")
elif number == 7:
    print("Friday!")
else:
    print("Sorry! Your number is not in between 1 and 7")