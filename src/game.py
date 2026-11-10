"""Game rules and one-round gameplay."""

import random

CHOICES = ("rock", "paper", "scissors")


def determine_result(user_choice, computer_choice):
    """Return 'win', 'loss', or 'tie' for a valid pair of choices."""
    if user_choice == computer_choice:
        return "tie"

    winning_pairs = {
        ("rock", "scissors"),
        ("paper", "rock"),
        ("scissors", "paper"),
    }
    if (user_choice, computer_choice) in winning_pairs:
        return "win"
    return "loss"


def play_round():
    """Ask for a valid player choice, play the computer, and return the round."""
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_choice in CHOICES:
            break
        print("Invalid choice. Enter rock, paper, or scissors.")

    computer_choice = random.choice(CHOICES)
    result = determine_result(user_choice, computer_choice)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    messages = {
        "win": "You win!",
        "loss": "You lose.",
        "tie": "It is a tie.",
    }
    print(messages[result])

    return user_choice, computer_choice, result
