# Review variables, strings, numbers, lists, sets, tuples → mini address book.

# you can combine them to create a simple program that stores 
# and organizes contact information, like names, phone numbers, or emails.

my_lists = ["the stranger", "the big", "the one", "the massive idea"]

my_sets = {"admin123@gmail.com", "big2@yahoo.com", "me8@outlook.com"}

my_tuples = ("user_1", "user_2", "user_3", "user_4")

my_strings = "you have mini address book, and you can buy it anywhere"

my_numbers = (10,20,30,40)

print(my_lists[:2])
my_lists.remove("the big")
my_lists.append("the different")
print(my_lists)

my_new = list(my_tuples)
print(my_new)
print(my_new.count("user_3"))
my_new_1 = tuple(my_new)
print(my_new_1)


my_sets.pop()
print(my_sets)
my_sets.add("warrior_70@gmail.com")
print(my_sets)


print(my_strings.count("o")) #4
print(my_strings.find("a"))
print(my_strings.upper())
print(my_strings.format())
print(my_strings.startswith("a")) #3
print(my_strings.endswith("e")) #2
print(my_strings.split(","))

print(my_numbers[2])


