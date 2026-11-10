from game_data import game_stats
import random

print(game_stats)
# Start your CLI app here.
def rock_paper_scissors():
    computer_choice = random.randint(1, 3)
    menu_display = True
    while menu_display:
        print("Welcome to the game.\n" \
        "1. Play Tic Tac Toe\n" \
        "2. View Stats\n" \
        "3. Quit")
        selection = input()


    
# Run it with:  python3 src/main.py

rock_paper_scissors()

# The brief is in PROJECT.md.