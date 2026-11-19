game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0,
}

# calculate total games
total_games = game_stats["wins"] + game_stats["losses"] + game_stats["ties"]

def view_stats():
    
    # calculate win rate if total_games is not zero
    
    if total_games == 0:
        print("\nPlease play a game.")
    else:
        win_rate = (game_stats["wins"] / total_games) * 100
        # display statistics
        print(f"\nTotal games:{total_games}\n\nWins:{game_stats["wins"]}\nTies:{game_stats["ties"]}\nLosses:{game_stats["losses"]}\nWin rate:{win_rate}%")
        return game_stats["wins"] + game_stats["losses"] + game_stats["ties"]