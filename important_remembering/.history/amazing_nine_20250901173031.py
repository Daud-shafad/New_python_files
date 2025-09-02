# Challenge 9: Traffic Light
# Ask for a color (red, yellow, green). Use match to print an action (“Stop”, “Slow down”, “Go”).

color = input("Enter a color red, yellow, green: ").lower()
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Slow down")
    case "green":
        print("Go")
    case _:
        print("Invalid color choice, try again.")