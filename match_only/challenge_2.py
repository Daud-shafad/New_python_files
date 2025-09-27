# Use match to check if today is "Sat" or "Sun" → print "Weekend", else "Weekday".

today = "thur"

match today:
    case "sat" | "sun":
        print("weekend")
    case _:
        print("weekday")