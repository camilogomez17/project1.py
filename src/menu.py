from game_data import view_stats
from play_game import run_game
    
def show_menu():
    is_running = True
    while is_running:
        print("\nMenu: ")
        print("1. Play rock, paper, scissors!")
        print("2. View Statistics")
        print("3. Exit")
        
        choice = input("Please choose an option!")
        
        print(f"You chose: {choice}")
        
        if choice == "1":
            run_game()
        elif choice == "2":
            view_stats()
        elif choice == "3":
            is_running = False
            break
        else:
            print("Invalid choice. Please try again.")
            continue