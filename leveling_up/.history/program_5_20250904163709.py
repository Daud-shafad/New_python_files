# Challenge 23: Simple Voting System (while + if/else + list + variables)

# Candidates are stored in a list.

# Users enter the candidate name to vote.

# Loop continues until user types “stop”.

# Count votes for each candidate and show results at the end.

candidates_name = [ "mohamoud", "mouse", "abdirahman", "faysal" ]

while True:

 users_vote_name = input("Enter candidate's name you want to vote type 'stop' to stop it: ").lower()
 if users_vote_name == "stop":
     break
 if users_vote_name == "mohamoud":
      print(users_vote_name.count("mohamoud"))
 elif users_vote_name == "mouse":
      print(users_vote_name.count("mouse"))
 elif users_vote_name == "abdirahman":
      print(users_vote_name.count("abdirahman"))
 elif users_vote_name == "faysal":
      print(users_vote_name.count("faysal"))
     
 else:
   print("Invalid candidate name")


