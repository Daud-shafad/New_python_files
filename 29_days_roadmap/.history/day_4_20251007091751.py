# Day 4: Sets + lists + conditions → unique word counter.

# Start with a list of words containing duplicates.
# Create an empty set to store unique words found.
# Check each word in the list using conditions.
# If the word is not in the set, add it to track uniqueness.
# The final set size gives the count of unique words.

words_list = ["python", "awesome", "language", "python", "maverick", "awesome", "top"]

unique_words_set = set()

if words_list[0] not in unique_words_set:
    unique_words_set.add(words_list[0])
    print(unique_words_set)
elif words_list[1] not in unique_words_set:
    unique_words_set.add(words_list[1])
elif words_list[2] not in unique_words_set:
    unique_words_set.add(words_list[2])
elif words_list[3] not in unique_words_set:
    unique_words_set.add(words_list[3])
elif words_list[4] not in unique_words_set:
    unique_words_set.add(words_list[4])
elif words_list[5] not in unique_words_set:
    unique_words_set.add(words_list[5])
elif words_list[6] not in unique_words_set:
    unique_words_set.add(words_list[6])
else:
    print("No unique Words in the list.")

print(unique_words_set)
