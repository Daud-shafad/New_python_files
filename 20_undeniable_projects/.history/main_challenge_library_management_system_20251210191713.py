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

books_dict = {}
members_dict = {}
while True:
    print("\n----------Available Library Menu Options----------")
    print("1. Add New Book")# that is worked really well
    print("2. Register New Member")# this is worked really well
    print("3. Borrow A book")# this is worked really well
    print("4. Return Books")# this is worked really well
    print("5. Search books By Title, Author, or Genre")
    print("6. View Borrowing Members History")
    print("7. View All Books")# this is worked really well
    print("8. Exit The system")# this is worked really well
    
    
    user_choice = input("Enter Your Choice: ")
    
    if user_choice == '8':
          print("Good Bye, You stopped the system, See You later!")
          break
      
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5' or user_choice == '6' or user_choice == '7':
        
        match user_choice:
            
            case '1':
                book_id = int(input("Enter the Book ID: "))
                book_title = input("Enter the title of the Book: ") 
                book_author = input("Enter the Author of the Book: ")
                book_genre = input("Enter the Genre of the Book: ")
                book_year = input("Enter the Year of published: ")
                book_availability = input("Enter the Availability of the book: ")
                book_borrower = input("Enter the Borrower of the Book: ")
                if book_id not in books_dict:
                    books_dict[book_id] = [book_title, book_author, book_genre, book_year, book_availability, book_borrower]
                    print(f"You Added {book_id} which belongs {book_title} Successfully")
                else:
                    print("The Book is Already exist")
            
            case '2':
                member_id = int(input("Enter member ID: "))
                member_name = input("Enter member Name: ")
                member_email = input("Enter member Email: ")
                borrowed_books = input("Enter borrowed Books: ").split()
                if member_id not in members_dict:
                    members_dict[member_id] = [member_name, member_email, (borrowed_books)]
                    print(f"You Added {member_id} who is {member_name} Successfully")
                else:
                    print("The Member is Already in the list of Members")
            
            case '3':
                member_id = int(input("Enter member ID: "))
                borrower_name = input("Enter borrower name: ")
                book_id = int(input("Enter the Book ID: "))
                if member_id in members_dict and book_id in books_dict:
                    books_dict.pop(book_id)
                    print(f"{member_id} borrowed the book Id of {book_id}")
                    books_dict[book_id] = [book_title, book_author, book_genre, book_year, book_availability, borrower_name]
                elif member_id not in members_dict and book_id in books_dict:
                    print("You are not a member, please register as a member to borrow a book")
                elif member_id in members_dict and book_id not in books_dict:
                    print("The book You want to borrow is not available, Thanks")
                else:
                    print("You're a random customer/person, please register Your name")
            
            case '4':
                member_id = int(input("Enter member ID: "))
                book_id = int(input("Enter the Book ID: "))
                if member_id in members_dict and book_id not in books_dict:
                    books_dict.update({book_id : [book_title, book_author, book_genre, book_year, book_availability, book_borrower]})
                    print(f"{member_id} has returned the book of {book_id} that he borrowed early.")
                elif member_id in members_dict and book_id in books_dict:
                    print("You don't borrow a book still")
                elif member_id not in members_dict and book_id in books_dict:
                    print("The system isn't accept to return a book without registering, Sorry ")
                else:
                    print("You're not a member, borrow a book firstly")
            
            case '5':
                search_book = input("Enter The Title/Author/Genre of the Book: ")
                
                match search_book:

                  case title if title in books_dict[101][0]:
                       books_dict.get(101)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)
                  
                  case title if title in books_dict[102][0]:
                       books_dict.get(102)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)

                  case title if title in books_dict[103][0]:
                       books_dict.get(103)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)
                  
                  case author if author in books_dict[101][1]:
                       books_dict.get(101)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)
                  
                  case author if author in books_dict[102][1]:
                       books_dict.get(102)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)

                  case author if author in books_dict[103][1]:
                       books_dict.get(103)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)
                  
                  case genre if genre in books_dict[101][2]:
                       books_dict.get(101)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)
                  
                  case genre if title in books_dict[102][2]:
                       books_dict.get(102)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)

                  case genre if title in books_dict[103][2]:
                       books_dict.get(103)
                       result_search = f"The book you want is: {books_dict[book_id]}"
                       print(result_search)
                  
                  case _:
                       print("Invalid input / No book found!")
                       
            case '6':
                member_id = int(input("Enter member ID: "))
                if member_id in members_dict:
                   print(f"{borrowed_books} is borrowed: {members_dict[member_id]}")
            
            case '7':
                print(f"In the current time we have these Data of books: {books_dict}")
            
            case _:
                print("Invalid choice, Try again")
    
    else:
        print("Invalid Option Menu! Type (1-8)")
        
               
                
                
                    
                
                
                
        
    
    

