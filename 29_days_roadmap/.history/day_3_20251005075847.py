# Day 3: Dictionaries + lists → student grade tracker

stud_grade = [89, 67, 57, 90, 75]

stud_dict = {"ali" : "ID-1", "fatima" : "ID-2", "osman" : "ID-3", 
             "faarah" : "ID-4", "nour" : "ID-5"}

stud_dict["ali"] = stud_grade[3]
print(stud_dict.items(), stud_grade[3])
stud_dict["fatima"] = stud_grade[2]
stud_dict["osman"] = stud_grade[1]
stud_dict["faarah"] = stud_grade[0]
stud_dict["nour"] = stud_grade[4]