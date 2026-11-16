import random
import game_data

def run_game():
    # What input do you need from the user?
    game_running = True
    
    while game_running:
        user_choice = input("Please pick rock, paper, scissors, or quit.\n\n>").strip().lower()
    
    # What logic needs to happen?
    
    # Computer picks rock, paper, or scissors.
    
        computer_choice = random.randint(1, 3)
        
    
    # Rock beats scissors
        if user_choice == "rock":
            print("User picked rock.")
    # Scissors beat paper
        elif user_choice == "paper":
            print("User picked paper.")
    # Paper beats rock
        elif user_choice == "paper":
                print("User picked paper.")
        elif user_choice == "quit":
            print("Quitting...\n\n")
            game_running = False
            
            
            
    # What message should you show the user?
    
    # Update game stats
    
    # Ask the user to keep playing