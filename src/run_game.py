import random
import game_data

def run_game():
    # What input do you need from the user?
    game_running = True
    
    # Store user's choice (rock/paper/scissors/quit)
    
    while game_running:
        user_choice = input("\nPlease pick rock, paper, scissors, or quit.\n\n>").strip().lower()
    
    # What logic needs to happen?
    
    # Computer picks rock, paper, or scissors.
    
        computer_choice = random.randint(1, 3)
        
    # Compare user choice with computer choice.
        
    
    # Rock beats scissors
        if user_choice == "rock":
            print("\nUser picked rock.\n")
    # Scissors beat paper
        elif user_choice == "paper":
            print("\nUser picked paper.\n")
    # Paper beats rock
        elif user_choice == "paper":
                print("\nUser picked paper.\n")
        elif user_choice == "quit":
            print("Quitting...\n\n")
            game_running = False
        else:
            print("\nInvalid input. You are being punished with another game of rock, paper, scissors.\n >:D")
            
            
            
    # What message should you show the user?
    
    # Update game stats
    
    # Ask the user to keep playing