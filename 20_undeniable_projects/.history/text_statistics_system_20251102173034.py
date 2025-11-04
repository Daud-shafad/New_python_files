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
                if any(vowel in user_input for vowel in vowels):
                    total_vowels = sum(user_input.count(vowels) for vowel in vowels)
                    found_vowels_set = {vowel for vowel in vowels if vowel in user_input}
                    print(f"Your vowels in the text are: {sorted(list(found_vowels_set))}")
                    print(f"You have a total of vowels: {total_vowels}")
                else:
                    print("You have no vowels in Your text")
                    
            case '4':
                user_input = input("Enter a text: ").lower()
                my_vowels = 'aeiou'
                unique_consonants_set = {char for char in user_input if char.isalpha() and char not in my_vowels}
                total_consonants = sum(1 for char in user_input if char.isalpha() and char not in my_vowels)
                if unique_consonants_set:
                    print(f"Your consonants in the text are: {sorted(list(unique_consonants_set))}")
                    print(f"You have a total of consonants: {total_consonants}")
                else:
                    print("You have no consonants in your text")
            case _:
                    print("Invalid option, Try again")
                    
    else:
            print("Invalid choice Menu, Choose (1-5)")
            
                