#In here i am going to make a police record management system with
# registering cases, officers, complains and suspects and lastly generating reports
# also searching cases, and officers 
# i will make it here a full text-based version of police record management system


police_record_dict = {}

suspects_record_dict = {}

while True:
    print("\n-------Available Police Record Management Menu Options:-------")
    print("1. Register An Officer")
    print("2. Add Case")
    print("3. Register A Suspect")
    print("4. Search Officer")
    print("5. Generate A Report")
    print("6. Exit")
    
    user_choice = input("Enter Your choice: ")
    if user_choice == '6':
       print("You Cancelled The System, See You Later!")
       break
    
    elif user_choice == '1' or user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5':
        
        match user_choice:
            
            case '1':
                officer_ID = input("Enter Officer ID: ")
                officer_name = input("Enter Your name: ")
                if officer_ID not in police_record_dict:
                   police_record_dict[officer_ID] = [officer_name]
                   print(f"You registered {officer_ID} as a new officer")
                else:
                   print("This officer is Already Registered")
                
            case '2':
                officer_ID = input("Enter Officer ID: ")
                officer_name = input("Enter Officer name: ")
                case_name = input("Enter case name: ")
                case_maker = input("Enter case maker name: ")
                case_date = input("Enter the date: ")
                if case_name not in police_record_dict:
                   police_record_dict[officer_ID] = [officer_name, case_name, case_maker, case_date]
                   print(f"You added a case name of ({case_name}) belongs the officer ID of {officer_ID}")
                elif case_name in police_record_dict:
                   case_maker = input("Enter Your name: ")
                   case_date = input("Enter the date: ")
                   police_record_dict[officer_ID] = (case_maker, case_date) 
                else:
                   print("This case is not Exist")
            
            case '3':
                officer_ID = input("Enter Officer ID: ")
                suspector_ID = input("Enter suspector ID: ")
                suspector_name = input("Enter suspector name: ")
                suspector_age = input("Enter suspector Age: ")
                suspector_gender = input("Enter suspector gender: ")
                suspector_arrest = input("Enter suspector status (arrested/not arrested): ")
                if officer_ID not in suspects_record_dict:
                   suspects_record_dict[officer_ID] = [suspector_ID, suspector_name, suspector_age, suspector_gender, suspector_arrest]
                   print(f"You registered new suspector ID {suspector_ID} successfully") 
                else:
                   print("Suspector is Already Exist")
            
            case '4':
                officer_ID = input("Enter Officer ID: ")
                if officer_ID in police_record_dict:
                   print(f"The officer you searched has this data: {police_record_dict[officer_ID]}") 
                else:
                   print("the ID of {officer_ID} was not Found. Register it firstly") 
            
            case '5':
                print(f"You have this data: {police_record_dict}")
                print(f"You have this suspects: {suspects_record_dict}")
            
            case _:
                print("Invalid option, Try again")
    else:
        
        print("Invalid choice Menu, Type (1-7)")            