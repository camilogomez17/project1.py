
from game_data import game_stats
import random


def rock_paper_scissors():
    menu_display = True

    while menu_display:
        print(
            "\nWelcome to the game.\n"
            "1. Play Rock, Paper, Scissors.\n"
            "2. View Stats.\n"
            "3. Quit.\n"
            "Select?"
        )

        # Get menu selection
        try:
            menu_select = int(input())
        except ValueError:
            print("Please enter 1, 2, or 3.")
            continue

        match menu_select:
            case 1:
                # Play game
                print("\nWelcome to the game!")

                # Get user's choice
                user_choice = input(
                    "Pick rock, paper, or scissors!\nChoice: "
                ).lower()

                # Validate user input
                while user_choice not in ["rock", "paper", "scissors"]:
                    print("Invalid choice. Please try again.")
                    user_choice = input(
                        "Pick rock, paper, or scissors!\nChoice: "
                    ).lower()

                # Computer randomly selects a choice
                computer_play = random.randint(1, 3)

                match computer_play:
                    case 1:
                        computer_choice = "rock"
                    case 2:
                        computer_choice = "paper"
                    case 3:
                        computer_choice = "scissors"

                print(f"Computer picks {computer_choice}.")

                # Determine the winner
                if user_choice == computer_choice:
                    print("You tie! :|")
                    game_stats["ties"] += 1

                elif (
                    (user_choice == "rock" and computer_choice == "scissors")
                    or (user_choice == "paper" and computer_choice == "rock")
                    or (user_choice == "scissors" and computer_choice == "paper")
                ):
                    print("You win!!! :D")
                    game_stats["wins"] += 1

                else:
                    print("You lose... :(")
                    game_stats["losses"] += 1

                # Ask whether the user wants to continue
                while True:
                    continue_playing = input(
                        "\nContinue?\nChoice (yes/no): "
                    ).lower()

                    if continue_playing == "yes":
                        break
                    elif continue_playing == "no":
                        print("Returning to main menu...")
                        break
                    else:
                        print("Please pick yes or no.")

                if continue_playing == "yes":
                    continue

            case 2:
                # View stats
                print("\nGame Statistics:")
                print(game_stats)

            case 3:
                # Quit game
                print("Bye bye!")
                return

            case _:
                print("Invalid selection. Please choose 1, 2, or 3.")


# Run the game
if __name__ == "__main__":
    rock_paper_scissors()
