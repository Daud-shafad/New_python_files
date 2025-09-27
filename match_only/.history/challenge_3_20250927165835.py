# Given a variable grade, match "A", "B", "C", else print "Fail".

grade = "C"

match grade:
    case "A" | "B" | "C":
        print("pass")
    case _:
        print("fail")