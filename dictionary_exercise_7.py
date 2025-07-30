#Write a function that takes a nested dictionary and return a list of all names
def extract_names(nested):
    return [info["name"] for info in nested.values()]

nested = {
    "emp1": {"name": "Ali", "age": 30},
    "emp2": {"name": "Ayan", "age": 25}
}
print(extract_names(nested))
# Output: ['Ali', 'Ayan']


