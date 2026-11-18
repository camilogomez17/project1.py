import random

from game_data import game_stats

def rock_paper_scissors():
    
    results = ["Draw", "You win!", "Computer wins!"]
    
    moves = {
                        "rock": 0,
                        "paper": 1,
                        "scissors": 2,
                        "quit":3
                    }
    
    move_names = ["rock", "paper", "scissors"]
    
    stat_keys = ["ties", "wins", "losses"]
    
    while True:
        
        user_string = input("\nChoose a move (rock, paper, or scissors):").lower().strip()
        
        if user_string == "quit":
            break
        
        if user_string not in moves:
            print("move is invalid")
            continue
        
        computer_choice = random.randrange(3)
        
        computer_move = move_names[computer_choice]
        
        user_digit = moves[user_string]
        
        result = (user_digit - computer_choice) % 3
        
        game_stats[stat_keys[result]] += 1
        
        print(f"You chose {computer_move}\nComputer chose {computer_move}\n{results[result]}")