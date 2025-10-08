# Day 4: Sets + lists + conditions → unique word counter.

# Start with a list of words containing duplicates.
# Create an empty set to store unique words found.
# Check each word in the list using conditions.
# If the word is not in the set, add it to track uniqueness.
# The final set size gives the count of unique words.

words_list = ["apple", "banana", "apple", "orange", "banana", "grape"]
unique_set = set()

if words_list[0] not in unique_set: unique_set.add(words_list[0])
if words_list[1] not in unique_set: unique_set.add(words_list[1])
if words_list[2] not in unique_set: unique_set.add(words_list[2])
if words_list[3] not in unique_set: unique_set.add(words_list[3])
if words_list[4] not in unique_set: unique_set.add(words_list[4])
if words_list[5] not in unique_set: unique_set.add(words_list[5])

count = len(unique_set)
print("Unique words count:", count)

