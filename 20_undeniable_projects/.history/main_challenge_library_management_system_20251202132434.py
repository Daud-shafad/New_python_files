# MAIN CHALLENGE: Library Management System

# Create a complete text-based library system using ONLY these concepts:

# Data Structures:

# Use nested dictionaries for books and members

# Books: {book_id: {title, author, genre, year, available, borrower}}

# Members: {member_id: {name, email, borrowed_books}}

# Use lists for tracking book IDs and member IDs

# Use sets for genres and available books

# Use tuples for book information display

# Operations:

# Add new books to library

# Register new members

# Borrow books (update availability and borrower)

# Return books (update status)

# Search books by title, author, or genre

# View all available books

# View member borrowing history

# Control Flow:

# While loop for main menu system

# Match statements for menu options

# Match with guards for genre-based searches

# If/else for all validations and conditions

# Continue/break for menu navigation

# Boolean flags for system state

# Features:

# Input validation using casting and string methods

# Track book availability with booleans

# Use operators for year comparisons and searches

# Handle all data types appropriately

# Comprehensive error checking with conditions

# Menu Options:

# Book Operations

# Member Operations

# Search System

# Reports

# Exit

# Use ONLY: syntax, comments, variables, data types, numbers, casting, strings, booleans, operators, lists, tuples, sets, dictionaries, nested dictionaries, if/else, match, match with guards, while loop with continue/break

# No functions, no for loops!


while True:
    print("\n----------Available Library Menu Options----------")
    print("1. Add New Book")
    print("2. Register New Member")
    print("3. Borrow A book")
    print("4. Return Books")
    print("5. Search books By Title, Author, or Genre")
    print("6. View Borrowing Members History")
    print("7. View All Books")
    print("8. Exit The system")
    
    user_choice = input("Enter Your Choice: ")
    if user_choice == '8':
          print("Good Bye, You stopped the system, See You later!")
          break
      
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6' or user_choice == '7':
        
        match user_choice:
            
            case '1':
                
        
    
    

