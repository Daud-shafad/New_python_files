# Program Challenge 2: Student Grade Evaluator System

# Step 1. Create variables for school name (string), is_term_active (boolean), 
# and counters for total students and total score (numbers).
# Step 2. Prepare an empty list to store individual numeric grades.
# Step 3. Define a tuple of allowed grade ranges or labels 
# (e.g., “Poor”, “Average”, “Good”, “Excellent”) just to display.
# Step 4. Define a set to store unique performance labels encountered 
# (e.g., if a grade is “Good”, add “Good” to the set).
# Step 5. Define a dictionary mapping performance label → message 
# (e.g., "Excellent": "Great job!").
# Step 6. Ask the user for their name (string) and greet them; 
# display the tuple of performance labels.
# Step 7. If is_term_active is False, use if/else to stop with a message; otherwise continue.
# Step 8. Start a while loop to input grades repeatedly; 
# tell the user to type "stop" when finished.
# Step 9. On each loop, read input; if it equals "stop", break; 
# otherwise cast to integer and validate (0–100) with if/else.
# Step 10. If valid, append the grade to the list, 
# update the total score with operators, and increase the student counter.
# Step 11. Use if/else to determine the performance label for this grade 
# (e.g., <50 Poor, 50–74 Average, 75–89 Good, 90–100 Excellent) and add that label to the set.
# Step 12. After the loop, use a boolean like has_grades to check if any grades were entered; 
# if not, print a message and stop.
# Step 13. Compute the average using operators (total score / number of grades), 
# and determine pass/fail with if/else (e.g., average ≥ 50 → Pass).
# Step 14. Use a match statement on the final average to choose a summary level 
# (“Poor” / “Average” / “Good” / “Excellent”) 
# and print the corresponding message from the dictionary.
# Step 15. Print a report showing: student name (uppercase), 
# number of grades, the list of grades, the set of performance labels seen, 
# the average, pass/fail (boolean displayed), and the final performance label.