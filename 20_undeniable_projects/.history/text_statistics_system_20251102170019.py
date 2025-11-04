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
                 user_input = input("Enter a text: ").lower()
                 print(len(user_input))
                 
            case '2':
                 user_input = input("Enter a text: ").lower()
                 words = user_input.lower().split()
                 text_statistics_set = set(words)
                 unique_word_count = len(text_statistics_set)
                 print(f"Original word list: {words}")
                 print(f"Unique words: {text_statistics_set}")
                 print(f"Total unique words: {unique_word_count}")
                 
            case '3':
                 user_input = input("Enter a text: ").lower()
                 vowels = ['a', 'e', 'i', 'o', 'u']
                 if vowels[0] or vowels[1] or vowels[2] or vowels[3] or vowels[4] in user_input:
                    total_vowels = len((vowels in user_input))
                    print(f"Your vowels in the text are: {vowels})")
                    print(f"You have a total vowels of: {total_vowels}")
                 else:
                    print("You have no Vowels in Your Text")
            
            case '4':
                 user_input = input("Enter a text: ").lower()
                 consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'n',
                               'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
                 if consonants[0] or consonants[1] or consonants[2] or consonants[3] or  consonants[4] or consonants[5] or consonants[6] or consonants[7] or consonants[8] or consonants[9] or consonants[10] or consonants[11] or consonants[12] or consonants[13] or consonants[14] or consonants[15] or consonants[16] or consonants[17] or consonants[18] or consonants[19]:
                    total_consonants = len(user_input(consonants))
                    print(f"Your consonants in the text are: {user_input(consonants)}")
                    print(f"You have a total vowels of: {total_consonants}")
                 else:
                    print("You have no consonants in Your Text")
            case _:
                    print("Invalid option, Try again")
                    
    else:
            print("Invalid choice Menu, Choose (1-5)")
            
                