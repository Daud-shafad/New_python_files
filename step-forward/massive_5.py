# Challenge 5: Simple Banking Simulator

# Keep a variable for user balance (number).

# Use a while loop to repeatedly ask the user for action: deposit, withdraw, or check balance.

# Store all transactions in a list.

# Keep unique transaction types in a set.

# Use casting for amounts.

# Use if/else to check: withdraw > balance → deny, else allow.

# Use operators for updating balance.

# Print a dictionary summary of transactions (total deposits, total withdrawals).

# At the end, print a tuple: final balance, total transactions, unique actions.


# Challenge 15: Simple Banking Simulator
balance = 0
transactions = []
unique_actions = set()
summary = {"deposits": 0, "withdrawals": 0}

while True:
    action = input("Enter action (deposit/withdraw/check/stop): ")
    if action == "stop":
        break
    if action == "deposit":
        amt = float(input("Enter amount: "))
        balance = balance + amt
        transactions.append(("deposit", amt))
        unique_actions.add("deposit")
        summary["deposits"] = summary["deposits"] + amt
    elif action == "withdraw":
        amt = float(input("Enter amount: "))
        if amt > balance:
            print("Not enough balance!")
        else:
            balance = balance - amt
            transactions.append(("withdraw", amt))
            unique_actions.add("withdraw")
            summary["withdrawals"] = summary["withdrawals"] + amt
    elif action == "check":
        print("Current balance:", balance)
        unique_actions.add("check")

print("Final Balance:", balance)
print("Transactions:", transactions)
print("Unique Actions:", unique_actions)
print("Summary Dictionary:", summary)
print("Final Summary Tuple:", (balance, len(transactions), unique_actions))
