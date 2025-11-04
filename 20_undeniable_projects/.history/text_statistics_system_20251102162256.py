# Challenge 8: Text Statistics
# Combine: strings, sets, lists, if/else, while, match

# Input text, analyze: character count, unique words, vowels/consonants

# Use sets for unique elements

# Multiple analysis options


while True:
    print("\n-----AVAILABLE MENU TEXT STATISTICS-----")
    print("1. Character Count")
    print("2. Unique Words")
    print("3. Vowels")
    print("4. Consonants")
    print("5. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '5':
       print("You Cancelled The System, See You Later!")
       break
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4':
        match user_choice:
            
            case '1':
                 user_input = input("Enter a text: ")
                 print(len(user_input))
                 
            case '2':
                 user_input = input("Enter a text: ")
                 words = user_input.lower().split()
                 text_statistics_set = set(words)
                 unique_word_count = len(text_statistics_set)
                 print(f"Original word list: {words}")
                 print(f"Unique words: {text_statistics_set}")
                 print(f"Total unique words: {unique_word_count}")
                 
            case '3':
                 user_input = input("Enter a text: ")
                 