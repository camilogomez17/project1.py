import random

import game_data

def run_game():
    # What input do you need from the user?
    game_running = True
    
    while game_running:
        user_choice = input("Please pick rock, paper, or scissors.\n\n>").lower()
    
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
    # What message should you show the user?
        else:
            print("Please pick rock, paper, or scissors.")
        
    # Tell the user the output.
        print("You lost, tied, or won!")
    
    # Update game stats
    
    
    
    # Ask the user to play again.
    
        game_running = input("Play again?(y/n)").lower()
        if game_running == "y":
            print("Playing again\n\n")
            continue
        elif game_running == "n":
            print("Thanks for playing!!\n\n")
            break
        else:
            print("Please pick y/n.\n\n>")