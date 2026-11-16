import random

def run_game():
    # What input do you need from the user?
    user_choice = input("Please pick rock, paper, or scissors.").lower()
    
    # What logic needs to happen?
    
    # Computer picks rock, paper, or scissors.
    
    computer_choice = random.randint(1, 3)
    
    match user_choice:
        case "rock":
            print("You picked rock.")
        case "paper":
            print("You picked paper")
        case "paper":
            print("You picked scissors.")
    # Rock beats scissors
    
    # Scissors beat paper
    
    # Paper beats rock
    
    # What message should you show the user?
    
    print("You lost, tied, or won!")