"""Text interface and menu actions for Rock, Paper, Scissors."""

from game import CHOICES, determine_result, play_round
from game_data import (
    add_game,
    delete_game,
    game_history,
    get_statistics,
    update_game,
)


def display_menu():
    """Print the main menu."""
    print(
        "\n=== Rock, Paper, Scissors ===\n"
        "1. Play a game\n"
        "2. View game history\n"
        "3. Edit or delete a game\n"
        "4. View statistics\n"
        "5. Quit"
    )


def get_menu_choice():
    """Return a valid menu number, or None when the input is not numeric."""
    try:
        return int(input("Select an option: ").strip())
    except ValueError:
        return None


def display_history():
    """Print every saved game in a readable format."""
    if not game_history:
        print("\nNo games have been played yet.")
        return

    print("\n=== Game History ===")
    for index, game in enumerate(game_history, start=1):
        print(
            f"{index}. {game['played_at']} | "
            f"You: {game['user_choice']} | "
            f"Computer: {game['computer_choice']} | "
            f"Result: {game['result'].title()}"
        )


def play_game():
    """Play one round and store its result."""
    user_choice, computer_choice, result = play_round()
    add_game(user_choice, computer_choice, result)
    print("Game saved to your history.")


def get_game_index():
    """Ask for a displayed game number and convert it to a list index."""
    if not game_history:
        print("There are no games to edit or delete.")
        return None

    display_history()
    try:
        selected_number = int(input("Enter the game number: ").strip())
    except ValueError:
        print("Please enter a whole number.")
        return None

    index = selected_number - 1
    if index < 0 or index >= len(game_history):
        print("That game number does not exist.")
        return None
    return index


def edit_game():
    """Change the choices in a selected record and recalculate its outcome."""
    index = get_game_index()
    if index is None:
        return

    print("Enter the corrected choices for this record.")
    while True:
        user_choice = input("Player choice (rock/paper/scissors): ").strip().lower()
        if user_choice in CHOICES:
            break
        print("Invalid choice. Try again.")

    while True:
        computer_choice = input("Computer choice (rock/paper/scissors): ").strip().lower()
        if computer_choice in CHOICES:
            break
        print("Invalid choice. Try again.")

    result = determine_result(user_choice, computer_choice)
    update_game(index, user_choice, computer_choice, result)
    print("Game record updated.")


def remove_game():
    """Delete a selected game record after confirmation."""
    index = get_game_index()
    if index is None:
        return

    confirmation = input("Delete this game? (yes/no): ").strip().lower()
    if confirmation == "yes":
        delete_game(index)
        print("Game record deleted.")
    elif confirmation == "no":
        print("Deletion cancelled.")
    else:
        print("Please enter yes or no. Nothing was deleted.")


def manage_history():
    """Offer edit and delete actions for a selected history record."""
    if not game_history:
        print("\nThere are no games to manage.")
        return

    print("\n1. Edit a game\n2. Delete a game\n3. Return to main menu")
    try:
        choice = int(input("Select an option: ").strip())
    except ValueError:
        print("Please enter 1, 2, or 3.")
        return

    if choice == 1:
        edit_game()
    elif choice == 2:
        remove_game()
    elif choice == 3:
        return
    else:
        print("Invalid selection. Choose 1, 2, or 3.")


def display_statistics():
    """Print totals calculated from the saved game records."""
    statistics = get_statistics()
    print("\n=== Statistics ===")
    print(f"Wins: {statistics['wins']}")
    print(f"Losses: {statistics['losses']}")
    print(f"Ties: {statistics['ties']}")
    print(f"Total games: {statistics['total']}")


def run_menu():
    """Keep showing the menu until the user chooses to quit."""
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            play_game()
        elif choice == 2:
            display_history()
        elif choice == 3:
            manage_history()
        elif choice == 4:
            display_statistics()
        elif choice == 5:
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Invalid selection. Enter a number from 1 to 5.")
