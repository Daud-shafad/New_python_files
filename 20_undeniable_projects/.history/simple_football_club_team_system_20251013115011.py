# in here i'm going to make a simple football management system 
# with external password

football_team_dict = {}

while True:
    print("\n------Available Menu Choices/Options:------ ")
    print("\n1. Add Team")
    print("2. Add Player")
    print("3. Update coach")
    print("4. Search Team")
    print("5. Search Player")
    print("6. Delete team")
    print("7. View Team")
    print("8. View All Teams")
    print("9. Exit")
    
    user_input = input("Enter your choice: ")
    if user_input == '9':
        print("Good bye, You stopped the app.")
        break
    elif user_input == '1' or user_input == '2' or user_input == '3' or user_input == '4' or user_input == '5' or user_input == '6' or user_input == '7' or user_input == '8':
        
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
                if player_name not in football_team_dict[team_name]:
                    football_team_dict[team_name].append(player_name)
                    print(f"You added {player_name} for the {team_name}")
                else:
                    print(f"Player is already available for the team")
            
            case '3':
                coach_name = input("Enter the coach name: ")
                if coach_name in football_team_dict:
                    football_team_dict[team_name][1] = coach_name
                    print("You updated {coach_name} where the DB is {team_name}")
                else:
                    print("Coach not found.")
                    
            case '4':
                player_name = input("Enter the player name: ")
                if player_name in football_team_dict[team_name][0]:
                    football_team_dict[team_name] = team_name
                    print(f"The team is: {football_team_dict[team_name]}")
                else:
                    print("Team not found, add it firstly")
            
            case '5':
                team_name = input("Enter the team name: ")
                if team_name in football_team_dict:
                    print(f"The player is in this: {football_team_dict[team_name][0]}")
                else:
                    print("Player not found")
            
            case '6':
                team_name = input("Enter the team name: ")
                if team_name in football_team_dict:
                    football_team_dict.popitem()
                    print(f"You Deleted the, {team_name}")
                else:
                    print("Team not found.")
                    
            case '7':
                team_name = input("Enter the team name: ")
                if team_name in football_team_dict:
                    view_team = football_team_dict[team_name] = []
                    print(f"The team you entered has the DATA of {view_team}")
                else:
                    print("Team not found")
            
            case '8':
                print("The DATA you Requested is: {football_team_dict}")
            
            case _:
                print("Option not valid, Try again")
    else:
        print("Invalid choice Type (1-9)")                                 
                