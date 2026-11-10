# Example: game_data.py (Rock Paper Scissors)
game_stats = {"wins": 0, "losses": 0, "ties": 0}

def view_stats():
    print("\nCurrent Statistics:")
    print(f"Games Won: {game_stats['wins']}")
    print(f"Games Lost: {game_stats['losses']}")
    print(f"Games Tied: {game_stats['ties']}")
    total = game_stats["wins"] + game_stats["losses"] + game_stats["ties"]
    print(f"Total Games: {total}")