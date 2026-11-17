import random

def run_game():
    
    game_playing = True
    
    while game_playing:
        
        #computer and user picks
        
        def choices():
            p = int(input("Pick:\n0. Rock\n1. Paper\n2. Scissors"))
            c = random.randint(0,2)
        
        choices()
        
        # define game logic
        def rock_paper_scissors(p, c):
            return (p - c) % 3
    
        rock_paper_scissors()
        # tell the user the result
    
        def game_winner():
            print("Winner is #placeholder")
    
        game_winner()
        # update the game_data
    
        def update_game_data():
            print("Data updated!")
        
        update_game_data()
        
        # ask user to play again
    
        def play_or_quit():
            playing_or_quitting = input("\n\nContinue playing?\n1. Yes\n2. No\n")
            if playing_or_quitting == "1":
                print("Game continuing...\n")
                continue
            elif playing_or_quitting == "2":
                break
            else:
                playing_or_quitting = input("\nInvalid input.\nContinue playing?\n1. Yes\n2. No\n")
        
        play_or_quit()
        
    