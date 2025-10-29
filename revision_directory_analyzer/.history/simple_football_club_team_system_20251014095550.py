# in here i'm going to make a simple football management system 
# with external password

football_team_dict = {}

password = "football"

user_pass = input("Enter the term 'football' as a password: ")

if user_pass != password:
    print("Wrong Password, Start it again")
    

else:

  while True:
    print("\n------Available Menu Choices/Options:------ ")
    print("\n1. Add Team")
    print("2. Update player")
    print("3. Search Player")
    print("4. Delete team")
    print("5. View Team")
    print("6. View All Teams")
    print("7. Count The Teams")
    print("8. Exit")
    
    user_input = input("Enter your choice: ")
    if user_input == '8':
        print("Good bye, You stopped the app.")
        break
    elif user_input == '1' or user_input == '2' or user_input == '3' or user_input == '4' or user_input == '5' or user_input == '6' or user_input == '7':
        
        match user_input:
            
            case '1':
                team_name = input("Enter the team name: ")
                player_name = input("Enter the player name: ")
                coach_name = input("Enter the coach name: ")
                stadium_name = input("Enter the stadium name: ")
                if team_name not in football_team_dict:
                    football_team_dict[team_name] = [player_name, coach_name, stadium_name]
                    print(f"You added {team_name} Successfully")
                else:
                    print("Team is Already existed.")
         
            case '2':
                player_name = input("Enter the player name: ")
                team_name = input ("Enter the team name: ")
                if team_name not in football_team_dict:
                    print("Team not found, Add it firstly")
                    continue
                if player_name in football_team_dict[team_name]:
                    new_player = input("Enter the new player name: ")
                    football_team_dict[team_name][0] = new_player
                    print(f"You updated {new_player} where the DB is {player_name}")
                else:
                    print("Player not found.")
                    
            case '3':
                team_name = input("Enter the team name: ")
                if team_name in football_team_dict:
                    print(f"The player in this team is: {football_team_dict[team_name][0]}")
                else:
                    print("Player not found")
            
            case '4':
                team_name = input("Enter the team name: ")
                if team_name in football_team_dict:
                    football_team_dict.pop(team_name)
                    print(f"You Deleted, {team_name}")
                else:
                    print("Team not found.")
                    
            case '5':
                team_name = input("Enter the team name: ")
                if team_name in football_team_dict:
                    print(f"The team you entered has the DATA of: {football_team_dict[team_name]}")
                else:
                    print("Team not found, Add it firstly")
                    
            case '6':
                print(f"The DATA you Requested is: {football_team_dict}")
                
            case '7':
                print(f"The number of teams You have is: {len(football_team_dict)}")
            
            case _:
                print("Option not valid, Try again")
    else:
        print("Invalid choice Type (1-8)")                                 
                