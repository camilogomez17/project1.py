import random

from game_data import game_stats

def rock_paper_scissors():
    game_running = True
    
    results = ["Draw", "You win!", "Computer wins!"]
    
    moves = {
                        "rock": 0,
                        "paper": 1,
                        "scissors": 2,
                        "quit":3
                    }
    
    stat_keys = ["ties", "wins", "losses"]
    
    game_stats[stat_keys[result]]
    
    while game_running:
        
        user_string = input("\nChoose a move (rock, paper, or scissors):").lower().strip()
        
        if user_string == "quit":
            break
        
        if user_string not in moves:
            print("move is invalid")
            continue
        
        computer_choice = random.randrange(3)
        
        user_digit = moves[user_string]
        
        result = (user_digit - computer_choice) % 3
        
        print(results[result])
    