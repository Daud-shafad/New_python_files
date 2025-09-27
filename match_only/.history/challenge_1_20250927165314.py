# Match a variable color against "red", "green", "blue", else "unknown".

color  = "red"

match color:
    case "red":
        print("red")
    case "green":
        print("green")
    case "blue":
        print("blue")
    case _:
        print("unknown")