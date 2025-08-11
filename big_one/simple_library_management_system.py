#You are making a small library system that allows a user to borrow books.
# Your program should follow these steps in order:

# Ask the user for their full name (string) and number of books they already borrowed this month (integer).

# Display a welcome message like:
# "Hello, Sarah! You have borrowed 3 books this month."

# Create a list of at least 5 available books (strings).

# Create a tuple containing the prices (as floats) of those books in the same order.

# Create a set containing membership types (e.g., "regular", "premium", "guest").

# Create a dictionary mapping book titles (keys) to their prices (values).

# Ask the user which book they want to borrow (string input).

# Check (using if–else) if the book exists in the dictionary:

# If it exists, display "This book costs $X".

# If it does not exist, display "Sorry, we don't have that book." and stop the program.

# If the book exists, ask the user how many days they want to borrow it (integer).

# Use operators to calculate the total rental fee: price_per_day × days.

# If the fee is more than $30, print "You qualify for free bookmarks!"; otherwise "No extra gift for this rental."

# Ask the user for their membership type and use a match statement:
 
# "regular" → "You can borrow for a maximum of 14 days."

# "premium" → "You can borrow for a maximum of 30 days."

# "guest" → "You can borrow for a maximum of 7 days."

# Anything else → "Invalid membership type."

# Use a while loop to keep asking until the user enters a membership type that exists in the set.
 
# Cast the number of books already borrowed into a float and display it with one decimal place.

# Use a boolean to check if the user has borrowed more than 5 books this month:

# More than 5 → "Heavy reader!"

# Otherwise → "Casual reader."

person_name = str(input("Enter your full name please: "))
num_of_books = int(input("Enter number of books you borrowed this month please: "))
print(f"Hello! {person_name} You have borrowed {num_of_books} books this month.")
books = ["animal farm", "the great gatsby", "the little prince", "the stranger", "of mice and men"]
books_price = (11.6, 14.8, 10.3, 12.7, 13.4)
membership_types = {"regular", "premium", "guest"}
books_dict = {"animal farm" : 11.6, "the great gatsby" : 14.8, "the little prince" : 10.3, "the stranger" : 12.7, "of mice and men" : 13.4}

person_choice = str(input("Enter the book you want to borrow: "))
if person_choice in books_dict:
    print(f"this book costs ${books_dict[person_choice]} USD")
    num_of_days_borrow = int(input("Enter number of days you want to borrow this book: "))
    total_rental = num_of_days_borrow * books_dict[person_choice]
    if total_rental > 30:
        print("You qualify for free bookmarks!")
    else:
        print("No extra gift for this rental.")
        
    while True:
        library_membership = str(input("Enter your membership type,(regular, premium, guest): "))
        if library_membership in membership_types:
             match library_membership:
                case "regular":
                    print("You can borrow for a maximum of 14 days.")
                case "premium":
                    print("You can borrow for a maximum of 30 days.")
                case "guest":
                    print("You can borrow for a maximum of 7 days.")
             break
        else:
            print("Invalid membership type.")
        
    borrow_books = float(num_of_books)
    print(f"{borrow_books:.1f}")
    more_than_5 = num_of_books > 5
    if more_than_5:
        print("Heavy reader!")
    else:
        print("Casual reader.")


else:
    print("Sorry! we don't have that book now.")
exit
