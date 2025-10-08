# Day 4: Sets + lists + conditions → unique word counter.

# Start with a list of words containing duplicates.
# Create an empty set to store unique words found.
# Check each word in the list using conditions.
# If the word is not in the set, add it to track uniqueness.
# The final set size gives the count of unique words.

words_list = ["python", "awesome", "language", "python", "maverick", "awesome", "top"]

unique_words_set = set(words_list)
count = len(unique_words_set)
print("Unique words are: ", count)

