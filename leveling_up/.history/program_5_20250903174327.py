# Challenge 23: Simple Voting System (while + if/else + list + variables)

# Candidates are stored in a list.

# Users enter the candidate name to vote.

# Loop continues until user types “stop”.

# Count votes for each candidate and show results at the end.

candidates_name = ["mohamoud", "mouse", "abdirahman", "faysal"]

while True:

 users_vote_name = input("Enter candidate's name you want to vote: ").lower()
 if users_vote_name == "stop":
     break
 if users_vote_name == "mohamoud":
   candidates_name.count(0)
 elif users_vote_name == "mouse":
   candidates_name.count(1)
 elif users_vote_name == "abdirahman":
   candidates_name.count(2)
 elif users_vote_name == "faysal":
   candidates_name.count(3)
 else:
     print("Invalid candidate name")


