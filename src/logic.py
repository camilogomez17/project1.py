import random

def rock_paper_scissors():
    game_running = True
    
    results = ["Draw", "You win!", "Computer wins!"]
    
    while game_running:
        
        moves = {
                    "rock": 0,
                    "paper": 1,
                    "scissors": 2,
                    "quit":3
                }
        
        user_string = input("\nChoose a move (rock, paper, or scissors):").lower().strip()
        
        if user_string == "quit":
            break
        
        if user_string not in moves:
            print("move is invalid")
            continue
        
        computer_choice = random.randint(1, 2)
        
        user_digit = moves[user_string]
        
        game_logic = (user_digit - computer_choice) % 3
    