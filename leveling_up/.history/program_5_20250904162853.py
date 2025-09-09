# Challenge 23: Simple Voting System (while + if/else + list + variables)

# Candidates are stored in a list.

# Users enter the candidate name to vote.

# Loop continues until user types “stop”.

# Count votes for each candidate and show results at the end.

candidates_name = ["mohamoud", "mouse", "abdirahman", "faysal"]

while True:

 users_vote_name = input("Enter candidate's name you want to vote type 'stop' to stop it: ").lower()
 if users_vote_name == "stop":
     break
 if users_vote_name == candidates_name[users_vote_name]:
   print(users_vote_name)
   print(candidates_name.count(users_vote_name))
 else:
   print("Invalid candidate name")


