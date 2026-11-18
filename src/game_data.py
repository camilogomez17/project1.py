game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0,
}

def view_stats():
    
    # calculate total games
    
    total_games = game_stats["wins"] + game_stats["losses"] + game_stats["ties"]
    
    # calculate win rate if total_games is not zero
    
    if total_games == 0:
        print("Please play a game.")
    else:
        win_rate = (game_stats["wins"] / total_games) * 100
        # display statistics
        print(f"{game_stats}\nwin_rate:{win_rate}%")