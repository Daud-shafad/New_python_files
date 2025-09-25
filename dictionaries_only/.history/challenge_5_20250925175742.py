# Create a nested dictionary of a student with "marks" 
# having math and science scores, and access the science score.

my_dict = {"name" : "Daud", "age" : 25, 
           "subject" : {"maths" : 80, "science" : 90}}
print(my_dict["subject"]["science"])