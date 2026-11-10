from game_data import game_stats
import random

print(game_stats)
# Start your CLI app here.
def rock_paper_scissors():
    menu_display = True
    while menu_display:
        print("Welcome to the game.\n" \
        "1. Play Tic Tac Toe\n" \
        "2. View Stats\n" \
        "3. Quit\n" \
        "Select?")
        # Need to select from menu
        menu_select = int(input())
        match menu_select:
            case 1:
                # Play game
                return menu_select
            case 2:
                # View Stats
                return menu_select
            case 3:
                break


    
# Run it with:  python3 src/main.py

rock_paper_scissors()

# The brief is in PROJECT.md.