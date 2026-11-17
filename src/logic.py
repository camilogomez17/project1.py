import random

def rock_paper_scissors():
    game_running = True
    
    while game_running:
        
        moves = {
                    "rock": 0,
                    "paper": 1,
                    "scissors": 2,
                    "quit":3
                }
        
        user_string = input("Choose a move (rock, paper, or scissors):").lower().strip()
        
        if user_string == 4:
            break
        
        computer_choice = random.randint(1, 2)
        
        user_digit = moves[user_string]
        
        print(user_digit)
    