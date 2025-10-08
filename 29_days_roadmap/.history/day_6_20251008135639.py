# Day 6: Simple library system (add/remove/search books).

library_books_dict = {101: ["the big", "by: william smith"],
                      102: ["the amazing", "by: john"],
                      103: ["the money", "by: nicolas"],
                      104: ["the president", "by: ahmed"]}


while True:
    print("\n-----Available Option Menu-----")
    print("1. View Available / present books")
    print("2. Add book")
    print("3. Remove book")
    print("4. Search book by Key(ID)")
    print("5. Exit")
    
    user_choice = input("Enter Your choice (1-5): ")
    if user_choice == '5':
        print("Good Bye, You Stopped the App!")
        break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        
        match user_choice:
            
            case '1':
                print(f"The Available books are: {library_books_dict}")
            
            case '2':
                user_id = int(input("Enter the ID: "))
                user_book = input("Enter the book name: ")
                user_author = input("Enter the author name: ")
                if user_id not in  library_books_dict:
                    library_books_dict[user_id] = [user_book, user_author]
                    print(f"You Added a new book {user_id}, {user_book}, & author of {user_author}")
                else:
                    print("The book  is Already exist")
            case '3':
                user_id = int(input("Enter the ID: "))
                if user_id in library_books_dict:
                    library_books_dict.pop(user_id)
                    print(f"You removed the book, that belongs the ID of {user_id}")
                else:
                    print("The ID you entered is not Exist, Add it firstly")
            case '4':
                user_id = int(input("Enter the ID: "))
                if user_id in library_books_dict:
                    library_books_dict.get([user_id])
                    print(f"The book you searched is: {library_books_dict[user_id]}")
                else:
                    print("ID/Book  not Found")
            case _:
                print("Invalid option, try again")
    else:
        print("Invalid choice Type (1-5)")