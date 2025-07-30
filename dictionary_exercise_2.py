# Write a Python function that takes a dictionary and returns a list of keys that have numeric values only.
def get_numeric_keys(d):
    return [k for k, v in d.items() if isinstance(v, (int, float))]

mydict = {"a": 1, "b": "hello", "c": 3.5}
print(get_numeric_keys(mydict))  # Output: ['a', 'c']
