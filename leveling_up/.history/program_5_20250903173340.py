# Challenge 23: Simple Voting System (while + if/else + list + variables)

# Candidates are stored in a list.

# Users enter the candidate name to vote.

# Loop continues until user types “stop”.

# Count votes for each candidate and show results at the end.

candidates_name = ["mohamoud", "mouse", "abdirahman", "faysal"]
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
while True:
 users_vote_name = input("Enter candidate's name you want to vote: ").lower()
 if users_vote_name == "stop":
     break
 if users_vote_name == "mohamoud":
     count_1 += users_vote_name
 elif users_vote_name == "mouse":
     count_2+=users_vote_name
 elif users_vote_name == "abdirahman":
     count_3+=users_vote_name
 elif users_vote_name == "faysal":
     count_4+=users_vote_name
 else:
     print("Invalid candidate name")


