# Use match with guards: check if a number is >0, <0, or 0.

num = 0

match num:
    case n if n > 0:
        print("number is greater than 0 man")
    case n if n < 0:
        print("number is less than 0 man")
    case n if n == 0:
        print("number is 0 man")
    case _:
        print("Invalid number")
        
        