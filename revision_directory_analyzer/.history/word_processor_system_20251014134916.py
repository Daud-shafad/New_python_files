# Challenge 4: Word Processor
# Combine: strings, lists, if/else, while, match, booleans

# Input text, options: reverse, uppercase, word count, find/replace

# Store results in list

# Use string methods and boolean checks

words_list = []

while True:
    print("\n-----Available options:-----")
    print("1. Reverse")
    print("2. Uppercase")
    print("3. Word count")
    print("4. Find")
    print("5. Replace")
    print("6. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '6':
        print("Good bye, You stop the program")
        break
    elif  user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5':
        
        match user_choice:
            case '1':
                user_string = input("Enter a word/sentence: ")
                print(f"The result is: {user_string[::-1]}")
                words_list.append(user_string[::1])
                
            case '2':
                user_string = input("Enter a word/sentence: ")
                print(f"The result is: {user_string.upper()}")
                words_list.append(user_string.upper())
                
            case '3':
                user_string = input("Enter a word/sentence: ")
                print(f"The result is: {len(user_string)}")
                words_list.append(len(user_string))
                
            case '4':
                user_string = input("Enter a word/sentence: ")
                user_letter = input("Enter the letter You want to find: ")
                if user_letter in user_string:
                    print(f"This letter {user_letter} is in index {user_string.find(user_letter)}")
                    words_list.append(user_string.find(user_letter))
                else:
                    print("The letter is not present in the word/sentence")
                
            case '5':
                user_string = input("Enter a word/sentence: ")
                user_letter_1 = input("Enter the letter You want to replace: ")
                user_letter_2 = input("Enter the letter You want to put in: ")
                if user_letter_1 in user_string:
                    print(f"The replacing you make is: {user_string.replace(user_letter_1, user_letter_2)}")
                    words_list.append(user_string.replace(user_letter_1, user_letter_2))
                else:
                    print("The letter is not present in the word/sentence")
            case _:
                    print("Invalid option, Try again")
    else:
        print("Invalid choice Type (1-6)")
                   
print("Your results are: " , words_list)              