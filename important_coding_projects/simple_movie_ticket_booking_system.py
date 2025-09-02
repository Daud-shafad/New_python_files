# Challenge: Simple Movie Ticket Booking System 🎬
# Goal:
# Create a program where the user can:

# Enter their name.

# See a list of 3–5 movies with ticket prices.

# Select the movie by typing its name.

# Enter how many tickets they want.

# Calculate the total cost.

# Ask if they want Standard seats or VIP seats (VIP seats cost extra).

# Display a final confirmation with:

# Customer name (in uppercase)

# Movie name

# Number of tickets

# Type of seat (standard or VIP)

# Total cost

Cinema_name = "filmhub"
print(f"Welcome to {Cinema_name.upper()}.")

user_name = input("Enter your name: ")
movies_name = ["fast and furious 7", "mission impossible", "prison break", "money heist", "game of thrones"]
ticket_prices = [15.3, 16.2, 17.5, 16.7, 14.8]
print("Available movies: ", movies_name)
user_choice = input("Enter the movie name you want to watch: ").lower()
user_number_of_tickets = int(input("Enter number of tickets you want: "))

movie_index = movies_name.index(user_choice)
price_of_the_movie = ticket_prices[movie_index]
total_cost = price_of_the_movie * user_number_of_tickets
print(f"Your cost is ${total_cost}.")

user_seat_choice = str(input("Enter the seat you want STANDARD SEAT  VIP SEAT by typing it: ")).lower()

print("\n----------CONFIRMATION RECIEPT----------")
print(f"Your named is {user_name.upper()}.")
print(f"You choose to watch {user_choice.upper()}.")
print(f"You ordered {user_number_of_tickets} tickets.")
print(f"You choose also a {user_seat_choice.upper()}.")
print(f"Your total cost is ${total_cost}.")