"""
Given a variable command = "start", write a match block that prints 
"System starting" if command is "start" and "System stopped" if "stop".
"""
command = "stop"
match command:
    case "start":
        print("System starting")
    case "stop":
        print("System stopped")