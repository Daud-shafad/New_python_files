# Write a Python script to count how many times each word appears in the following list:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(words.count("apple"))
print(words.count("banana"))
print(words.count("orange"))

# or also you can do it by this way at once 
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = {}
for word in words:
    counter[word] = counter.get(word, 0) + 1

print(counter)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}


