# Write a function that receives a dictionary and returns a new dictionary with keys and values swapped.
def swap_dict(d):
    return {v: k for k, v in d.items()}

example = {"a": 1, "b": 2}
swapped = swap_dict(example)
print(swapped)
# Output: {1: 'a', 2: 'b'}
