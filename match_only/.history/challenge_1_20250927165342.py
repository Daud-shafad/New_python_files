# Match a variable color against "red", "green", "blue", else "unknown".

color  = "green"

match color:
    case "red":
        print("red")
    case "green":
        print("green")
    case "blue":
        print("blue")
    case _:
        print("unknown")