import random

def rock_paper_scissors():
    game_running = True
    
    while game_running:
        user_string = moves[input("Choose a move (rock, paper, or scissors):").lower().strip()]
        
        moves = {
            "rock": 0,
            "paper": 1,
            "scissors": 2
        }
        
        computer_choice = random.randint(1, 2)
        
        
        # convert string to int and assign value
    