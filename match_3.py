# Ask the user to enter a country name.
# Use a match statement to print the corresponding continent: "Somalia" → "Africa"
#  "China" → "Asia", "Germany" → "Europe", "Brazil" → "South America" 
# Any other input → "Continent unknown"

country = str(input("Enter your country: "))
match country:
    case "Somalia":
        print("Africa")
    case "China":
        print("Asia")
    case "Germany":
        print("Europe")
    case "Brazil":
        print("South America")
    case _:
        print("Continent unknown")
        








