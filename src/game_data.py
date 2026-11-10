"""In-memory game history and operations on its records."""

from datetime import datetime

# Each game is a dictionary; the complete history is a list of dictionaries.
game_history = []


def add_game(user_choice, computer_choice, result):
    """Add one completed game to the history and return the new record."""
    game = {
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
        "played_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    game_history.append(game)
    return game


def update_game(index, user_choice, computer_choice, result):
    """Update the choices and outcome for a game at the given list index."""
    if index < 0 or index >= len(game_history):
        return False

    game_history[index]["user_choice"] = user_choice
    game_history[index]["computer_choice"] = computer_choice
    game_history[index]["result"] = result
    return True


def delete_game(index):
    """Remove a game at the given list index."""
    if index < 0 or index >= len(game_history):
        return False

    game_history.pop(index)
    return True


def get_statistics():
    """Calculate win, loss, tie, and total counts from the game history."""
    statistics = {"wins": 0, "losses": 0, "ties": 0}

    for game in game_history:
        if game["result"] == "win":
            statistics["wins"] += 1
        elif game["result"] == "loss":
            statistics["losses"] += 1
        elif game["result"] == "tie":
            statistics["ties"] += 1

    statistics["total"] = len(game_history)
    return statistics
