#Write a Python program that:

#Asks for your favorite word

#Prints how many letters it has using len()

#And shows the word in all uppercase letters

favorite_word = input("Enter your favorite word ")
print(len(favorite_word))
print(favorite_word.upper())
print(f"Your word has {len(favorite_word)} letters.")
print(f"In all caps: {favorite_word.upper()}")