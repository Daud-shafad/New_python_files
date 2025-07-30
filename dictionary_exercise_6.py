# Given this dictionary:
# Write code to find the key with the maximum value.

data = {"a": 10, "b": 20, "c": 30}
max_key = max(data, key=data.get)
print(max_key)
# Output: 'c'

