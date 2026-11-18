game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0,
}

def view_stats():
    
    # calculate total games
    
    total_games = game_stats["wins"] + game_stats["losses"] + game_stats["ties"]

    #check whether total games is zero
    
    is_zero = total_games == 0
    
    win_rate = (game_stats["wins"] / total_games) * 100

def view_stats():
    print(game_stats)