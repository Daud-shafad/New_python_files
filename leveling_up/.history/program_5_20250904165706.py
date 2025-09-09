# Challenge 23: Simple Voting System (while + if/else + list + variables)

# Candidates are stored in a list.

# Users enter the candidate name to vote.

# Loop continues until user types “stop”.

# Count votes for each candidate and show results at the end.


candidates = ["Ali", "Fatima", "Ahmed"]
votes = [0, 0, 0] 

while True:
    vote = input("Enter candidate name (or 'stop' to finish): ")

    if vote == "stop":
        break
    elif vote == candidates[0]:
        votes[0] = votes[0] + 1
        print("Vote counted for", candidates[0])
    elif vote == candidates[1]:
        votes[1] = votes[1] + 1
        print("Vote counted for", candidates[1])
    elif vote == candidates[2]:
        votes[2] = votes[2] + 1
        print("Vote counted for", candidates[2])
    else:
        print("Candidate not found. Try again.")

print("\n--- Voting Results ---")
print(candidates[0], ":", votes[0])
print(candidates[1], ":", votes[1])
print(candidates[2], ":", votes[2])



