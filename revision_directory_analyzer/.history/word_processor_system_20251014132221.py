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
    print("4. Find/Replace")
    print("5. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '5':
        print("Good bye, You stop the program")
        break
    elif  user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        
        match user_choice:
            case '1':
                user_string = input("Enter a word or sentence: ")
                if user_string not in words_list:
                    print(f"The result is: {user_string[::-1]}")
               